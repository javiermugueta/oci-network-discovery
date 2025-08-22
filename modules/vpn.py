#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo para obtener información sobre túneles VPN.
"""

import oci


def get_vpn_connections(network_client, compartment_id):
    """
    Obtiene todas las conexiones VPN IPSec en un compartment.
    
    Args:
        network_client: Cliente de red de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos IPSecConnection.
    """
    try:
        vpn_connections_response = oci.pagination.list_call_get_all_results(
            network_client.list_ip_sec_connections,
            compartment_id=compartment_id
        )
        return vpn_connections_response.data
    except Exception as e:
        print(f"Error al obtener conexiones VPN IPSec: {str(e)}")
        return []


def get_vpn_tunnels(network_client, ipsec_id):
    """
    Obtiene todos los túneles de una conexión VPN IPSec.
    
    Args:
        network_client: Cliente de red de OCI.
        ipsec_id (str): ID de la conexión IPSec.
        
    Returns:
        list: Lista de objetos IPSecConnectionTunnel.
    """
    try:
        tunnels_response = oci.pagination.list_call_get_all_results(
            network_client.list_ip_sec_connection_tunnels,
            ipsc_id=ipsec_id
        )
        return tunnels_response.data
    except Exception as e:
        print(f"Error al obtener túneles VPN: {str(e)}")
        return []


def get_cpe_devices(virtual_network_client, compartment_id):
    """
    Obtiene todos los dispositivos CPE (Customer-Premises Equipment) en un compartment.
    
    Args:
        virtual_network_client: Cliente de red virtual de OCI.
        compartment_id (str): ID del compartment.
        
    Returns:
        list: Lista de objetos Cpe.
    """
    try:
        cpe_devices_response = oci.pagination.list_call_get_all_results(
            virtual_network_client.list_cpes,
            compartment_id=compartment_id
        )
        return cpe_devices_response.data
    except Exception as e:
        print(f"Error al obtener dispositivos CPE: {str(e)}")
        return []


def get_cpe_device_shapes(virtual_network_client):
    """
    Obtiene todos los shapes de dispositivos CPE disponibles.
    
    Args:
        virtual_network_client: Cliente de red virtual de OCI.
        
    Returns:
        list: Lista de objetos CpeDeviceShapeDetail.
    """
    try:
        cpe_shapes_response = oci.pagination.list_call_get_all_results(
            virtual_network_client.list_cpe_device_shapes
        )
        return cpe_shapes_response.data
    except Exception as e:
        print(f"Error al obtener shapes de dispositivos CPE: {str(e)}")
        return []