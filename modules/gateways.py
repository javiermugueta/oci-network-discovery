#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo para obtener información sobre gateways (Internet, NAT, Service).
"""

import oci


def get_internet_gateways(network_client, compartment_id, vcn_id):
    """
    Obtiene todos los Internet Gateways en una VCN.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        vcn_id (str): ID de la VCN.
        
    Returns:
        list: Lista de objetos InternetGateway.
    """
    try:
        igws_response = oci.pagination.list_call_get_all_results(
            network_client.list_internet_gateways,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
        return igws_response.data
    except Exception as e:
        print(f"Error al obtener Internet Gateways: {str(e)}")
        return []


def get_nat_gateways(network_client, compartment_id, vcn_id):
    """
    Obtiene todos los NAT Gateways en una VCN.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        vcn_id (str): ID de la VCN.
        
    Returns:
        list: Lista de objetos NatGateway.
    """
    try:
        nat_gws_response = oci.pagination.list_call_get_all_results(
            network_client.list_nat_gateways,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
        return nat_gws_response.data
    except Exception as e:
        print(f"Error al obtener NAT Gateways: {str(e)}")
        return []


def get_service_gateways(network_client, compartment_id, vcn_id):
    """
    Obtiene todos los Service Gateways en una VCN.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        vcn_id (str): ID de la VCN.
        
    Returns:
        list: Lista de objetos ServiceGateway.
    """
    try:
        sgws_response = oci.pagination.list_call_get_all_results(
            network_client.list_service_gateways,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
        return sgws_response.data
    except Exception as e:
        print(f"Error al obtener Service Gateways: {str(e)}")
        return []


def get_local_peering_gateways(network_client, compartment_id, vcn_id):
    """
    Obtiene todos los Local Peering Gateways en una VCN.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        vcn_id (str): ID de la VCN.
        
    Returns:
        list: Lista de objetos LocalPeeringGateway.
    """
    try:
        lpgs_response = oci.pagination.list_call_get_all_results(
            network_client.list_local_peering_gateways,
            compartment_id=compartment_id,
            vcn_id=vcn_id
        )
        return lpgs_response.data
    except Exception as e:
        print(f"Error al obtener Local Peering Gateways: {str(e)}")
        return []