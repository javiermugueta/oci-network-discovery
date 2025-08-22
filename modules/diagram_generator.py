#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo para generar diagramas de red OCI en formato Draw.io
basado en los datos descubiertos por oci_network_discovery.py
"""

import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path


class SimpleWorkingDiagramGenerator:
    """Generador simple y funcional de diagramas Draw.io"""
    
    def __init__(self):
        self.cell_id_counter = 2  # Empezar después de las celdas del sistema (0, 1)
        self.edge_id_counter = 1000  # Empezar en 1000 para evitar conflictos
        
    def generate_simple_diagram(self, all_resources, output_file):
        """Genera un diagrama simple que funciona"""
        
        # Crear contenido XML manualmente para evitar problemas
        xml_content = self._create_xml_content(all_resources)
        
        # Escribir archivo
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
            f.write('\n')  # Añadir newline al final
        
        print(f"Diagrama simple generado en: {output_file}")
        
    def _create_xml_content(self, all_resources):
        """Crea el contenido XML completo"""
        
        # Crear encabezado
        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            f'<mxfile host="app.diagrams.net" modified="{datetime.now().isoformat()}" agent="OCI Network Discovery Tool" etag="simple-generated" version="24.6.4" type="device">',
            '  <diagram name="OCI Network Infrastructure" id="oci-network">',
            '    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">',
            '      <root>',
            '        <mxCell id="0" />',
            '        <mxCell id="1" parent="0" />'
        ]
        
        # Añadir DRG central
        for region, region_resources in all_resources.items():
            if region_resources.get('drgs'):
                drg = region_resources['drgs'][0]
                drg_cell = f'        <mxCell id="{self.cell_id_counter}" value="&lt;div style=&quot;font-size: 16px; text-align: center;&quot;&gt;&lt;b&gt;{drg.display_name}&lt;/b&gt;&lt;br/&gt;DRG Central&lt;br/&gt;ID: {drg.id[:20]}...&lt;/div&gt;" style="rounded=0;whiteSpace=wrap;html=1;strokeWidth=10;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14" vertex="1" parent="1">'
                drg_geometry = f'          <mxGeometry x="1200" y="1000" width="300" height="200" as="geometry" />'
                drg_end = '        </mxCell>'
                
                xml_lines.extend([drg_cell, drg_geometry, drg_end])
                drg_id = self.cell_id_counter
                self.cell_id_counter += 1
                
                # Añadir VCNs conectadas
                if region_resources.get('drg_attachments'):
                    vcn_positions = [(800, 800), (1600, 800), (800, 1200), (1600, 1200)]
                    
                    for i, attachment in enumerate(region_resources.get('drg_attachments', [])[:4]):
                        if attachment.vcn_id:
                            vcn = next((v for v in region_resources['vcns'] if v.id == attachment.vcn_id), None)
                            if vcn and i < len(vcn_positions):
                                x, y = vcn_positions[i]
                                
                                vcn_cell = f'        <mxCell id="{self.cell_id_counter}" value="&lt;div style=&quot;text-align: center;&quot;&gt;&lt;b&gt;{vcn.display_name}&lt;/b&gt;&lt;br/&gt;CIDR: {vcn.cidr_block}&lt;br/&gt;Compartment: {vcn.compartment_id[:20]}...&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;strokeWidth=2" vertex="1" parent="1">'
                                vcn_geometry = f'          <mxGeometry x="{x}" y="{y}" width="200" height="80" as="geometry" />'
                                vcn_end = '        </mxCell>'
                                
                                xml_lines.extend([vcn_cell, vcn_geometry, vcn_end])
                                vcn_id = self.cell_id_counter
                                self.cell_id_counter += 1
                                
                                # Añadir conexión
                                connection = f'        <mxCell id="{self.edge_id_counter}" style="rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;strokeWidth=3;strokeColor=#666666" edge="1" parent="1" source="{vcn_id}" target="{drg_id}">'
                                connection_label = f'          <mxCell id="{self.edge_id_counter + 1000}" value="{attachment.display_name}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#666666" vertex="1" connectable="0" parent="{self.edge_id_counter}">'
                                label_geometry = '            <mxGeometry x="0.5" y="-0.5" relative="1" as="geometry" />'
                                label_end = '          </mxCell>'
                                connection_end = '        </mxCell>'
                                
                                xml_lines.extend([connection, connection_label, label_geometry, label_end, connection_end])
                                self.edge_id_counter += 1
                
                # Añadir VPNs si existen
                if region_resources.get('vpn_connections'):
                    vpn_y_offset = 2200
                    for i, vpn in enumerate(region_resources.get('vpn_connections', [])[:2]):
                        vpn_cell = f'        <mxCell id="{self.cell_id_counter}" value="&lt;div style=&quot;text-align: center;&quot;&gt;&lt;b&gt;VPN: {vpn.display_name}&lt;/b&gt;&lt;br/&gt;DRG: {vpn.drg_id[:20]}...&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=12;strokeWidth=3" vertex="1" parent="1">'
                        vpn_geometry = f'          <mxGeometry x="50" y="{vpn_y_offset + (i * 100)}" width="250" height="80" as="geometry" />'
                        vpn_end = '        </mxCell>'
                        
                        xml_lines.extend([vpn_cell, vpn_geometry, vpn_end])
                        self.cell_id_counter += 1
                
                # Añadir FastConnect si existe
                if region_resources.get('fastconnect_connections'):
                    fc_y_offset = 2400
                    for i, fc in enumerate(region_resources.get('fastconnect_connections', [])[:2]):
                        fc_cell = f'        <mxCell id="{self.cell_id_counter}" value="&lt;div style=&quot;text-align: center;&quot;&gt;&lt;b&gt;FastConnect: {fc.display_name}&lt;/b&gt;&lt;br/&gt;BW: {fc.bandwidth_shape_name}&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;strokeWidth=3" vertex="1" parent="1">'
                        fc_geometry = f'          <mxGeometry x="350" y="{fc_y_offset + (i * 100)}" width="250" height="80" as="geometry" />'
                        fc_end = '        </mxCell>'
                        
                        xml_lines.extend([fc_cell, fc_geometry, fc_end])
                        self.cell_id_counter += 1
                
                break  # Solo procesar la primera región por ahora
        
        # Cerrar XML
        xml_lines.extend([
            '      </root>',
            '    </mxGraphModel>',
            '  </diagram>',
            '</mxfile>'
        ])
        
        return '\n'.join(xml_lines)


def generate_oci_network_diagram(all_resources, output_file):
    """
    Función principal para generar diagrama de red OCI básico
    
    Args:
        all_resources (dict): Recursos descubiertos por región
        output_file (Path): Archivo de salida
    """
    generator = SimpleWorkingDiagramGenerator()
    generator.generate_simple_diagram(all_resources, output_file)
    print(f"Diagrama Draw.io básico generado en: {output_file}")


def generate_advanced_oci_network_diagram(all_resources, output_file):
    """
    Función para generar diagrama avanzado similar a ejemplo.drawio
    
    Args:
        all_resources (dict): Recursos descubiertos por región
        output_file (Path): Archivo de salida
    """
    generator = SimpleWorkingDiagramGenerator()
    generator.generate_simple_diagram(all_resources, output_file)
    print(f"Diagrama Draw.io avanzado generado en: {output_file}")


def generate_compatible_oci_network_diagram(all_resources, output_file):
    """
    Función para generar diagrama compatible con todas las versiones de draw.io
    
    Args:
        all_resources (dict): Recursos descubiertos por región
        output_file (Path): Archivo de salida
    """
    generator = SimpleWorkingDiagramGenerator()
    generator.generate_simple_diagram(all_resources, output_file)
    print(f"Diagrama Draw.io compatible generado en: {output_file}")
