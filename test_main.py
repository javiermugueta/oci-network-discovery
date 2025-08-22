#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de prueba que simula el script principal para verificar que todos los diagramas se generen.
"""

from modules.report import generate_markdown_report, generate_network_diagram
from modules.diagram_generator import generate_hub_spoke_diagram
from modules.network_diagrams import generate_top_level_diagram, generate_vcn_gateway_diagram
from pathlib import Path
from datetime import datetime

# Datos de ejemplo más completos
sample_resources = {
    'eu-madrid-1': {
        'vcns': [
            type('VCN', (), {
                'id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'display_name': 'vcn-prod',
                'cidr_block': '10.0.0.0/16',
                'lifecycle_state': 'AVAILABLE',
                'compartment_id': 'ocid1.compartment.oc1..aaaaaaaacomp1'
            })(),
            type('VCN', (), {
                'id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaayyy',
                'display_name': 'vcn-pre',
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
                'display_name': 'IGW-Prod',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'is_enabled': True,
                'lifecycle_state': 'AVAILABLE'
            })(),
            type('InternetGateway', (), {
                'id': 'ocid1.internetgateway.oc1.eu-madrid-1.aaaaaaaigw2',
                'display_name': 'IGW-Pre',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaayyy',
                'is_enabled': True,
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'nat_gateways': [
            type('NatGateway', (), {
                'id': 'ocid1.natgateway.oc1.eu-madrid-1.aaaaaaanat1',
                'display_name': 'NAT-Prod',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'lifecycle_state': 'AVAILABLE',
                'nat_ip': '192.168.1.1',
                'block_traffic': False
            })()
        ],
        'service_gateways': [
            type('ServiceGateway', (), {
                'id': 'ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaasgw1',
                'display_name': 'SGW-Prod',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'lifecycle_state': 'AVAILABLE',
                'services': [
                    type('ServiceGatewayService', (), {
                        'service_name': 'OCI Object Storage'
                    })()
                ]
            })()
        ],
        'drgs': [
            type('Drg', (), {
                'id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'display_name': 'DRG-Hub',
                'compartment_id': 'ocid1.compartment.oc1..aaaaaaaacomp3',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'drg_attachments': [
            type('DrgAttachment', (), {
                'id': 'ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaadra1',
                'display_name': 'DRA-Prod',
                'drg_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaaxxx',
                'lifecycle_state': 'AVAILABLE'
            })(),
            type('DrgAttachment', (), {
                'id': 'ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaadra2',
                'display_name': 'DRA-Pre',
                'drg_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'vcn_id': 'ocid1.vcn.oc1.eu-madrid-1.aaaaaaaayyy',
                'lifecycle_state': 'AVAILABLE'
            })()
        ],
        'remote_peering_connections': [
            type('RemotePeeringConnection', (), {
                'id': 'ocid1.remotepeeringconnection.oc1.eu-madrid-1.aaaaaaaarpc1',
                'display_name': 'RPC-Prod',
                'drg_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'lifecycle_state': 'AVAILABLE',
                'peer_region_name': 'eu-frankfurt-1',
                'peer_id': 'ocid1.remotepeeringconnection.oc1.eu-frankfurt-1.aaaaaaaarpc2',
                'peering_status': 'PEERED'
            })()
        ],
        'vpn_connections': [
            type('IPSecConnection', (), {
                'id': 'ocid1.ipsecconnection.oc1.eu-madrid-1.aaaaaaaavpn1',
                'display_name': 'VPN-Prod',
                'drg_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'lifecycle_state': 'AVAILABLE',
                'cpe_id': 'ocid1.cpe.oc1.eu-madrid-1.aaaaaaaacpe1',
                'cpe_local_identifier': '203.0.113.1',
                'cpe_local_identifier_type': 'IP_ADDRESS'
            })()
        ],
        'vpn_tunnels': [],
        'fastconnect_connections': [
            type('VirtualCircuit', (), {
                'id': 'ocid1.virtualcircuit.oc1.eu-madrid-1.aaaaaaaafc1',
                'display_name': 'FC-Prod',
                'gateway_id': 'ocid1.drg.oc1.eu-madrid-1.aaaaaaaadrg1',
                'lifecycle_state': 'AVAILABLE',
                'type': 'PRIVATE',
                'bandwidth_shape_name': '10 Gbps',
                'provider_name': 'Equinix',
                'compartment_id': 'ocid1.compartment.oc1..aaaaaaaacomp1'
            })()
        ],
        'cross_connect_groups': [],
        'cross_connects': [],
        'drg_route_tables': [],
        'drg_route_distributions': []
    }
}

if __name__ == "__main__":
    print("🚀 Simulando script principal de descubrimiento de red...")
    print("📋 Este test verifica que se generen TODOS los diagramas:")
    print("  - Diagrama tradicional de red")
    print("  - Diagrama hub-and-spoke profesional")
    print("  - Diagrama de primer nivel (DRG topology)")
    print("  - Diagrama por VCN (gateways y conexiones)")
    print("  - Todos en formato DOT y Draw.io")
    
    # Crear directorio de salida
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    
    # Simular timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print(f"\n🔧 Generando reporte Markdown...")
    markdown_file = output_dir / f"oci_network_report_{timestamp}.md"
    generate_markdown_report(sample_resources, markdown_file)
    
    print(f"🔧 Generando diagrama tradicional...")
    diagram_file = output_dir / f"oci_network_diagram_{timestamp}"
    generate_network_diagram(sample_resources, diagram_file)
    
    print(f"🔧 Generando diagrama hub-and-spoke...")
    hub_spoke_file = output_dir / f"oci_network_hub_spoke_{timestamp}"
    generate_hub_spoke_diagram(sample_resources, hub_spoke_file, "dot")
    generate_hub_spoke_diagram(sample_resources, hub_spoke_file, "drawio")
    
    print(f"🔧 Generando diagrama de primer nivel...")
    top_level_file = output_dir / f"oci_network_top_level_{timestamp}"
    generate_top_level_diagram(sample_resources, top_level_file, "dot")
    generate_top_level_diagram(sample_resources, top_level_file, "drawio")
    
    print(f"🔧 Generando diagrama por VCN...")
    vcn_gateway_file = output_dir / f"oci_network_vcn_gateways_{timestamp}"
    generate_vcn_gateway_diagram(sample_resources, vcn_gateway_file, "dot")
    generate_vcn_gateway_diagram(sample_resources, vcn_gateway_file, "drawio")
    
    print(f"\n✅ Archivos generados:")
    print(f"  - Markdown: {markdown_file}")
    print(f"  - Diagrama tradicional: {diagram_file}.png")
    print(f"  - Hub-and-spoke DOT: {hub_spoke_file}.dot")
    print(f"  - Hub-and-spoke Draw.io: {hub_spoke_file}.drawio")
    print(f"  - Top Level DOT: {top_level_file}_top_level.dot")
    print(f"  - Top Level Draw.io: {top_level_file}_top_level.drawio")
    print(f"  - VCN Gateway DOT: {vcn_gateway_file}_vcn_gateways.dot")
    print(f"  - VCN Gateway Draw.io: {vcn_gateway_file}_vcn_gateways.drawio")
    
    print(f"\n🔍 Verifica que:")
    print(f"  - Se generen TODOS los archivos")
    print(f"  - Los diagramas DOT tengan contenido válido")
    print(f"  - Los archivos Draw.io se puedan abrir")
    print(f"  - No haya errores durante la generación")
    
    print(f"\n💡 Si todo funciona, significa que el script principal generará todos los diagramas correctamente")
