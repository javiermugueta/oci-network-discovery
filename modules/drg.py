#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo para obtener información sobre DRGs y sus componentes.
"""

import oci


def get_drgs(network_client, compartment_id):
    """
    Obtiene todos los DRGs en un compartment.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos DRG.
    """
    try:
        drgs_response = oci.pagination.list_call_get_all_results(
            network_client.list_drgs,
            compartment_id=compartment_id
        )
        return drgs_response.data
    except Exception as e:
        print(f"Error al obtener DRGs: {str(e)}")
        return []


def get_drg_attachments(network_client, compartment_id, drg_id=None):
    """
    Obtiene todos los DRG Attachments en un compartment, opcionalmente filtrados por DRG ID.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        drg_id (str, optional): ID del DRG para filtrar.
        
    Returns:
        list: Lista de objetos DrgAttachment.
    """
    try:
        if drg_id:
            attachments_response = oci.pagination.list_call_get_all_results(
                network_client.list_drg_attachments,
                compartment_id=compartment_id,
                drg_id=drg_id
            )
        else:
            attachments_response = oci.pagination.list_call_get_all_results(
                network_client.list_drg_attachments,
                compartment_id=compartment_id
            )
        return attachments_response.data
    except Exception as e:
        print(f"Error al obtener DRG Attachments: {str(e)}")
        return []


def get_remote_peering_connections(network_client, compartment_id, drg_id=None):
    """
    Obtiene todos los Remote Peering Connections en un compartment, opcionalmente filtrados por DRG ID.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        drg_id (str, optional): ID del DRG para filtrar.
        
    Returns:
        list: Lista de objetos RemotePeeringConnection.
    """
    try:
        if drg_id:
            rpcs_response = oci.pagination.list_call_get_all_results(
                network_client.list_remote_peering_connections,
                compartment_id=compartment_id,
                drg_id=drg_id
            )
        else:
            rpcs_response = oci.pagination.list_call_get_all_results(
                network_client.list_remote_peering_connections,
                compartment_id=compartment_id
            )
        return rpcs_response.data
    except Exception as e:
        print(f"Error al obtener Remote Peering Connections: {str(e)}")
        return []


def get_drg_route_tables(network_client, drg_id):
    """
    Obtiene todas las tablas de rutas de un DRG.
    
    Args:
        network_client: Cliente de red de OCI.
        drg_id (str): ID del DRG.
        
    Returns:
        list: Lista de objetos DrgRouteTable.
    """
    try:
        route_tables_response = oci.pagination.list_call_get_all_results(
            network_client.list_drg_route_tables,
            drg_id=drg_id
        )
        return route_tables_response.data
    except Exception as e:
        print(f"Error al obtener DRG Route Tables: {str(e)}")
        return []


def get_drg_route_distributions(network_client, drg_id):
    """
    Obtiene todas las distribuciones de rutas de un DRG.
    
    Args:
        network_client: Cliente de red de OCI.
        drg_id (str): ID del DRG.
        
    Returns:
        list: Lista de objetos DrgRouteDistribution.
    """
    try:
        distributions_response = oci.pagination.list_call_get_all_results(
            network_client.list_drg_route_distributions,
            drg_id=drg_id
        )
        return distributions_response.data
    except Exception as e:
        print(f"Error al obtener DRG Route Distributions: {str(e)}")
        return []