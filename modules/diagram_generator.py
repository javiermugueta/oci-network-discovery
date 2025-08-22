#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo para generar diagramas de red OCI en formato Draw.io
basado en los datos descubiertos por oci_network_discovery.py
"""

import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path


class DrawIODiagramGenerator:
    """Generador de diagramas Draw.io para infraestructura OCI"""
    
    def __init__(self):
        self.cell_id_counter = 1
        self.edge_id_counter = 1
        
    def generate_network_diagram(self, all_resources, output_file):
        """
        Genera un diagrama Draw.io completo de la infraestructura de red OCI
        
        Args:
            all_resources (dict): Diccionario con recursos por región
            output_file (Path): Ruta del archivo de salida
        """
        # Crear estructura XML del diagrama
        root = self._create_diagram_root()
        
        # Generar contenido del diagrama
        for region, region_resources in all_resources.items():
            self._add_region_section(root, region, region_resources)
        
        # Escribir archivo
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        
    def _create_diagram_root(self):
        """Crea la estructura raíz del diagrama Draw.io"""
        root = ET.Element('mxfile')
        root.set('host', 'Electron')
        root.set('modified', datetime.now().isoformat())
        root.set('agent', 'OCI Network Discovery Tool')
        root.set('etag', 'generated')
        root.set('version', '24.6.4')
        root.set('type', 'device')
        
        # Crear página principal
        diagram = ET.SubElement(root, 'diagram')
        diagram.set('name', 'OCI Network Infrastructure')
        diagram.set('id', 'oci-network-diagram')
        
        # Crear modelo del gráfico
        mx_graph_model = ET.SubElement(diagram, 'mxGraphModel')
        mx_graph_model.set('dx', '4326')
        mx_graph_model.set('dy', '21794')
        mx_graph_model.set('grid', '1')
        mx_graph_model.set('gridSize', '10')
        mx_graph_model.set('guides', '1')
        mx_graph_model.set('tooltips', '1')
        mx_graph_model.set('connect', '1')
        mx_graph_model.set('arrows', '1')
        mx_graph_model.set('fold', '1')
        mx_graph_model.set('page', '1')
        mx_graph_model.set('pageScale', '1')
        mx_graph_model.set('pageWidth', '3300')
        mx_graph_model.set('pageHeight', '2339')
        mx_graph_model.set('math', '0')
        mx_graph_model.set('shadow', '0')
        
        # Crear raíz del gráfico
        graph_root = ET.SubElement(mx_graph_model, 'root')
        
        # Celdas del sistema
        ET.SubElement(graph_root, 'mxCell', id='0')
        ET.SubElement(graph_root, 'mxCell', id='1', parent='0')
        
        return root
        
    def _add_region_section(self, root, region, region_resources):
        """Añade una sección completa para una región"""
        # Obtener el elemento diagram
        diagram = root.find('diagram')
        mx_graph_model = diagram.find('mxGraphModel')
        graph_root = mx_graph_model.find('root')
        
        # Crear título de región
        region_title = ET.SubElement(graph_root, 'mxCell')
        region_title.set('id', f'region-title-{self.cell_id_counter}')
        region_title.set('value', f'<h2>{region}</h2>')
        region_title.set('style', 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontStyle=1')
        region_title.set('vertex', '1')
        region_title.set('parent', '1')
        
        geometry = ET.SubElement(region_title, 'mxGeometry')
        geometry.set('x', '50')
        geometry.set('y', f'{50 + (self.cell_id_counter * 100)}')
        geometry.set('width', '300')
        geometry.set('height', '40')
        geometry.set('as', 'geometry')
        
        self.cell_id_counter += 1
        
        # Añadir DRG si existe
        if region_resources.get('drgs'):
            self._add_drg_section(graph_root, region_resources, region)
            
        # Añadir VCNs conectadas al DRG
        if region_resources.get('drg_attachments'):
            self._add_vcn_section(graph_root, region_resources, region)
            
        # Añadir conexiones VPN
        if region_resources.get('vpn_connections'):
            self._add_vpn_section(graph_root, region_resources, region)
            
        # Añadir FastConnect
        if region_resources.get('fastconnect_connections'):
            self._add_fastconnect_section(graph_root, region_resources, region)
            
    def _add_drg_section(self, graph_root, region_resources, region):
        """Añade la sección del DRG"""
        drg = region_resources['drgs'][0]  # Asumimos un DRG principal por región
        
        # Crear DRG principal
        drg_cell = ET.SubElement(graph_root, 'mxCell')
        drg_cell.set('id', f'drg-{self.cell_id_counter}')
        drg_cell.set('value', f'<b>DRG: {drg.display_name}</b><br/>ID: {drg.id[:20]}...')
        drg_cell.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=14')
        drg_cell.set('vertex', '1')
        drg_cell.set('parent', '1')
        
        geometry = ET.SubElement(drg_cell, 'mxGeometry')
        geometry.set('x', '200')
        geometry.set('y', f'{150 + (self.cell_id_counter * 50)}')
        geometry.set('width', '200')
        geometry.set('height', '80')
        geometry.set('as', 'geometry')
        
        drg_id = self.cell_id_counter
        self.cell_id_counter += 1
        
        # Crear tabla de rutas del DRG
        if region_resources.get('drg_route_tables'):
            self._add_drg_route_table(graph_root, region_resources, drg_id)
            
    def _add_drg_route_table(self, graph_root, region_resources, drg_id):
        """Añade la tabla de rutas del DRG"""
        drg_rt = region_resources['drg_route_tables'][0]
        
        # Crear tabla de rutas
        rt_cell = ET.SubElement(graph_root, 'mxCell')
        rt_cell.set('id', f'drg-rt-{self.cell_id_counter}')
        rt_cell.set('value', f'<b>DRG Route Table</b><br/>{drg_rt.display_name}')
        rt_cell.set('style', 'shape=table;startSize=30;container=1;collapsible=0;childLayout=tableLayout;strokeColor=#36393d;fontSize=12;fillColor=#f9f7ed')
        rt_cell.set('vertex', '1')
        rt_cell.set('parent', '1')
        
        geometry = ET.SubElement(rt_cell, 'mxGeometry')
        geometry.set('x', '450')
        geometry.set('y', f'{150 + (drg_id * 50)}')
        geometry.set('width', '250')
        geometry.set('height', '80')
        geometry.set('as', 'geometry')
        
        self.cell_id_counter += 1
        
    def _add_vcn_section(self, graph_root, region_resources, region):
        """Añade las VCNs conectadas al DRG"""
        vcn_y_offset = 300
        
        for i, attachment in enumerate(region_resources.get('drg_attachments', [])):
            if attachment.vcn_id:
                # Buscar la VCN
                vcn = next((v for v in region_resources['vcns'] if v.id == attachment.vcn_id), None)
                if vcn:
                    # Crear VCN
                    vcn_cell = ET.SubElement(graph_root, 'mxCell')
                    vcn_cell.set('id', f'vcn-{self.cell_id_counter}')
                    vcn_cell.set('value', f'<b>VCN: {vcn.display_name}</b><br/>CIDR: {vcn.cidr_block}')
                    vcn_cell.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12')
                    vcn_cell.set('vertex', '1')
                    vcn_cell.set('parent', '1')
                    
                    geometry = ET.SubElement(vcn_cell, 'mxGeometry')
                    geometry.set('x', '50')
                    geometry.set('y', f'{vcn_y_offset + (i * 120)}')
                    geometry.set('width', '180')
                    geometry.set('height', '60')
                    geometry.set('as', 'geometry')
                    
                    vcn_id = self.cell_id_counter
                    self.cell_id_counter += 1
                    
                    # Conectar VCN al DRG
                    self._add_connection(graph_root, f'vcn-{vcn_id}', 'drg-1', 
                                       f'DRG Attachment: {attachment.display_name}')
                    
                    # Añadir subnets si existen
                    self._add_subnets(graph_root, region_resources, vcn, vcn_id, vcn_y_offset + (i * 120))
                    
    def _add_subnets(self, graph_root, region_resources, vcn, vcn_id, base_y):
        """Añade las subnets de una VCN"""
        vcn_subnets = [s for s in region_resources.get('subnets', []) if s.vcn_id == vcn.id]
        
        for i, subnet in enumerate(vcn_subnets[:3]):  # Máximo 3 subnets por VCN
            subnet_cell = ET.SubElement(graph_root, 'mxCell')
            subnet_cell.set('id', f'subnet-{self.cell_id_counter}')
            subnet_cell.set('value', f'<b>Subnet: {subnet.display_name}</b><br/>CIDR: {subnet.cidr_block}')
            subnet_cell.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=10')
            subnet_cell.set('vertex', '1')
            subnet_cell.set('parent', '1')
            
            geometry = ET.SubElement(subnet_cell, 'mxGeometry')
            geometry.set('x', '250')
            geometry.set('y', f'{base_y + (i * 40)}')
            geometry.set('width', '150')
            geometry.set('height', '40')
            geometry.set('as', 'geometry')
            
            self.cell_id_counter += 1
            
    def _add_vpn_section(self, graph_root, region_resources, region):
        """Añade las conexiones VPN"""
        vpn_y_offset = 800
        
        for i, vpn in enumerate(region_resources.get('vpn_connections', [])):
            # Crear conexión VPN
            vpn_cell = ET.SubElement(graph_root, 'mxCell')
            vpn_cell.set('id', f'vpn-{self.cell_id_counter}')
            vpn_cell.set('value', f'<b>VPN: {vpn.display_name}</b><br/>DRG: {vpn.drg_id[:20]}...')
            vpn_cell.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=12')
            vpn_cell.set('vertex', '1')
            vpn_cell.set('parent', '1')
            
            geometry = ET.SubElement(vpn_cell, 'mxGeometry')
            geometry.set('x', '50')
            geometry.set('y', f'{vpn_y_offset + (i * 80)}')
            geometry.set('width', '180')
            geometry.set('height', '50')
            geometry.set('as', 'geometry')
            
            self.cell_id_counter += 1
            
    def _add_fastconnect_section(self, graph_root, region_resources, region):
        """Añade las conexiones FastConnect"""
        fc_y_offset = 1000
        
        for i, fc in enumerate(region_resources.get('fastconnect_connections', [])):
            # Crear conexión FastConnect
            fc_cell = ET.SubElement(graph_root, 'mxCell')
            fc_cell.set('id', f'fc-{self.cell_id_counter}')
            fc_cell.set('value', f'<b>FastConnect: {fc.display_name}</b><br/>BW: {fc.bandwidth_shape_name}')
            fc_cell.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12')
            fc_cell.set('vertex', '1')
            fc_cell.set('parent', '1')
            
            geometry = ET.SubElement(fc_cell, 'mxGeometry')
            geometry.set('x', '50')
            geometry.set('y', f'{fc_y_offset + (i * 80)}')
            geometry.set('width', '180')
            geometry.set('height', '50')
            geometry.set('as', 'geometry')
            
            self.cell_id_counter += 1
            
    def _add_connection(self, graph_root, source_id, target_id, label):
        """Añade una conexión entre dos elementos"""
        connection = ET.SubElement(graph_root, 'mxCell')
        connection.set('id', f'edge-{self.edge_id_counter}')
        connection.set('style', 'rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;strokeWidth=2')
        connection.set('edge', '1')
        connection.set('parent', '1')
        connection.set('source', source_id)
        connection.set('target', target_id)
        
        # Añadir etiqueta si se proporciona
        if label:
            edge_label = ET.SubElement(connection, 'mxCell')
            edge_label.set('id', f'edge-label-{self.edge_id_counter}')
            edge_label.set('value', label)
            edge_label.set('style', 'edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10')
            edge_label.set('vertex', '1')
            edge_label.set('connectable', '0')
            edge_label.set('parent', f'edge-{self.edge_id_counter}')
            
            label_geometry = ET.SubElement(edge_label, 'mxGeometry')
            label_geometry.set('x', '0.5')
            label_geometry.set('y', '-0.5')
            label_geometry.set('relative', '1')
            label_geometry.set('as', 'geometry')
        
        self.edge_id_counter += 1


class AdvancedDrawIODiagramGenerator:
    """Generador avanzado de diagramas Draw.io similar a ejemplo.drawio"""
    
    def __init__(self):
        self.cell_id_counter = 1
        self.edge_id_counter = 1
        
    def generate_advanced_diagram(self, all_resources, output_file):
        """Genera un diagrama avanzado similar a ejemplo.drawio"""
        root = self._create_advanced_diagram_root()
        
        # Generar diagrama por región
        for region, region_resources in all_resources.items():
            self._add_advanced_region_section(root, region, region_resources)
        
        # Escribir archivo
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        
    def _create_advanced_diagram_root(self):
        """Crea estructura avanzada del diagrama"""
        root = ET.Element('mxfile')
        root.set('host', 'Electron')
        root.set('modified', datetime.now().isoformat())
        root.set('agent', 'OCI Network Discovery Tool - Advanced')
        root.set('etag', 'advanced-generated')
        root.set('version', '24.6.4')
        root.set('type', 'device')
        
        diagram = ET.SubElement(root, 'diagram')
        diagram.set('name', 'OCI Network Infrastructure - Advanced')
        diagram.set('id', 'oci-network-advanced')
        
        mx_graph_model = ET.SubElement(diagram, 'mxGraphModel')
        mx_graph_model.set('dx', '4326')
        mx_graph_model.set('dy', '21794')
        mx_graph_model.set('grid', '1')
        mx_graph_model.set('gridSize', '10')
        mx_graph_model.set('guides', '1')
        mx_graph_model.set('tooltips', '1')
        mx_graph_model.set('connect', '1')
        mx_graph_model.set('arrows', '1')
        mx_graph_model.set('fold', '1')
        mx_graph_model.set('page', '1')
        mx_graph_model.set('pageScale', '1')
        mx_graph_model.set('pageWidth', '3300')
        mx_graph_model.set('pageHeight', '2339')
        mx_graph_model.set('math', '0')
        mx_graph_model.set('shadow', '0')
        
        graph_root = ET.SubElement(mx_graph_model, 'root')
        ET.SubElement(graph_root, 'mxCell', id='0')
        ET.SubElement(graph_root, 'mxCell', id='1', parent='0')
        
        return root
        
    def _add_advanced_region_section(self, root, region, region_resources):
        """Añade sección avanzada de región"""
        diagram = root.find('diagram')
        mx_graph_model = diagram.find('mxGraphModel')
        graph_root = mx_graph_model.find('root')
        
        # Crear DRG central
        if region_resources.get('drgs'):
            self._add_central_drg(graph_root, region_resources, region)
            
        # Crear VCNs alrededor del DRG
        if region_resources.get('drg_attachments'):
            self._add_vcns_around_drg(graph_root, region_resources, region)
            
        # Crear tablas de rutas detalladas
        if region_resources.get('route_tables'):
            self._add_detailed_route_tables(graph_root, region_resources, region)
            
        # Crear conexiones VPN y FastConnect
        self._add_advanced_connections(graph_root, region_resources, region)
        
    def _add_central_drg(self, graph_root, region_resources, region):
        """Añade DRG central con estilo avanzado"""
        drg = region_resources['drgs'][0]
        
        # DRG principal
        drg_cell = ET.SubElement(graph_root, 'mxCell')
        drg_cell.set('id', f'central-drg-{self.cell_id_counter}')
        drg_cell.set('value', f'<div style="font-size: 16px; text-align: center;"><b>{drg.display_name}</b><br/>DRG Central<br/>ID: {drg.id[:20]}...</div>')
        drg_cell.set('style', 'rounded=0;whiteSpace=wrap;html=1;strokeWidth=10;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14')
        drg_cell.set('vertex', '1')
        drg_cell.set('parent', '1')
        
        geometry = ET.SubElement(drg_cell, 'mxGeometry')
        geometry.set('x', '1200')
        geometry.set('y', '1000')
        geometry.set('width', '300')
        geometry.set('height', '200')
        geometry.set('as', 'geometry')
        
        self.cell_id_counter += 1
        
    def _add_vcns_around_drg(self, graph_root, region_resources, region):
        """Añade VCNs alrededor del DRG central"""
        vcn_positions = [
            (800, 800),   # Izquierda arriba
            (1600, 800),  # Derecha arriba
            (800, 1200),  # Izquierda abajo
            (1600, 1200), # Derecha abajo
            (1200, 600),  # Arriba
            (1200, 1400)  # Abajo
        ]
        
        # Obtener el ID del DRG central que se creó primero
        drg_id = None
        for cell in graph_root.findall('mxCell'):
            if cell.get('id', '').startswith('central-drg-'):
                drg_id = cell.get('id')
                break
        
        if not drg_id:
            return
        
        for i, attachment in enumerate(region_resources.get('drg_attachments', [])[:6]):
            if attachment.vcn_id:
                vcn = next((v for v in region_resources['vcns'] if v.id == attachment.vcn_id), None)
                if vcn and i < len(vcn_positions):
                    x, y = vcn_positions[i]
                    
                    # Crear VCN
                    vcn_cell = ET.SubElement(graph_root, 'mxCell')
                    vcn_cell.set('id', f'vcn-{self.cell_id_counter}')
                    vcn_cell.set('value', f'<div style="text-align: center;"><b>{vcn.display_name}</b><br/>CIDR: {vcn.cidr_block}<br/>Compartment: {vcn.compartment_id[:20]}...</div>')
                    vcn_cell.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;strokeWidth=2')
                    vcn_cell.set('vertex', '1')
                    vcn_cell.set('parent', '1')
                    
                    geometry = ET.SubElement(vcn_cell, 'mxGeometry')
                    geometry.set('x', str(x))
                    geometry.set('y', str(y))
                    geometry.set('width', '200')
                    geometry.set('height', '80')
                    geometry.set('as', 'geometry')
                    
                    vcn_id = self.cell_id_counter
                    self.cell_id_counter += 1
                    
                    # Conectar al DRG central usando el ID correcto
                    self._add_advanced_connection(graph_root, f'vcn-{vcn_id}', drg_id, 
                                               f'{attachment.display_name}')
                    
    def _add_detailed_route_tables(self, graph_root, region_resources, region):
        """Añade tablas de rutas detalladas"""
        rt_y_offset = 1800
        
        for i, rt in enumerate(region_resources.get('route_tables', [])[:3]):
            # Crear tabla de rutas
            rt_cell = ET.SubElement(graph_root, 'mxCell')
            rt_cell.set('id', f'rt-{self.cell_id_counter}')
            rt_cell.set('value', f'<b>Route Table: {rt.display_name}</b>')
            rt_cell.set('style', 'shape=table;startSize=30;container=1;collapsible=0;childLayout=tableLayout;strokeColor=#36393d;fontSize=14;fillColor=#f9f7ed')
            rt_cell.set('vertex', '1')
            rt_cell.set('parent', '1')
            
            geometry = ET.SubElement(rt_cell, 'mxGeometry')
            geometry.set('x', '50')
            geometry.set('y', f'{rt_y_offset + (i * 150)}')
            geometry.set('width', '400')
            geometry.set('height', '120')
            geometry.set('as', 'geometry')
            
            self.cell_id_counter += 1
            
            # Añadir reglas de ruta si existen
            if hasattr(rt, 'route_rules') and rt.route_rules:
                self._add_route_rules(graph_root, rt, f'rt-{self.cell_id_counter-1}')
                
    def _add_route_rules(self, graph_root, route_table, rt_id):
        """Añade reglas de ruta a una tabla de rutas"""
        for i, rule in enumerate(route_table.route_rules[:3]):  # Máximo 3 reglas
            rule_cell = ET.SubElement(graph_root, 'mxCell')
            rule_cell.set('id', f'rule-{self.cell_id_counter}')
            rule_cell.set('value', f'Dest: {rule.destination}<br/>Target: {rule.network_entity_id[:20]}...')
            rule_cell.set('style', 'shape=partialRectangle;html=1;whiteSpace=wrap;connectable=0;strokeColor=inherit;overflow=hidden;fillColor=default;top=0;left=0;bottom=0;right=0;pointerEvents=1;fontSize=10')
            rule_cell.set('vertex', '1')
            rule_cell.set('parent', rt_id)
            
            geometry = ET.SubElement(rule_cell, 'mxGeometry')
            geometry.set('x', '0')
            geometry.set('y', f'{30 + (i * 30)}')
            geometry.set('width', '400')
            geometry.set('height', '30')
            geometry.set('as', 'geometry')
            
            self.cell_id_counter += 1
            
    def _add_advanced_connections(self, graph_root, region_resources, region):
        """Añade conexiones avanzadas (VPN, FastConnect, etc.)"""
        # VPN Connections
        vpn_y_offset = 2200
        for i, vpn in enumerate(region_resources.get('vpn_connections', [])[:2]):
            vpn_cell = ET.SubElement(graph_root, 'mxCell')
            vpn_cell.set('id', f'vpn-{self.cell_id_counter}')
            vpn_cell.set('value', f'<div style="text-align: center;"><b>VPN: {vpn.display_name}</b><br/>DRG: {vpn.drg_id[:20]}...<br/>CPE: {vpn.cpe_id[:20]}...</div>')
            vpn_cell.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=12;strokeWidth=3')
            vpn_cell.set('vertex', '1')
            vpn_cell.set('parent', '1')
            
            geometry = ET.SubElement(vpn_cell, 'mxGeometry')
            geometry.set('x', '50')
            geometry.set('y', f'{vpn_y_offset + (i * 100)}')
            geometry.set('width', '250')
            geometry.set('height', '80')
            geometry.set('as', 'geometry')
            
            self.cell_id_counter += 1
            
        # FastConnect Connections
        fc_y_offset = 2400
        for i, fc in enumerate(region_resources.get('fastconnect_connections', [])[:2]):
            fc_cell = ET.SubElement(graph_root, 'mxCell')
            fc_cell.set('id', f'fc-{self.cell_id_counter}')
            fc_cell.set('value', f'<div style="text-align: center;"><b>FastConnect: {fc.display_name}</b><br/>BW: {fc.bandwidth_shape_name}<br/>Type: {fc.type}</div>')
            fc_cell.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;strokeWidth=3')
            fc_cell.set('vertex', '1')
            fc_cell.set('parent', '1')
            
            geometry = ET.SubElement(fc_cell, 'mxGeometry')
            geometry.set('x', '350')
            geometry.set('y', f'{fc_y_offset + (i * 100)}')
            geometry.set('width', '250')
            geometry.set('height', '80')
            geometry.set('as', 'geometry')
            
            self.cell_id_counter += 1
            
    def _add_advanced_connection(self, graph_root, source_id, target_id, label):
        """Añade conexión avanzada entre elementos"""
        connection = ET.SubElement(graph_root, 'mxCell')
        connection.set('id', f'edge-{self.edge_id_counter}')
        connection.set('style', 'rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;strokeWidth=3;strokeColor=#666666')
        connection.set('edge', '1')
        connection.set('parent', '1')
        connection.set('source', source_id)
        connection.set('target', target_id)
        
        # Añadir etiqueta
        if label:
            edge_label = ET.SubElement(connection, 'mxCell')
            edge_label.set('id', f'edge-label-{self.edge_id_counter}')
            edge_label.set('value', label)
            edge_label.set('style', 'edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#666666')
            edge_label.set('vertex', '1')
            edge_label.set('connectable', '0')
            edge_label.set('parent', f'edge-{self.edge_id_counter}')
            
            label_geometry = ET.SubElement(edge_label, 'mxGeometry')
            label_geometry.set('x', '0.5')
            label_geometry.set('y', '-0.5')
            label_geometry.set('relative', '1')
            label_geometry.set('as', 'geometry')
        
        self.edge_id_counter += 1


def generate_oci_network_diagram(all_resources, output_file):
    """
    Función principal para generar diagrama de red OCI básico
    
    Args:
        all_resources (dict): Recursos descubiertos por región
        output_file (Path): Archivo de salida
    """
    generator = DrawIODiagramGenerator()
    generator.generate_network_diagram(all_resources, output_file)
    print(f"Diagrama Draw.io básico generado en: {output_file}")


def generate_advanced_oci_network_diagram(all_resources, output_file):
    """
    Función para generar diagrama avanzado similar a ejemplo.drawio
    
    Args:
        all_resources (dict): Recursos descubiertos por región
        output_file (Path): Archivo de salida
    """
    generator = AdvancedDrawIODiagramGenerator()
    generator.generate_advanced_diagram(all_resources, output_file)
    print(f"Diagrama Draw.io avanzado generado en: {output_file}")
