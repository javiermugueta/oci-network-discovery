#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OCI Network Discovery Tool

Esta herramienta descubre y documenta toda la configuración de red en un tenant de Oracle Cloud Infrastructure.
"""

import oci
import argparse
import os
import sys
import json
from datetime import datetime
from tabulate import tabulate
import pandas as pd
from pathlib import Path
import hashlib
import pickle

# Módulos internos
from modules.auth import authenticate_oci, get_regions
from modules.vcn import get_vcns, get_subnets, get_route_tables, get_security_lists, get_network_security_groups
from modules.gateways import get_internet_gateways, get_nat_gateways, get_service_gateways
from modules.drg import get_drgs, get_drg_attachments, get_remote_peering_connections
from modules.vpn import get_vpn_connections
from modules.fastconnect import get_fastconnect_connections
from modules.report import generate_markdown_report


def parse_arguments():
    """
    Analiza los argumentos de línea de comandos.
    """
    parser = argparse.ArgumentParser(description='OCI Network Discovery Tool')
    parser.add_argument('--config', default='~/.oci/config', help='Path to OCI config file')
    parser.add_argument('--profile', default='DEFAULT', help='OCI config profile')
    parser.add_argument('--output-dir', default='./output', help='Output directory for reports')
    parser.add_argument('--all-regions', action='store_true', help='Discover all available regions')
    parser.add_argument('--regions', nargs='+', help='Specific regions to discover')
    parser.add_argument('--no-cache', action='store_true', help='Disable cache usage for discovery')
    parser.add_argument('--refresh-cache', action='store_true', help='Force refresh cache even if available')
    
    return parser.parse_args()


def create_output_directory(output_dir):
    """
    Crea el directorio de salida si no existe.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def discover_network_resources(config, profile, regions, output_dir):
    """
    Descubre todos los recursos de red en las regiones especificadas.
    """
    # Autenticar con OCI
    config_dict, identity_client = authenticate_oci(config, profile)
    
    # Si no se especifican regiones, preguntar al usuario
    if not regions:
        available_regions = get_regions(identity_client)
        print("Regiones disponibles:")
        for i, region in enumerate(available_regions, 1):
            print(f"{i}. {region}")
        
        selected_indices = input("\nSeleccione las regiones a analizar (números separados por comas, 'all' para todas): ")
        
        if selected_indices.lower() == 'all':
            selected_regions = available_regions
        else:
            try:
                indices = [int(idx.strip()) - 1 for idx in selected_indices.split(',')]
                selected_regions = [available_regions[idx] for idx in indices if 0 <= idx < len(available_regions)]
            except (ValueError, IndexError):
                print("Selección inválida. Utilizando la región home.")
                selected_regions = [config_dict['region']]
    else:
        # Parse regions - handle both comma-separated strings and lists
        if isinstance(regions, list) and len(regions) == 1 and ',' in regions[0]:
            # Handle case where --regions "20,1" becomes ['20,1']
            selected_regions = [r.strip() for r in regions[0].split(',')]
        elif isinstance(regions, str):
            selected_regions = [r.strip() for r in regions.split(',')]
        else:
            selected_regions = regions
    
    # Crear directorio de salida
    output_path = create_output_directory(output_dir)
    
    # Obtener tenancy_id
    tenancy_id = config_dict['tenancy']
    
    # Preparar caché (por tenant, perfil y regiones)
    def compute_cache_path(base_dir: Path, tenancy: str, profile_name: str, region_list):
        regions_key = ','.join(sorted(region_list))
        key = f"{tenancy}|{profile_name}|{regions_key}"
        key_hash = hashlib.sha256(key.encode('utf-8')).hexdigest()[:16]
        return base_dir / f"oci_network_cache_{profile_name}_{key_hash}.pkl"
    
    cache_file = compute_cache_path(output_path, tenancy_id, profile, selected_regions)
    use_cache = ('--no-cache' not in sys.argv)
    refresh_cache = ('--refresh-cache' in sys.argv)
    
    # Intentar cargar caché existente
    all_resources = {}
    if use_cache and cache_file.exists() and not refresh_cache:
        try:
            with open(cache_file, 'rb') as cf:
                all_resources = pickle.load(cf)
            print(f"Cargado desde caché: {cache_file}")
            # Validar que las regiones en caché coinciden con las solicitadas
            cached_regions = set(all_resources.keys()) if isinstance(all_resources, dict) else set()
            requested_regions = set(selected_regions)
            if cached_regions and cached_regions != requested_regions:
                print("Las regiones de la caché no coinciden con las solicitadas. Ignorando caché.")
                all_resources = {}
        except Exception as e:
            print(f"No se pudo cargar la caché ({e}). Se realizará el descubrimiento completo.")
            all_resources = {}
    
    # Descubrir recursos si no hay datos en caché
    if not all_resources:
        all_resources = {}
    
    # Descubrir recursos en cada región
    if not all_resources:
        for region in selected_regions:
            print(f"\nDescubriendo recursos de red en la región: {region}")
            
            # Configurar clientes para esta región
            config_dict['region'] = region
            
            # Crear clientes de OCI para esta región
            network_client = oci.core.VirtualNetworkClient(config_dict)
            identity_client_regional = oci.identity.IdentityClient(config_dict)
            
            # Obtener todos los compartments
            compartments = get_all_compartments(identity_client_regional, tenancy_id)
            
            # Inicializar recursos para esta región
            region_resources = {
                'vcns': [],
                'subnets': [],
                'route_tables': [],
                'security_lists': [],
                'network_security_groups': [],
                'internet_gateways': [],
                'nat_gateways': [],
                'service_gateways': [],
                'drgs': [],
                'drg_attachments': [],
                'drg_route_tables': [],
                'drg_route_distributions': [],
                'remote_peering_connections': [],
                'vpn_connections': [],
                'fastconnect_connections': [],
                'vpn_tunnels': [],
                'cross_connect_groups': [],
                'cross_connects': []
            }
            
            # Descubrir recursos en cada compartment
            for compartment in compartments:
                compartment_id = compartment.id
                compartment_name = compartment.name
                print(f"  Analizando compartment: {compartment_name}")
                
                # VCNs y componentes relacionados
                vcns = get_vcns(network_client, compartment_id)
                region_resources['vcns'].extend(vcns)
                
                for vcn in vcns:
                    vcn_id = vcn.id
                    print(f"    Analizando VCN: {vcn.display_name}")
                    
                    # Subnets
                    subnets = get_subnets(network_client, compartment_id, vcn_id)
                    region_resources['subnets'].extend(subnets)
                    
                    # Route Tables
                    route_tables = get_route_tables(network_client, compartment_id, vcn_id)
                    region_resources['route_tables'].extend(route_tables)
                    
                    # Security Lists
                    security_lists = get_security_lists(network_client, compartment_id, vcn_id)
                    region_resources['security_lists'].extend(security_lists)
                    
                    # Network Security Groups
                    nsgs = get_network_security_groups(network_client, compartment_id, vcn_id)
                    region_resources['network_security_groups'].extend(nsgs)
                    
                    # Internet Gateways
                    igws = get_internet_gateways(network_client, compartment_id, vcn_id)
                    region_resources['internet_gateways'].extend(igws)
                    
                    # NAT Gateways
                    nat_gws = get_nat_gateways(network_client, compartment_id, vcn_id)
                    region_resources['nat_gateways'].extend(nat_gws)
                    
                    # Service Gateways
                    sgws = get_service_gateways(network_client, compartment_id, vcn_id)
                    region_resources['service_gateways'].extend(sgws)
                
                # DRGs y componentes relacionados
                drgs = get_drgs(network_client, compartment_id)
                region_resources['drgs'].extend(drgs)
                
                for drg in drgs:
                    drg_id = drg.id
                    print(f"    Analizando DRG: {drg.display_name}")
                    
                    # DRG Attachments - buscar en TODOS los compartments de la región
                    # ya que los attachments pueden estar en cualquier compartment con acceso al DRG
                    for comp in compartments:
                        attachments = get_drg_attachments(network_client, comp.id, drg_id)
                        region_resources['drg_attachments'].extend(attachments)
                    
                    # Remote Peering Connections
                    rpcs = get_remote_peering_connections(network_client, compartment_id, drg_id)
                    region_resources['remote_peering_connections'].extend(rpcs)
                    
                    # DRG Route Tables
                    from modules.drg import get_drg_route_tables
                    route_tables = get_drg_route_tables(network_client, drg_id)
                    if 'drg_route_tables' not in region_resources:
                        region_resources['drg_route_tables'] = []
                    region_resources['drg_route_tables'].extend(route_tables)
                    
                    # DRG Route Distributions
                    from modules.drg import get_drg_route_distributions
                    distributions = get_drg_route_distributions(network_client, drg_id)
                    if 'drg_route_distributions' not in region_resources:
                        region_resources['drg_route_distributions'] = []
                    region_resources['drg_route_distributions'].extend(distributions)
                
                # VPN Connections
                vpns = get_vpn_connections(network_client, compartment_id)
                region_resources['vpn_connections'].extend(vpns)
                
                # Obtener túneles VPN para cada conexión
                for vpn in vpns:
                    vpn_id = vpn.id
                    print(f"    Analizando túneles VPN para: {vpn.display_name}")
                    
                    # Túneles VPN
                    from modules.vpn import get_vpn_tunnels
                    tunnels = get_vpn_tunnels(network_client, vpn_id)
                    if 'vpn_tunnels' not in region_resources:
                        region_resources['vpn_tunnels'] = []
                    region_resources['vpn_tunnels'].extend(tunnels)
                
                # FastConnect Connections
                fastconnects = get_fastconnect_connections(network_client, compartment_id)
                region_resources['fastconnect_connections'].extend(fastconnects)
                
                # Obtener información detallada de FastConnect
                for fc in fastconnects:
                    fc_id = fc.id
                    print(f"    Analizando detalles de FastConnect: {fc.display_name}")
                    
                    # Cross-Connect Groups
                    from modules.fastconnect import get_cross_connect_groups
                    cross_connect_groups = get_cross_connect_groups(network_client, compartment_id)
                    if 'cross_connect_groups' not in region_resources:
                        region_resources['cross_connect_groups'] = []
                    region_resources['cross_connect_groups'].extend(cross_connect_groups)
                    
                    # Cross-Connects
                    from modules.fastconnect import get_cross_connects
                    cross_connects = get_cross_connects(network_client, compartment_id)
                    if 'cross_connects' not in region_resources:
                        region_resources['cross_connects'] = []
                    region_resources['cross_connects'].extend(cross_connects)
            
            # Guardar recursos de esta región
            all_resources[region] = region_resources
    
    # Guardar caché si procede
    if use_cache:
        try:
            with open(cache_file, 'wb') as cf:
                pickle.dump(all_resources, cf)
            print(f"Caché escrita en: {cache_file}")
        except Exception as e:
            print(f"No se pudo escribir la caché: {e}")
    
    # Generar informe
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    markdown_file = output_path / f"oci_network_report_{timestamp}.md"
    generate_markdown_report(all_resources, markdown_file, config_dict)
    
    # Generar diagrama Draw.io avanzado
    try:
        from modules.diagram_generator import generate_advanced_oci_network_diagram
        diagram_file = output_path / f"oci_network_diagram_{timestamp}.drawio"
        generate_advanced_oci_network_diagram(all_resources, diagram_file)
        print(f"Diagrama Draw.io avanzado generado en: {diagram_file}")
    except ImportError as e:
        print(f"No se pudo generar el diagrama: {e}")
    
    print(f"\nInforme generado en: {markdown_file}")


def get_all_compartments(identity_client, tenancy_id):
    """
    Obtiene todos los compartments en el tenancy, incluido el root compartment.
    """
    # Obtener el root compartment
    root_compartment = identity_client.get_compartment(tenancy_id).data
    compartments = [root_compartment]
    
    # Obtener todos los compartments hijos
    list_compartments_response = oci.pagination.list_call_get_all_results(
        identity_client.list_compartments,
        tenancy_id,
        compartment_id_in_subtree=True,
        access_level="ACCESSIBLE",
        lifecycle_state="ACTIVE"
    )
    
    compartments.extend(list_compartments_response.data)
    return compartments


def main():
    """
    Función principal.
    """
    args = parse_arguments()
    
    try:
        discover_network_resources(
            args.config,
            args.profile,
            args.regions if args.regions else None,
            args.output_dir
        )
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()