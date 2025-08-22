#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo para obtener información sobre VCNs y sus componentes.
"""

import oci


def get_vcns(network_client, compartment_id):
    """
    Obtiene todas las VCNs en un compartment.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos VCN.
    """
    try:
        vcns_response = oci.pagination.list_call_get_all_results(
            network_client.list_vcns,
            compartment_id=compartment_id
        )
        return vcns_response.data
    except Exception as e:
        print(f"Error al obtener VCNs: {str(e)}")
        return []


def get_subnets(network_client, compartment_id, vcn_id):
    """
    Obtiene todas las subnets en una VCN.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        vcn_id (str): ID de la VCN.
        
    Returns:
        list: Lista de objetos Subnet.
    """
    try:
        subnets_response = oci.pagination.list_call_get_all_results(
            network_client.list_subnets,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
        return subnets_response.data
    except Exception as e:
        print(f"Error al obtener subnets: {str(e)}")
        return []


def get_route_tables(network_client, compartment_id, vcn_id):
    """
    Obtiene todas las tablas de rutas en una VCN.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        vcn_id (str): ID de la VCN.
        
    Returns:
        list: Lista de objetos RouteTable.
    """
    try:
        route_tables_response = oci.pagination.list_call_get_all_results(
            network_client.list_route_tables,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
        return route_tables_response.data
    except Exception as e:
        print(f"Error al obtener tablas de rutas: {str(e)}")
        return []


def get_security_lists(network_client, compartment_id, vcn_id):
    """
    Obtiene todas las security lists en una VCN.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        vcn_id (str): ID de la VCN.
        
    Returns:
        list: Lista de objetos SecurityList.
    """
    try:
        security_lists_response = oci.pagination.list_call_get_all_results(
            network_client.list_security_lists,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
        return security_lists_response.data
    except Exception as e:
        print(f"Error al obtener security lists: {str(e)}")
        return []


def get_network_security_groups(network_client, compartment_id, vcn_id):
    """
    Obtiene todos los network security groups en una VCN.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        vcn_id (str): ID de la VCN.
        
    Returns:
        list: Lista de objetos NetworkSecurityGroup.
    """
    try:
        nsgs_response = oci.pagination.list_call_get_all_results(
            network_client.list_network_security_groups,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
        return nsgs_response.data
    except Exception as e:
        print(f"Error al obtener network security groups: {str(e)}")
        return []


def get_nsg_rules(network_client, nsg_id):
    """
    Obtiene todas las reglas de un network security group.
    
    Args:
        network_client: Cliente de red de OCI.
        nsg_id (str): ID del network security group.
        
    Returns:
        tuple: (reglas de entrada, reglas de salida)
    """
    try:
        # Reglas de entrada
        ingress_rules_response = oci.pagination.list_call_get_all_results(
            network_client.list_network_security_group_security_rules,
            network_security_group_id=nsg_id,
            direction="INGRESS"
        )
        
        # Reglas de salida
        egress_rules_response = oci.pagination.list_call_get_all_results(
            network_client.list_network_security_group_security_rules,
            network_security_group_id=nsg_id,
            direction="EGRESS"
        )
        
        return ingress_rules_response.data, egress_rules_response.data
    except Exception as e:
        print(f"Error al obtener reglas de NSG: {str(e)}")
        return [], []