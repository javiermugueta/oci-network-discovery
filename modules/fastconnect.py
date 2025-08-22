#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo para obtener información sobre conexiones FastConnect.
"""

import oci


def get_fastconnect_connections(network_client, compartment_id):
    """
    Obtiene todas las conexiones FastConnect en un compartment.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos VirtualCircuit.
    """
    try:
        # Obtener circuitos virtuales (conexiones FastConnect)
        virtual_circuits_response = oci.pagination.list_call_get_all_results(
            network_client.list_virtual_circuits,
            compartment_id=compartment_id
        )
        return virtual_circuits_response.data
    except Exception as e:
        print(f"Error al obtener conexiones FastConnect: {str(e)}")
        return []


def get_fastconnect_provider_services(network_client, compartment_id):
    """
    Obtiene todos los servicios de proveedores FastConnect disponibles.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos FastConnectProviderService.
    """
    try:
        provider_services_response = oci.pagination.list_call_get_all_results(
            network_client.list_fast_connect_provider_services,
            compartment_id=compartment_id
        )
        return provider_services_response.data
    except Exception as e:
        print(f"Error al obtener servicios de proveedores FastConnect: {str(e)}")
        return []


def get_cross_connect_groups(network_client, compartment_id):
    """
    Obtiene todos los grupos de cross-connects en un compartment.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos CrossConnectGroup.
    """
    try:
        cross_connect_groups_response = oci.pagination.list_call_get_all_results(
            network_client.list_cross_connect_groups,
            compartment_id=compartment_id
        )
        return cross_connect_groups_response.data
    except Exception as e:
        print(f"Error al obtener grupos de cross-connects: {str(e)}")
        return []


def get_cross_connects(network_client, compartment_id, cross_connect_group_id=None):
    """
    Obtiene todos los cross-connects en un compartment, opcionalmente filtrados por grupo.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        cross_connect_group_id (str, optional): ID del grupo de cross-connects para filtrar.
        
    Returns:
        list: Lista de objetos CrossConnect.
    """
    try:
        if cross_connect_group_id:
            cross_connects_response = oci.pagination.list_call_get_all_results(
                network_client.list_cross_connects,
                compartment_id=compartment_id,
                cross_connect_group_id=cross_connect_group_id
            )
        else:
            cross_connects_response = oci.pagination.list_call_get_all_results(
                network_client.list_cross_connects,
                compartment_id=compartment_id
            )
        return cross_connects_response.data
    except Exception as e:
        print(f"Error al obtener cross-connects: {str(e)}")
        return []


def get_cross_connect_locations(network_client, compartment_id):
    """
    Obtiene todas las ubicaciones de cross-connects disponibles.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos CrossConnectLocation.
    """
    try:
        locations_response = oci.pagination.list_call_get_all_results(
            network_client.list_cross_connect_locations,
            compartment_id=compartment_id
        )
        return locations_response.data
    except Exception as e:
        print(f"Error al obtener ubicaciones de cross-connects: {str(e)}")
        return []


def get_cross_connect_port_speed_shapes(network_client, compartment_id):
    """
    Obtiene todas las formas de velocidad de puerto de cross-connect disponibles.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos CrossConnectPortSpeedShape.
    """
    try:
        port_speeds_response = oci.pagination.list_call_get_all_results(
            network_client.list_crossconnect_port_speed_shapes,
            compartment_id=compartment_id
        )
        return port_speeds_response.data
    except Exception as e:
        print(f"Error al obtener formas de velocidad de puerto de cross-connect: {str(e)}")
        return []