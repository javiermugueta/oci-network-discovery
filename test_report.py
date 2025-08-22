#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de prueba para verificar que los diagramas de red de dos niveles
se generen correctamente: top-level DRG topology y per-VCN gateway connections.
"""

from modules.network_diagrams import generate_top_level_diagram, generate_vcn_gateway_diagram
from pathlib import Path

# Datos de ejemplo para probar los diagramas de dos niveles
sample_resources = {
    'eu-madrid-1': {
        'vcns': [
            type('VCN', (), {
                'id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'display_name': 'test-vcn-pro',
                'cidr_block': '10.0.0.0/16',
                'lifecycle_state': 'AVAILABLE',
                'compartment_id': 'ocid1.compartment.oc1..aaaaaaaacomp1'
            })(),
            type('VCN', (), {
                'id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaayyy',
                'display_name': 'test-vcn-pre',
                'cidr_block': '10.1.0.0/16',
                'lifecycle_state': 'AVAILABLE',
                'compartment_id': 'ocid1.compartment.oc1..aaaaaaaacomp2'
            })()
        ],
        'subnets': [],
        'route_tables': [],
        'security_lists': [],
        'internet_gateways': [
            type('InternetGateway', (), {
                'id': 'ocid1.internetgateway.oc1.eu-madrid-1.aaaaaaaigw1',
                'display_name': 'Internet Gateway for test-vcn-pro',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'is_enabled': True,
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'nat_gateways': [
            type('NatGateway', (), {
                'id': 'ocid1.natgateway.oc1.eu-madrid-1.aaaaaaanat1',
                'display_name': 'NAT Gateway for test-vcn-pro',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'service_gateways': [
            type('ServiceGateway', (), {
                'id': 'ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaasgw1',
                'display_name': 'Service Gateway for test-vcn-pro',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'drgs': [
            type('Drg', (), {
                'id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'display_name': 'test-drg',
                'compartment_id': 'ocid1.compartment.oc1..aaaaaaaacomp3',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'drg_attachments': [
            type('DrgAttachment', (), {
                'id': 'ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaadra1',
                'display_name': 'DRG Attachment for test-vcn-pro',
                'drg_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'lifecycle_state': 'AVAILABLE'
            })(),
            type('DrgAttachment', (), {
                'id': 'ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaadra2',
                'display_name': 'DRG Attachment for test-vcn-pre',
                'drg_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaayyy',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'remote_peering_connections': [
            type('RemotePeeringConnection', (), {
                'id': 'ocid1.remotepeeringconnection.oc1.eu-madrid-1.aaaaaaaarpc1',
                'display_name': 'RPC-Production',
                'drg_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'vpn_connections': [
            type('IPSecConnection', (), {
                'id': 'ocid1.ipsecconnection.oc1.eu-madrid-1.aaaaaaaavpn1',
                'display_name': 'VPN-Production',
                'drg_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'vpn_tunnels': [],
        'fastconnect_connections': [
            type('VirtualCircuit', (), {
                'id': 'ocid1.virtualcircuit.oc1.eu-madrid-1.aaaaaaaafc1',
                'display_name': 'FastConnect-Production',
                'gateway_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'cross_connect_groups': [],
        'cross_connects': [],
        'drg_route_tables': [],
        'drg_route_distributions': []
    }
}

if __name__ == "__main__":
    print("🚀 Generando diagramas de red de dos niveles...")
    print("📋 Este test verifica:")
    print("  - Diagrama de primer nivel: DRGs y sus conexiones")
    print("  - Diagrama por VCN: Gateways y conexiones")
    print("  - Formato DOT y Draw.io para ambos diagramas")
    
    # Crear directorio de salida
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    
    # Generar diagramas
    base_file = output_dir / "test_network_diagrams"
    
    print("\n🔧 Generando diagrama de primer nivel...")
    top_level_dot = generate_top_level_diagram(sample_resources, base_file, "dot")
    top_level_drawio = generate_top_level_diagram(sample_resources, base_file, "drawio")
    
    print("🔧 Generando diagrama por VCN...")
    vcn_gateway_dot = generate_vcn_gateway_diagram(sample_resources, base_file, "dot")
    vcn_gateway_drawio = generate_vcn_gateway_diagram(sample_resources, base_file, "drawio")
    
    print(f"\n✅ Diagramas generados:")
    print(f"  - Top Level DOT: {top_level_dot}")
    print(f"  - Top Level Draw.io: {top_level_drawio}")
    print(f"  - VCN Gateway DOT: {vcn_gateway_dot}")
    print(f"  - VCN Gateway Draw.io: {vcn_gateway_drawio}")
    
    print("\n🔍 Verifica que:")
    print("  - Los archivos DOT se generen correctamente")
    print("  - Los archivos Draw.io se generen correctamente")
    print("  - Los diagramas muestren DRGs, VCNs, gateways y conexiones")
    print("  - La estructura de los diagramas sea clara y legible")
    print("\n💡 Estos diagramas muestran la topología de red en dos niveles de detalle")
