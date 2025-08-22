#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo para generar informes y diagramas de red.
"""

import os
import json
import pandas as pd
from tabulate import tabulate
from datetime import datetime
import subprocess
from pathlib import Path
import math


def generate_markdown_report(resources, output_file, config_dict=None):
    """
    Genera un informe en formato markdown con tablas para todos los recursos de red.
    
    Args:
        resources (dict): Diccionario con todos los recursos de red por región.
        output_file (Path): Ruta del archivo de salida.
        config_dict (dict, optional): Configuración de OCI para crear clientes de red.
    """
    import oci
    
    # Resolver de nombres de compartments con caché para minimizar llamadas
    compartment_name_cache = {}
    identity_client = None
    if config_dict:
        try:
            identity_client = oci.identity.IdentityClient(config_dict)
        except Exception:
            identity_client = None
    
    def resolve_compartment_name(compartment_id):
        if not compartment_id:
            return ""
        if compartment_id in compartment_name_cache:
            return compartment_name_cache[compartment_id]
        name = ""
        try:
            if identity_client:
                resp = identity_client.get_compartment(compartment_id)
                if hasattr(resp, 'data') and hasattr(resp.data, 'name'):
                    name = resp.data.name
        except Exception:
            name = ""
        compartment_name_cache[compartment_id] = name
        return name
    with open(output_file, 'w') as f:
        f.write("# Informe de Infraestructura de Red en OCI\n\n")
        f.write(f"Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        # Índice con enlaces por región y secciones principales
        f.write("## Índice\n")
        for region in resources.keys():
            safe_region = region.replace(' ', '-').replace('(', '').replace(')', '')
            f.write(f"- [{region}](#region-{safe_region})\n")
            f.write(f"  - [VCNs](#region-{safe_region}-vcns)\n")
            f.write(f"  - [DRGs](#region-{safe_region}-drgs)\n")
            f.write(f"  - [Conexiones VPN IPSec](#region-{safe_region}-vpn)\n")
            f.write(f"  - [Conexiones FastConnect](#region-{safe_region}-fc)\n")
            f.write(f"  - [Recursos por VCN](#region-{safe_region}-vcns)\n")
        f.write("\n")
        
        # Iterar por cada región
        for region, region_resources in resources.items():
            safe_region = region.replace(' ', '-').replace('(', '').replace(')', '')
            f.write(f"<a id=\"region-{safe_region}\"></a>\n")
            f.write(f"## Región: {region}\n\n")
            
            # VCNs
            f.write("### Virtual Cloud Networks (VCNs)\n\n")
            if region_resources['vcns']:
                vcns_data = []
                for vcn in region_resources['vcns']:
                    vcn_id_safe = vcn.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    vcn_link = f"[{vcn.display_name}](#vcn-{vcn_id_safe})"
                    compartment_name = resolve_compartment_name(getattr(vcn, 'compartment_id', ''))
                    # Mostrar siempre "Nombre (OCID)"; si no hay nombre, usar "Desconocido"
                    compartment_display = f"{compartment_name or 'Desconocido'} ({vcn.compartment_id})"
                    vcns_data.append({
                        'ID': vcn.id,
                        'Nombre': vcn_link,
                        'CIDR': vcn.cidr_block,
                        'Estado': vcn.lifecycle_state,
                        'Compartment': compartment_display
                    })
                
                df = pd.DataFrame(vcns_data)
                f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                
                # Iterar por cada VCN para mostrar sus recursos asociados
                for vcn in region_resources['vcns']:
                    vcn_id_safe = vcn.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    f.write(f"<a id=\"vcn-{vcn_id_safe}\"></a>\n")
                    f.write(f"#### Recursos de VCN: {vcn.display_name} (ID: {vcn.id})\n\n")
                    
                    # Subnets de esta VCN
                    f.write("##### Subnets\n\n")
                    vcn_subnets = [subnet for subnet in region_resources['subnets'] if subnet.vcn_id == vcn.id]
                    if vcn_subnets:
                        subnets_data = []
                        for subnet in vcn_subnets:
                            # Buscar la tabla de rutas asociada a esta subnet
                            route_table_name = "Default"
                            route_table_id = "Default"
                            route_table_link = ""
                            if hasattr(subnet, 'route_table_id') and subnet.route_table_id:
                                for rt in region_resources['route_tables']:
                                    if rt.id == subnet.route_table_id:
                                        route_table_name = rt.display_name
                                        route_table_id = rt.id
                                        rt_id_safe = rt.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                        route_table_link = f"[{rt.display_name}](#rt-{rt_id_safe})"
                                        break
                            
                            # Buscar las Security Lists asociadas a esta subnet
                            security_lists_info = []
                            security_lists_links = []
                            if hasattr(subnet, 'security_list_ids') and subnet.security_list_ids:
                                for sl_id in subnet.security_list_ids:
                                    for sl in region_resources['security_lists']:
                                        if sl.id == sl_id:
                                            sl_id_safe = sl.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                            sl_link = f"[{sl.display_name}](#sl-{sl_id_safe})"
                                            security_lists_info.append(sl.display_name)
                                            security_lists_links.append(sl_link)
                                            break
                            else:
                                # Si no hay security_list_ids específicos, buscar por VCN
                                for sl in region_resources['security_lists']:
                                    if sl.vcn_id == vcn.id:
                                        sl_id_safe = sl.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                        sl_link = f"[{sl.display_name}](#sl-{sl_id_safe})"
                                        security_lists_info.append(sl.display_name)
                                        security_lists_links.append(sl_link)
                            
                            # Crear texto para la columna Security Lists
                            if security_lists_links:
                                security_lists_text = ', '.join(security_lists_links)
                            else:
                                security_lists_text = "Default"
                            
                            subnets_data.append({
                                'ID': subnet.id,
                                'Nombre': subnet.display_name,
                                'CIDR': subnet.cidr_block,
                                'Disponibilidad': subnet.availability_domain or 'Regional',
                                'Pública': 'Sí' if subnet.prohibit_public_ip_on_vnic == False else 'No',
                                'Estado': subnet.lifecycle_state,
                                'Route Table': route_table_link if route_table_link else route_table_name,
                                'Route Table ID': route_table_id,
                                'Security Lists': security_lists_text
                            })
                        
                        df = pd.DataFrame(subnets_data)
                        f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                    else:
                        f.write("No se encontraron subnets en esta VCN.\n\n")
                    
                    # Route Tables de esta VCN
                    f.write("##### Tablas de Rutas\n\n")
                    vcn_route_tables = [rt for rt in region_resources['route_tables'] if rt.vcn_id == vcn.id]
                    if vcn_route_tables:
                        for rt in vcn_route_tables:
                            rt_id_safe = rt.id.replace('.', '_').replace(':', '_').replace('-', '_')
                            f.write(f"<a id=\"rt-{rt_id_safe}\"></a>\n")
                            f.write(f"###### {rt.display_name} (ID: {rt.id})\n\n")
                            
                            if rt.route_rules:
                                routes_data = []
                                for rule in rt.route_rules:
                                    network_entity_id = rule.network_entity_id
                                    entity_type = "Desconocido"
                                    entity_link = network_entity_id
                                    
                                    # Determinar tipo de entidad y crear links
                                    if any(igw.id == network_entity_id for igw in region_resources['internet_gateways']):
                                        entity_type = "Internet Gateway"
                                        igw_id_safe = network_entity_id.replace('.', '_').replace(':', '_').replace('-', '_')
                                        entity_link = f"[Internet Gateway](#igw-{igw_id_safe})"
                                    elif any(nat.id == network_entity_id for nat in region_resources['nat_gateways']):
                                        entity_type = "NAT Gateway"
                                        nat_id_safe = network_entity_id.replace('.', '_').replace(':', '_').replace('-', '_')
                                        entity_link = f"[NAT Gateway](#nat-{nat_id_safe})"
                                    elif any(sgw.id == network_entity_id for sgw in region_resources['service_gateways']):
                                        entity_type = "Service Gateway"
                                        sgw_id_safe = network_entity_id.replace('.', '_').replace(':', '_').replace('-', '_')
                                        entity_link = f"[Service Gateway](#sgw-{sgw_id_safe})"
                                    elif any(drg_attachment.drg_id == network_entity_id for drg_attachment in region_resources['drg_attachments']):
                                        entity_type = "DRG"
                                        drg_id_safe = network_entity_id.replace('.', '_').replace(':', '_').replace('-', '_')
                                        entity_link = f"[DRG](#drg-{drg_id_safe})"
                                    
                                    routes_data.append({
                                        'Destino': rule.destination,
                                        'Tipo de Destino': rule.destination_type,
                                        'Entidad de Red': entity_link,
                                        'Tipo de Entidad': entity_type,
                                        'Descripción': rule.description or ''
                                    })
                                
                                df = pd.DataFrame(routes_data)
                                f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                            else:
                                f.write("No hay reglas de ruta definidas.\n\n")
                    else:
                        f.write("No se encontraron tablas de rutas en esta VCN.\n\n")
                    
                    # Security Lists de esta VCN
                    f.write("##### Security Lists\n\n")
                    vcn_security_lists = [sl for sl in region_resources['security_lists'] if sl.vcn_id == vcn.id]
                    if vcn_security_lists:
                        for sl in vcn_security_lists:
                            sl_id_safe = sl.id.replace('.', '_').replace(':', '_').replace('-', '_')
                            f.write(f"<a id=\"sl-{sl_id_safe}\"></a>\n")
                            f.write(f"###### {sl.display_name} (ID: {sl.id})\n\n")
                            
                            # Reglas de entrada
                            f.write("####### Reglas de Entrada\n\n")
                            if sl.ingress_security_rules:
                                ingress_data = []
                                for rule in sl.ingress_security_rules:
                                    protocol = rule.protocol
                                    protocol_name = {
                                        "1": "ICMP",
                                        "6": "TCP",
                                        "17": "UDP",
                                        "all": "Todos"
                                    }.get(protocol, protocol)
                                    
                                    source = rule.source
                                    source_type = rule.source_type
                                    
                                    port_range = ""
                                    if hasattr(rule, 'tcp_options') and rule.tcp_options:
                                        if rule.tcp_options.destination_port_range:
                                            port_range = f"{rule.tcp_options.destination_port_range.min}-{rule.tcp_options.destination_port_range.max}"
                                        elif rule.tcp_options.source_port_range:
                                            port_range = f"{rule.tcp_options.source_port_range.min}-{rule.tcp_options.source_port_range.max}"
                                    elif hasattr(rule, 'udp_options') and rule.udp_options:
                                        if rule.udp_options.destination_port_range:
                                            port_range = f"{rule.udp_options.destination_port_range.min}-{rule.udp_options.destination_port_range.max}"
                                        elif rule.udp_options.source_port_range:
                                            port_range = f"{rule.udp_options.source_port_range.min}-{rule.udp_options.source_port_range.max}"
                                    
                                    ingress_data.append({
                                        'Origen': source,
                                        'Tipo de Origen': source_type,
                                        'Protocolo': protocol_name,
                                        'Puertos': port_range,
                                        'Descripción': rule.description or ''
                                    })
                                
                                df = pd.DataFrame(ingress_data)
                                f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                            else:
                                f.write("No hay reglas de entrada definidas.\n\n")
                            
                            # Reglas de salida
                            f.write("####### Reglas de Salida\n\n")
                            if sl.egress_security_rules:
                                egress_data = []
                                for rule in sl.egress_security_rules:
                                    protocol = rule.protocol
                                    protocol_name = {
                                        "1": "ICMP",
                                        "6": "TCP",
                                        "17": "UDP",
                                        "all": "Todos"
                                    }.get(protocol, protocol)
                                    
                                    destination = rule.destination
                                    destination_type = rule.destination_type
                                    
                                    port_range = ""
                                    if hasattr(rule, 'tcp_options') and rule.tcp_options:
                                        if rule.tcp_options.destination_port_range:
                                            port_range = f"{rule.tcp_options.destination_port_range.min}-{rule.tcp_options.destination_port_range.max}"
                                        elif rule.tcp_options.source_port_range:
                                            port_range = f"{rule.tcp_options.source_port_range.min}-{rule.tcp_options.source_port_range.max}"
                                    elif hasattr(rule, 'udp_options') and rule.udp_options:
                                        if rule.udp_options.destination_port_range:
                                            port_range = f"{rule.udp_options.destination_port_range.min}-{rule.udp_options.destination_port_range.max}"
                                        elif rule.udp_options.source_port_range:
                                            port_range = f"{rule.udp_options.source_port_range.min}-{rule.udp_options.source_port_range.max}"
                                    
                                    egress_data.append({
                                        'Destino': destination,
                                        'Tipo de Destino': destination_type,
                                        'Protocolo': protocol_name,
                                        'Puertos': port_range,
                                        'Descripción': rule.description or ''
                                    })
                                
                                df = pd.DataFrame(egress_data)
                                f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                            else:
                                f.write("No hay reglas de salida definidas.\n\n")
                    else:
                        f.write("No se encontraron security lists en esta VCN.\n\n")
                    
                    # DRG Attachments de esta VCN
                    f.write("##### DRG Attachments\n\n")
                    vcn_drg_attachments = [att for att in region_resources['drg_attachments'] if att.vcn_id == vcn.id]
                    if vcn_drg_attachments:
                        attachments_data = []
                        for att in vcn_drg_attachments:
                            # Buscar información del DRG
                            drg_name = "Desconocido"
                            for drg in region_resources['drgs']:
                                if drg.id == att.drg_id:
                                    drg_name = drg.display_name
                                    break
                            
                            attachments_data.append({
                                'ID': att.id,
                                'Nombre': att.display_name,
                                'DRG': f"[{drg_name}](#drg-{att.drg_id.replace('.', '_').replace(':', '_').replace('-', '_')})",
                                'Estado': att.lifecycle_state
                            })
                        
                        df = pd.DataFrame(attachments_data)
                        f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                    else:
                        f.write("No se encontraron DRG Attachments en esta VCN.\n\n")
                    
                    # Internet Gateways de esta VCN
                    f.write("##### Internet Gateways\n\n")
                    vcn_igws = [igw for igw in region_resources['internet_gateways'] if igw.vcn_id == vcn.id]
                    if vcn_igws:
                        igws_data = []
                        for igw in vcn_igws:
                            igw_id_safe = igw.id.replace('.', '_').replace(':', '_').replace('-', '_')
                            f.write(f"<a id=\"igw-{igw_id_safe}\"></a>\n")
                            igws_data.append({
                                'ID': igw.id,
                                'Nombre': igw.display_name,
                                'Habilitado': 'Sí' if igw.is_enabled else 'No',
                                'Estado': igw.lifecycle_state
                            })
                        
                        df = pd.DataFrame(igws_data)
                        f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                    else:
                        f.write("No se encontraron Internet Gateways en esta VCN.\n\n")
                    
                    # NAT Gateways de esta VCN
                    f.write("##### NAT Gateways\n\n")
                    vcn_nat_gws = [nat for nat in region_resources['nat_gateways'] if nat.vcn_id == vcn.id]
                    if vcn_nat_gws:
                        nat_gws_data = []
                        for nat in vcn_nat_gws:
                            nat_id_safe = nat.id.replace('.', '_').replace(':', '_').replace('-', '_')
                            f.write(f"<a id=\"nat-{nat_id_safe}\"></a>\n")
                            nat_gws_data.append({
                                'ID': nat.id,
                                'Nombre': nat.display_name,
                                'IP Pública': nat.nat_ip,
                                'Habilitado': 'Sí' if nat.block_traffic else 'No',
                                'Estado': nat.lifecycle_state
                            })
                        
                        df = pd.DataFrame(nat_gws_data)
                        f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                    else:
                        f.write("No se encontraron NAT Gateways en esta VCN.\n\n")
                    
                    # Service Gateways de esta VCN
                    f.write("##### Service Gateways\n\n")
                    vcn_sgws = [sgw for sgw in region_resources['service_gateways'] if sgw.vcn_id == vcn.id]
                    if vcn_sgws:
                        sgws_data = []
                        for sgw in vcn_sgws:
                            sgw_id_safe = sgw.id.replace('.', '_').replace(':', '_').replace('-', '_')
                            f.write(f"<a id=\"sgw-{sgw_id_safe}\"></a>\n")
                            services = [service.service_name for service in sgw.services] if sgw.services else []
                            sgws_data.append({
                                'ID': sgw.id,
                                'Nombre': sgw.display_name,
                                'Servicios': ', '.join(services),
                                'Estado': sgw.lifecycle_state
                            })
                        
                        df = pd.DataFrame(sgws_data)
                        f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                    else:
                        f.write("No se encontraron Service Gateways en esta VCN.\n\n")
            else:
                f.write("No se encontraron VCNs en esta región.\n\n")
            
            # Continuamos con los recursos que no están agrupados por VCN
            
            # DRGs
            f.write(f"<a id=\"region-{safe_region}-drgs\"></a>\n")
            f.write("### Dynamic Routing Gateways (DRGs)\n\n")
            if region_resources['drgs']:
                drgs_data = []
                for drg in region_resources['drgs']:
                    drg_id_safe = drg.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    f.write(f"<a id=\"drg-{drg_id_safe}\"></a>\n")
                    drgs_data.append({
                        'ID': drg.id,
                        'Nombre': drg.display_name,
                        'Compartment': drg.compartment_id,
                        'Estado': drg.lifecycle_state
                    })
                
                df = pd.DataFrame(drgs_data)
                f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                
                # DRG Attachments
                f.write("#### DRG Attachments\n\n")
                if region_resources['drg_attachments']:
                    attachments_data = []
                    for attachment in region_resources['drg_attachments']:
                        # Añadir anchor para este attachment
                        att_id_safe = attachment.id.replace('.', '_').replace(':', '_').replace('-', '_')
                        f.write(f'<a id="dra-{att_id_safe}"></a>\n')
                        
                        attachment_type = "Desconocido"
                        attached_resource = ""
                        attached_resource_name = ""
                        route_table_info = ""
                        vcn_link = ""
                        compartment_info = ""
                        
                        if attachment.vcn_id:
                            attachment_type = "VCN"
                            attached_resource = attachment.vcn_id
                            # Buscar el nombre de la VCN y su compartment
                            for vcn in region_resources['vcns']:
                                if vcn.id == attachment.vcn_id:
                                    attached_resource_name = vcn.display_name
                                    vcn_id_safe = vcn.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                    vcn_link = f"[{vcn.display_name}](#vcn-{vcn_id_safe})"
                                    # Obtener información del compartment de la VCN
                                    compartment_id = vcn.compartment_id
                                    compartment_name = compartment_id.split('.')[-1] if '.' in compartment_id else compartment_id
                                    compartment_info = f"Compartment: {compartment_name}"
                                    # Buscar la tabla de rutas asociada a esta VCN
                                    for rt in region_resources['route_tables']:
                                        if rt.vcn_id == attachment.vcn_id:
                                            rt_id_safe = rt.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                            route_table_info = f"[{rt.display_name}](#rt-{rt_id_safe})"
                                            break
                                    break
                        
                        attachments_data.append({
                            'ID': attachment.id,
                            'Nombre': attachment.display_name,
                            'DRG ID': attachment.drg_id,
                            'Tipo': attachment_type,
                            'Recurso': attached_resource,
                            'Nombre Recurso': vcn_link if vcn_link else attached_resource_name,
                            'Route Table': route_table_info,
                            'Compartment': compartment_info,
                            'Estado': attachment.lifecycle_state
                        })
                    
                    df = pd.DataFrame(attachments_data)
                    f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                else:
                    f.write("No se encontraron DRG Attachments en esta región.\n\n")
                
                # DRG Route Tables
                f.write("#### DRG Route Tables\n\n")
                if 'drg_route_tables' in region_resources and region_resources['drg_route_tables']:
                    for rt in region_resources['drg_route_tables']:
                        f.write(f"##### {rt.display_name} (ID: {rt.id})\n\n")
                        
                        # Crear link para Import Distribution si existe
                        import_dist_id = rt.import_drg_route_distribution_id
                        if import_dist_id:
                            # Buscar la distribución para crear el link
                            import_dist_link = ""
                            for dist in region_resources['drg_route_distributions']:
                                if dist.id == import_dist_id:
                                    dist_id_safe = dist.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                    import_dist_link = f"[{dist.display_name}](#drd-{dist_id_safe})"
                                    break
                            
                            if import_dist_link:
                                f.write(f"Import Distribution: {import_dist_link}\n\n")
                            else:
                                f.write(f"Import Distribution: {import_dist_id} (Distribución no encontrada)\n\n")
                        else:
                            f.write("Import Distribution: No configurada\n\n")
                        
                        # Obtener rutas de la tabla (solo estáticas)
                        routes_data = []
                        try:
                            # Crear cliente de red para esta región si es necesario
                            if config_dict:
                                region_config = config_dict.copy()
                                region_config['region'] = region
                                network_client = oci.core.VirtualNetworkClient(region_config)
                                
                                routes_response = oci.pagination.list_call_get_all_results(
                                    network_client.list_drg_route_rules,
                                    rt.id
                                )
                                
                                if routes_response and hasattr(routes_response, 'data') and routes_response.data:
                                    for rule in routes_response.data:
                                        route_type = getattr(rule, 'route_type', None)
                                        if str(route_type).upper() != 'STATIC':
                                            continue
                                        
                                        # Crear link para el Next Hop DRG Attachment si existe
                                        next_hop_info = getattr(rule, 'next_hop_drg_attachment_id', '')
                                        if next_hop_info:
                                            # Buscar el attachment para crear el link
                                            attachment_link = ""
                                            attachment_found = False
                                            
                                            for att in region_resources['drg_attachments']:
                                                if att.id == next_hop_info:
                                                    att_id_safe = att.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                                    attachment_link = f"[{att.display_name}](#dra-{att_id_safe})"
                                                    attachment_found = True
                                                    break
                                            
                                            if attachment_found:
                                                next_hop_display = attachment_link
                                            else:
                                                next_hop_display = f"{next_hop_info} (Attachment no encontrado)"
                                        else:
                                            next_hop_display = next_hop_info
                                        
                                        routes_data.append({
                                            'Destino': getattr(rule, 'destination', ''),
                                            'Tipo de Destino': getattr(rule, 'destination_type', ''),
                                            'Next Hop DRG Attachment': next_hop_display,
                                            'Origen': getattr(rule, 'route_provenance', ''),
                                            'Tipo de Ruta': str(route_type)
                                        })
                        except Exception as e:
                            f.write(f"Error al obtener reglas de ruta: {str(e)}\n\n")
                        
                        if routes_data:
                            df = pd.DataFrame(routes_data)
                            f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                        else:
                            f.write("No hay reglas de ruta estáticas definidas.\n\n")
                else:
                    f.write("No se encontraron tablas de rutas de DRG en esta región.\n\n")
                
                # DRG Route Distributions
                f.write("#### DRG Route Distributions (Import/Export)\n\n")
                if 'drg_route_distributions' in region_resources and region_resources['drg_route_distributions']:
                    for dist in region_resources['drg_route_distributions']:
                        # Añadir anchor para esta distribución
                        dist_id_safe = dist.id.replace('.', '_').replace(':', '_').replace('-', '_')
                        f.write(f'<a id="drd-{dist_id_safe}"></a>\n')
                        
                        f.write(f"##### {dist.display_name} (ID: {dist.id})\n\n")
                        f.write(f"Tipo de Distribución: {dist.distribution_type}\n\n")
                        
                        # Obtener statements de la distribución
                        statements_data = []
                        try:
                            # Crear cliente de red para esta región si es necesario
                            if config_dict:
                                region_config = config_dict.copy()
                                region_config['region'] = region
                                network_client = oci.core.VirtualNetworkClient(region_config)
                                
                                statements_response = oci.pagination.list_call_get_all_results(
                                    network_client.list_drg_route_distribution_statements,
                                    dist.id
                                )
                                
                                if statements_response and hasattr(statements_response, 'data') and statements_response.data:
                                    for stmt in statements_response.data:
                                        statements_data.append({
                                            'Prioridad': stmt.priority,
                                            'Tipo de Match': stmt.match_criteria.match_type if hasattr(stmt, 'match_criteria') and hasattr(stmt.match_criteria, 'match_type') else 'DESCONOCIDO',
                                            'Attachment Type': stmt.match_criteria.attachment_type if hasattr(stmt, 'match_criteria') and hasattr(stmt.match_criteria, 'attachment_type') else '',
                                            'DRG Attachment ID': stmt.match_criteria.drg_attachment_id if hasattr(stmt, 'match_criteria') and hasattr(stmt.match_criteria, 'drg_attachment_id') else '',
                                            'Acción': stmt.action
                                        })
                        except Exception as e:
                            f.write(f"Error al obtener statements de distribución: {str(e)}\n\n")
                        
                        if statements_data:
                            df = pd.DataFrame(statements_data)
                            f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                        else:
                            f.write("No hay statements de distribución definidos.\n\n")
                else:
                    f.write("No se encontraron distribuciones de rutas de DRG en esta región.\n\n")
                
                # Remote Peering Connections
                f.write("#### Remote Peering Connections\n\n")
                if region_resources['remote_peering_connections']:
                    rpcs_data = []
                    for rpc in region_resources['remote_peering_connections']:
                        rpcs_data.append({
                            'ID': rpc.id,
                            'Nombre': rpc.display_name,
                            'DRG ID': rpc.drg_id,
                            'Región Peer': rpc.peer_region_name or 'No conectado',
                            'RPC Peer ID': rpc.peer_id or 'No conectado',
                            'Estado': rpc.lifecycle_state,
                            'Estado Peering': rpc.peering_status
                        })
                    
                    df = pd.DataFrame(rpcs_data)
                    f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                else:
                    f.write("No se encontraron Remote Peering Connections en esta región.\n\n")
            else:
                f.write("No se encontraron DRGs en esta región.\n\n")
            
            # VPN Connections
            f.write(f"<a id=\"region-{safe_region}-vpn\"></a>\n")
            f.write("### Conexiones VPN IPSec\n\n")
            if region_resources['vpn_connections']:
                vpns_data = []
                for vpn in region_resources['vpn_connections']:
                    vpns_data.append({
                        'ID': vpn.id,
                        'Nombre': vpn.display_name,
                        'DRG ID': vpn.drg_id,
                        'CPE ID': vpn.cpe_id,
                        'IP CPE': vpn.cpe_local_identifier,
                        'IP CPE Tipo': vpn.cpe_local_identifier_type,
                        'Estado': vpn.lifecycle_state
                    })
                
                df = pd.DataFrame(vpns_data)
                f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                
                # Mostrar detalles de túneles VPN para cada conexión
                f.write("#### Detalles de Túneles VPN\n\n")
                for vpn in region_resources['vpn_connections']:
                    f.write(f"##### Túneles de {vpn.display_name}\n\n")
                    
                    # Buscar túneles para esta conexión VPN
                    vpn_tunnels = [t for t in region_resources.get('vpn_tunnels', []) if t.ipsec_id == vpn.id]
                    
                    if vpn_tunnels:
                        tunnels_data = []
                        for tunnel in vpn_tunnels:
                            tunnels_data.append({
                                'ID': tunnel.id,
                                'Estado': tunnel.lifecycle_state,
                                'Estado del Túnel': tunnel.status,
                                'IP Pública OCI': tunnel.vpn_ip,
                                'IP Pública CPE': tunnel.cpe_ip,
                                'Rango de IPs': tunnel.routing,
                                'Estado BGP': tunnel.bgp_session_info.state if hasattr(tunnel, 'bgp_session_info') and tunnel.bgp_session_info else 'N/A',
                                'ASN OCI': tunnel.bgp_session_info.oci_asn if hasattr(tunnel, 'bgp_session_info') and tunnel.bgp_session_info else 'N/A',
                                'ASN CPE': tunnel.bgp_session_info.customer_bgp_asn if hasattr(tunnel, 'bgp_session_info') and tunnel.bgp_session_info else 'N/A'
                            })
                        
                        df = pd.DataFrame(tunnels_data)
                        f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                    else:
                        f.write("No se encontraron túneles para esta conexión VPN.\n\n")
            else:
                f.write("No se encontraron conexiones VPN IPSec en esta región.\n\n")
            
            # FastConnect
            f.write(f"<a id=\"region-{safe_region}-fc\"></a>\n")
            f.write("### Conexiones FastConnect\n\n")
            if region_resources['fastconnect_connections']:
                fc_data = []
                for fc in region_resources['fastconnect_connections']:
                    fc_data.append({
                        'ID': fc.id,
                        'Nombre': fc.display_name,
                        'Tipo': fc.type,
                        'Ancho de Banda (Gbps)': fc.bandwidth_shape_name,
                        'DRG ID': fc.gateway_id,
                        'Proveedor': fc.provider_name or 'N/A',
                        'Estado': fc.lifecycle_state
                    })
                
                df = pd.DataFrame(fc_data)
                f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                
                # Mostrar detalles de Virtual Circuits y Cross-Connects
                f.write("#### Detalles de Virtual Circuits y Cross-Connects\n\n")
                
                # Cross-Connect Groups
                if 'cross_connect_groups' in region_resources and region_resources['cross_connect_groups']:
                    f.write("##### Cross-Connect Groups\n\n")
                    ccg_data = []
                    for ccg in region_resources['cross_connect_groups']:
                        ccg_data.append({
                            'ID': ccg.id,
                            'Nombre': ccg.display_name,
                            'Estado': ccg.lifecycle_state,
                            'Compartment': ccg.compartment_id
                        })
                    
                    df = pd.DataFrame(ccg_data)
                    f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                
                # Cross-Connects
                if 'cross_connects' in region_resources and region_resources['cross_connects']:
                    f.write("##### Cross-Connects\n\n")
                    cc_data = []
                    for cc in region_resources['cross_connects']:
                        cc_data.append({
                            'ID': cc.id,
                            'Nombre': cc.display_name,
                            'Estado': cc.lifecycle_state,
                            'Tipo': cc.port_speed_shape_name,
                            'Grupo': cc.cross_connect_group_id,
                            'Compartment': cc.compartment_id
                        })
                    
                    df = pd.DataFrame(cc_data)
                    f.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                
                # Detalles de cada Virtual Circuit
                f.write("##### Detalles de Virtual Circuits\n\n")
                for fc in region_resources['fastconnect_connections']:
                    f.write(f"###### Virtual Circuit: {fc.display_name}\n\n")
                    
                    # Información detallada del Virtual Circuit
                    vc_details = {
                        'ID': fc.id,
                        'Nombre': fc.display_name,
                        'Tipo': fc.type,
                        'Ancho de Banda': fc.bandwidth_shape_name,
                        'DRG ID': fc.gateway_id,
                        'Proveedor': fc.provider_name or 'N/A',
                        'Estado': fc.lifecycle_state,
                        'Compartment': fc.compartment_id,
                        'Fecha Creación': fc.time_created.strftime('%Y-%m-%d %H:%M:%S') if hasattr(fc, 'time_created') and fc.time_created else 'N/A'
                    }
                    
                    # Crear tabla de detalles
                    details_df = pd.DataFrame([vc_details]).T
                    details_df.columns = ['Valor']
                    f.write(tabulate(details_df, headers='keys', tablefmt='pipe', showindex=True) + "\n\n")
                    
                    # Buscar Cross-Connects asociados (si existe la relación)
                    # Nota: La relación entre Cross-Connects y Virtual Circuits puede ser compleja en OCI
                    associated_ccs = []
                    for cc in region_resources.get('cross_connects', []):
                        # Intentar diferentes formas de asociación si existen
                        if hasattr(cc, 'virtual_circuit_id') and cc.virtual_circuit_id == fc.id:
                            associated_ccs.append(cc)
                        elif hasattr(cc, 'gateway_id') and cc.gateway_id == fc.gateway_id:
                            associated_ccs.append(cc)
                        elif hasattr(cc, 'cross_connect_group_id') and any(ccg.id == cc.cross_connect_group_id for ccg in region_resources.get('cross_connect_groups', [])):
                            # Si están en el mismo grupo, considerarlos potencialmente relacionados
                            associated_ccs.append(cc)
                    
                    if associated_ccs:
                        f.write("**Cross-Connects Potencialmente Asociados:**\n\n")
                        cc_details = []
                        for cc in associated_ccs:
                            cc_details.append({
                                'ID': cc.id,
                                'Nombre': cc.display_name,
                                'Estado': cc.lifecycle_state,
                                'Tipo': cc.port_speed_shape_name,
                                'Grupo': cc.cross_connect_group_id if hasattr(cc, 'cross_connect_group_id') else 'N/A'
                            })
                        
                        cc_df = pd.DataFrame(cc_details)
                        f.write(tabulate(cc_df, headers='keys', tablefmt='pipe', showindex=False) + "\n\n")
                    else:
                        f.write("No se encontraron Cross-Connects claramente asociados a este Virtual Circuit.\n\n")
                        f.write("*Nota: Los Cross-Connects pueden estar asociados indirectamente a través de grupos o DRGs.*\n\n")
            else:
                f.write("No se encontraron conexiones FastConnect en esta región.\n\n")


def generate_network_diagram(resources, output_file):
    """
    Genera un diagrama de red utilizando GraphViz/DOT.
    
    Args:
        resources (dict): Diccionario con todos los recursos de red por región.
        output_file (Path): Ruta base del archivo de salida (sin extensión).
    """
    # Crear archivo DOT
    dot_file = f"{output_file}.dot"
    
    with open(dot_file, 'w') as f:
        f.write("digraph OCI_Network {\n")
        f.write("  graph [layout=dot, rankdir=TB, splines=ortho, nodesep=1.5, ranksep=2.0, bgcolor=\"#fcfcfc\"];\n")
        f.write("  node [shape=box, style=filled, fillcolor=white, color=\"#34495e\", fontname=\"Helvetica\", fontsize=8, width=2.5, height=1.2];\n")
        f.write("  edge [color=\"#7f8c8d\", penwidth=1.0, arrowsize=0.6];\n\n")
        f.write("  newrank=true;\n")
        
        # Crear un subgrafo para cada región
        for region, region_resources in resources.items():
            f.write(f"  subgraph cluster_{region.replace('-', '_')} {{\n")
            f.write(f"    label=\"Región: {region}\";\n")
            f.write("    style=filled;\n")
            f.write("    color=lightgrey;\n")
            f.write("    node [style=filled, fillcolor=white];\n\n")
            
            # Crear nodos para VCNs
            for vcn in region_resources['vcns']:
                vcn_id = vcn.id.replace('.', '_').replace(':', '_').replace('-', '_')
                f.write(f"    vcn_{vcn_id} [label=\"VCN: {vcn.display_name}\\nCIDR: {vcn.cidr_block}\", shape=polygon, sides=6, peripheries=1, style=\"filled,bold\", fillcolor=\"#e8f4fd\", color=\"#2980b9\"];\n")
                
                # Crear nodos para subnets y conectarlos a la VCN
                for subnet in [s for s in region_resources['subnets'] if s.vcn_id == vcn.id]:
                    subnet_id = subnet.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    public_private = "Pública" if subnet.prohibit_public_ip_on_vnic == False else "Privada"
                    f.write(f"    subnet_{subnet_id} [label=\"Subnet: {subnet.display_name}\\nCIDR: {subnet.cidr_block}\\n{public_private}\", fillcolor=lightyellow];\n")
                    f.write(f"    vcn_{vcn_id} -> subnet_{subnet_id};\n")
                
                # Crear nodos para tablas de rutas y conectarlos a la VCN
                for rt in [rt for rt in region_resources['route_tables'] if rt.vcn_id == vcn.id]:
                    rt_id = rt.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    
                    # Preparar información de reglas para mostrar en el diagrama
                    route_rules_info = []
                    if rt.route_rules:
                        # Limitar a máximo 5 reglas para no sobrecargar el diagrama
                        for i, rule in enumerate(rt.route_rules[:5]):
                            # Determinar tipo de entidad
                            entity_type = "Desconocido"
                            if any(igw.id == rule.network_entity_id for igw in region_resources['internet_gateways']):
                                entity_type = "IGW"
                            elif any(nat.id == rule.network_entity_id for nat in region_resources['nat_gateways']):
                                entity_type = "NAT"
                            elif any(sgw.id == rule.network_entity_id for sgw in region_resources['service_gateways']):
                                entity_type = "SGW"
                            elif any(drg_attachment.drg_id == rule.network_entity_id for drg_attachment in region_resources['drg_attachments']):
                                entity_type = "DRG"
                            
                            route_rules_info.append(f"{rule.destination} → {entity_type}")
                        
                        # Indicar si hay más reglas que no se muestran
                        if len(rt.route_rules) > 5:
                            route_rules_info.append(f"... y {len(rt.route_rules) - 5} reglas más")
                    else:
                        route_rules_info.append("Sin reglas definidas")
                    
                    # Crear el nodo con la información de las reglas
                    rules_label = "\\n".join(route_rules_info)
                    f.write(f"    rt_{rt_id} [label=\"RT: {rt.display_name}\\n{rules_label}\", shape=folder, style=filled, fillcolor=\"#e6f7ff\", color=\"#5dade2\"];\n")
                    f.write(f"    rt_{rt_id} -> vcn_{vcn_id};\n")
                    
                    # Conectar la tabla de rutas con las subnets que la utilizan
                    for subnet in [s for s in region_resources['subnets'] if s.vcn_id == vcn.id and s.route_table_id == rt.id]:
                        subnet_id = subnet.id.replace('.', '_').replace(':', '_').replace('-', '_')
                        f.write(f"    rt_{rt_id} -> subnet_{subnet_id} [style=dotted, color=blue];\n")
                
                # Crear nodos para Internet Gateways y conectarlos a la VCN
                for igw in [g for g in region_resources['internet_gateways'] if g.vcn_id == vcn.id]:
                    igw_id = igw.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    f.write(f"    igw_{igw_id} [label=\"IGW: {igw.display_name}\", shape=pentagon, style=filled, fillcolor=\"#d4efdf\", color=\"#27ae60\"];\n")
                    f.write(f"    igw_{igw_id} -> vcn_{vcn_id};\n")
                
                # Crear nodos para NAT Gateways y conectarlos a la VCN
                for nat in [n for n in region_resources['nat_gateways'] if n.vcn_id == vcn.id]:
                    nat_id = nat.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    f.write(f"    nat_{nat_id} [label=\"NAT GW: {nat.display_name}\\nIP: {nat.nat_ip}\", shape=pentagon, style=filled, fillcolor=\"#fcf3cf\", color=\"#b7950b\"];\n")
                    f.write(f"    nat_{nat_id} -> vcn_{vcn_id};\n")
                
                # Crear nodos para Service Gateways y conectarlos a la VCN
                for sgw in [s for s in region_resources['service_gateways'] if s.vcn_id == vcn.id]:
                    sgw_id = sgw.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    services = [service.service_name for service in sgw.services] if sgw.services else []
                    service_label = "\\n".join(services) if services else "No services"
                    f.write(f"    sgw_{sgw_id} [label=\"SGW: {sgw.display_name}\\n{service_label}\", shape=pentagon, style=filled, fillcolor=\"#f6ddcc\", color=\"#d35400\"];\n")
                    f.write(f"    sgw_{sgw_id} -> vcn_{vcn_id};\n")
            
            # Fin del bucle de VCNs
            
            # Crear un subgrafo para los DRGs en el centro
            f.write(f"    subgraph cluster_drgs_{region.replace('-', '_')} {{\n")
            f.write(f"      label=\"DRGs de la región {region}\";\n")
            f.write("      style=filled;\n")
            f.write("      color=lightsalmon;\n")
            f.write("      rank=source;\n")
            
            # Crear nodos para DRGs
            for drg in region_resources['drgs']:
                drg_id = drg.id.replace('.', '_').replace(':', '_').replace('-', '_')
                
                # Contar tablas de rutas y distribuciones para este DRG
                rt_count = len([rt for rt in region_resources.get('drg_route_tables', []) if rt.drg_id == drg.id])
                dist_count = len([dist for dist in region_resources.get('drg_route_distributions', []) if dist.drg_id == drg.id])
                
                # Añadir información de tablas de rutas y distribuciones al label
                label = f"DRG: {drg.display_name}\nRoute Tables: {rt_count}\nDistributions: {dist_count}"
                
                f.write(f"      drg_{drg_id} [label=\"{label}\", shape=circle, width=1.2, height=1.2, style=\"filled,bold\", fillcolor=\"#ffe0b2\", color=\"#ef6c00\", penwidth=2];\n")
                    
                # Crear nodos para las tablas de rutas de DRG
                for drg_rt in [rt for rt in region_resources.get('drg_route_tables', []) if rt.drg_id == drg.id]:
                    drg_rt_id = drg_rt.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    
                    # Obtener información de las reglas de la tabla de rutas DRG
                    rules_info = []
                    if hasattr(drg_rt, 'route_rules') and drg_rt.route_rules:
                        # Limitar a máximo 5 reglas para no sobrecargar el diagrama
                        for i, rule in enumerate(drg_rt.route_rules[:5]):
                            destination = rule.destination if hasattr(rule, 'destination') else 'Desconocido'
                            next_hop_drg_attachment_id = rule.next_hop_drg_attachment_id if hasattr(rule, 'next_hop_drg_attachment_id') else 'Desconocido'
                            
                            # Intentar obtener el nombre del attachment
                            attachment_name = "Desconocido"
                            for attachment in region_resources['drg_attachments']:
                                if attachment.id == next_hop_drg_attachment_id:
                                    attachment_name = attachment.display_name
                                    break
                            
                            rules_info.append(f"{destination} → {attachment_name}")
                        
                        # Indicar si hay más reglas que no se muestran
                        if len(drg_rt.route_rules) > 5:
                            rules_info.append(f"... y {len(drg_rt.route_rules) - 5} reglas más")
                    else:
                        rules_info.append("Sin reglas definidas")
                    
                    # Crear el nodo con la información de las reglas
                    rules_label = "\\n".join(rules_info)
                    import_distribution = drg_rt.import_drg_route_distribution_id if hasattr(drg_rt, 'import_drg_route_distribution_id') else 'Ninguna'
                    
                    # Obtener el nombre de la distribución de importación
                    import_dist_name = "Ninguna"
                    if import_distribution != 'Ninguna':
                        for dist in region_resources.get('drg_route_distributions', []):
                            if dist.id == import_distribution:
                                import_dist_name = dist.display_name
                                break
                    
                    label = f"DRG RT: {drg_rt.display_name}\nImport: {import_dist_name}\n{rules_label}"
                    f.write(f"      drg_rt_{drg_rt_id} [label=\"{label}\", shape=folder, style=filled, fillcolor=\"#ffe6e6\", color=\"#c0392b\"];\n")
                    f.write(f"      drg_rt_{drg_rt_id} -> drg_{drg_id};\n")
                    
                # Crear nodos para las distribuciones de rutas de DRG
                for drg_dist in [dist for dist in region_resources.get('drg_route_distributions', []) if dist.drg_id == drg.id]:
                    drg_dist_id = drg_dist.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    
                    # Obtener información de las declaraciones de la distribución
                    statements_info = []
                    if hasattr(drg_dist, 'statements') and drg_dist.statements:
                        # Limitar a máximo 5 declaraciones para no sobrecargar el diagrama
                        for i, stmt in enumerate(drg_dist.statements[:5]):
                            # Obtener el tipo de match si existe
                            match_type = "Desconocido"
                            if hasattr(stmt, 'match_criteria') and stmt.match_criteria:
                                if hasattr(stmt.match_criteria, 'match_type'):
                                    match_type = stmt.match_criteria.match_type
                                elif hasattr(stmt.match_criteria, 'attachment_type'):
                                    match_type = stmt.match_criteria.attachment_type
                            
                            # Obtener el nombre del attachment si existe
                            attachment_name = "Todos"
                            if hasattr(stmt, 'match_criteria') and stmt.match_criteria:
                                if hasattr(stmt.match_criteria, 'drg_attachment_id') and stmt.match_criteria.drg_attachment_id:
                                    for attachment in region_resources['drg_attachments']:
                                        if attachment.id == stmt.match_criteria.drg_attachment_id:
                                            attachment_name = attachment.display_name
                                            break
                            
                            priority = stmt.priority if hasattr(stmt, 'priority') else "N/A"
                            statements_info.append(f"P{priority}: {match_type} → {attachment_name}")
                        
                        # Indicar si hay más declaraciones que no se muestran
                        if len(drg_dist.statements) > 5:
                            statements_info.append(f"... y {len(drg_dist.statements) - 5} más")
                    else:
                        statements_info.append("Sin declaraciones")
                    
                    # Crear el nodo con la información de las declaraciones
                    statements_label = "\\n".join(statements_info)
                    dist_type = drg_dist.distribution_type if hasattr(drg_dist, 'distribution_type') else "Desconocido"
                    
                    label = f"DRG Dist: {drg_dist.display_name}\nTipo: {dist_type}\n{statements_label}"
                    f.write(f"      drg_dist_{drg_dist_id} [label=\"{label}\", shape=note, style=filled, fillcolor=\"#f9e79f\", color=\"#b9770e\"];\n")
                    f.write(f"      drg_dist_{drg_dist_id} -> drg_{drg_id};\n")
                    
                    # Conectar distribuciones con las tablas de rutas que las importan
                    for rt in [rt for rt in region_resources.get('drg_route_tables', []) if rt.drg_id == drg.id]:
                        if hasattr(rt, 'import_drg_route_distribution_id') and rt.import_drg_route_distribution_id == drg_dist.id:
                            rt_id = rt.id.replace('.', '_').replace(':', '_').replace('-', '_')
                            f.write(f"      drg_dist_{drg_dist_id} -> drg_rt_{rt_id} [style=dashed, color=red, label=\"import\"];\n")
                
                # Conectar DRG a VCNs a través de attachments (conexiones simples)
                attachments = [a for a in region_resources['drg_attachments'] if a.drg_id == drg.id and getattr(a, 'vcn_id', None)]
                for att in attachments:
                    vcn_node_id = att.vcn_id.replace('.', '_').replace(':', '_').replace('-', '_')
                    f.write(f"      drg_{drg_id} -> vcn_{vcn_node_id} [dir=both, penwidth=1.5, color=\"#34495e\"];\n")

            # Cerrar el subgrafo de DRGs
            f.write("    }\n\n")
            
            # Conexiones DRG↔VCN dibujadas dentro del subgrafo con posiciones fijas
                
            # Crear nodos para Remote Peering Connections y conectarlos al DRG
            for drg in region_resources['drgs']:
                drg_id = drg.id.replace('.', '_').replace(':', '_').replace('-', '_')
                for rpc in [r for r in region_resources['remote_peering_connections'] if r.drg_id == drg.id]:
                    rpc_id = rpc.id.replace('.', '_').replace(':', '_').replace('-', '_')
                    peer_region = rpc.peer_region_name or "No conectado"
                    f.write(f"    rpc_{rpc_id} [label=\"RPC: {rpc.display_name}\\nPeer Region: {peer_region}\", shape=diamond, style=filled, fillcolor=\"#f5b7b1\", color=\"#943126\"];\n")
                    f.write(f"    drg_{drg_id} -> rpc_{rpc_id} [constraint=false];\n")
            
            # Crear nodos para VPN Connections
            for vpn in region_resources['vpn_connections']:
                vpn_id = vpn.id.replace('.', '_').replace(':', '_').replace('-', '_')
                drg_id = vpn.drg_id.replace('.', '_').replace(':', '_').replace('-', '_')
                f.write(f"    vpn_{vpn_id} [label=\"VPN: {vpn.display_name}\", shape=trapezium, style=filled, fillcolor=\"#f9ebea\", color=\"#c0392b\"];\n")
                f.write(f"    vpn_{vpn_id} -> drg_{drg_id} [dir=both, constraint=false];\n")
            
            # Crear nodos para FastConnect
            for fc in region_resources['fastconnect_connections']:
                fc_id = fc.id.replace('.', '_').replace(':', '_').replace('-', '_')
                drg_id = fc.gateway_id.replace('.', '_').replace(':', '_').replace('-', '_')
                f.write(f"    fc_{fc_id} [label=\"FastConnect: {fc.display_name}\\nBandwidth: {fc.bandwidth_shape_name}\", shape=cylinder, style=filled, fillcolor=\"#fdebd0\", color=\"#d35400\"];\n")
                f.write(f"    fc_{fc_id} -> drg_{drg_id} [dir=both, constraint=false];\n")
            
            f.write("  }\n\n")
        
        # Conectar Remote Peering Connections entre regiones
        for region1, resources1 in resources.items():
            for rpc1 in resources1['remote_peering_connections']:
                if rpc1.peer_id and rpc1.peer_region_name:
                    for region2, resources2 in resources.items():
                        if region2 == rpc1.peer_region_name:
                            for rpc2 in resources2['remote_peering_connections']:
                                if rpc2.id == rpc1.peer_id:
                                    rpc1_id = rpc1.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                    rpc2_id = rpc2.id.replace('.', '_').replace(':', '_').replace('-', '_')
                                    f.write(f"  rpc_{rpc1_id} -> rpc_{rpc2_id} [dir=both, style=dashed, color=red, constraint=false];\n")
        
        # Leyenda compacta en la esquina
        f.write("  subgraph cluster_legend {\n")
        f.write("    label=\"Leyenda\"; color=lightgrey; style=dashed; rank=sink;\n")
        f.write("    legend_vcn   [label=\"VCN\", shape=polygon, sides=6, style=filled, fillcolor=\"#e8f4fd\", color=\"#2980b9\", width=1.0, height=0.8];\n")
        f.write("    legend_sub   [label=\"Subnet\", shape=box, style=filled, fillcolor=\"#fffde7\", width=1.0, height=0.8];\n")
        f.write("    legend_drg   [label=\"DRG\", shape=circle, width=0.8, height=0.8, style=filled, fillcolor=\"#ffe0b2\", color=\"#ef6c00\"];\n")
        f.write("    legend_rt    [label=\"Route Table\", shape=folder, style=filled, fillcolor=\"#e6f7ff\", width=1.0, height=0.8];\n")
        f.write("    legend_igw   [label=\"Gateway\", shape=pentagon, style=filled, fillcolor=\"#d4efdf\", width=1.0, height=0.8];\n")
        f.write("    legend_rpc   [label=\"RPC/VPN/FC\", shape=diamond, style=filled, fillcolor=\"#f5b7b1\", width=1.0, height=0.8];\n")
        f.write("  }\n")

        f.write("}\n")
    
    # Generar imagen PNG a partir del archivo DOT
    try:
        subprocess.run(['dot', '-Tpng', dot_file, '-o', f"{output_file}.png"], check=True)
        print(f"Diagrama de red generado en: {output_file}.png")
    except Exception as e:
        print(f"Error al generar el diagrama de red: {str(e)}")
        print("Asegúrese de tener GraphViz instalado (https://graphviz.org/)")
        print(f"El archivo DOT se ha guardado en: {dot_file}")