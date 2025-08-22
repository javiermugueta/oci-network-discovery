#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo de autenticación para OCI Network Discovery Tool.
"""

import oci
import os
from pathlib import Path


def authenticate_oci(config_path='~/.oci/config', profile='DEFAULT'):
    """
    Autentica con OCI utilizando el archivo de configuración.
    
    Args:
        config_path (str): Ruta al archivo de configuración de OCI.
        profile (str): Perfil a utilizar en el archivo de configuración.
        
    Returns:
        tuple: (config_dict, identity_client)
    """
    # Expandir la ruta del archivo de configuración
    config_path = os.path.expanduser(config_path)
    
    # Verificar si existe el archivo de configuración
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"El archivo de configuración de OCI no existe: {config_path}")
    
    # Cargar la configuración
    config = oci.config.from_file(config_path, profile)
    
    # Crear cliente de identidad
    identity_client = oci.identity.IdentityClient(config)
    
    # Verificar la autenticación
    try:
        user = identity_client.get_user(config['user']).data
        print(f"Autenticado como: {user.name}")
    except Exception as e:
        raise Exception(f"Error de autenticación: {str(e)}")
    
    return config, identity_client


def get_regions(identity_client):
    """
    Obtiene todas las regiones disponibles en OCI.
    
    Args:
        identity_client: Cliente de identidad de OCI.
        
    Returns:
        list: Lista de nombres de regiones disponibles.
    """
    regions_response = identity_client.list_regions()
    regions = [region.name for region in regions_response.data]
    return regions


def get_subscribed_regions(identity_client, tenancy_id):
    """
    Obtiene las regiones a las que está suscrito el tenancy.
    
    Args:
        identity_client: Cliente de identidad de OCI.
        tenancy_id (str): ID del tenancy.
        
    Returns:
        list: Lista de nombres de regiones suscritas.
    """
    regions_response = identity_client.list_region_subscriptions(tenancy_id)
    subscribed_regions = [region.region_name for region in regions_response.data]
    return subscribed_regions