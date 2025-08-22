# OCI Network Discovery Tool

## Descripción
Esta herramienta permite descubrir y documentar toda la configuración de red en un tenant de Oracle Cloud Infrastructure (OCI). La herramienta recorre todos los compartments desde el root hacia abajo y en múltiples regiones para obtener información detallada sobre:

- Virtual Cloud Networks (VCNs)
- Tablas de rutas
- Security Lists
- Network Security Groups
- Gateways (Internet, NAT, Service)
- Dynamic Routing Gateways (DRGs)
- Túneles VPN
- Configuraciones FastConnect
- Remote Peering Connections

## Características

- **Descubrimiento Automático**: Escanea automáticamente todos los compartments desde el root hacia abajo
- **Multi-Región**: Soporte para múltiples regiones de OCI
- **Recursos de Red Completos**: VCNs, subnets, route tables, security lists, gateways, DRGs, VPN, FastConnect
- **Reportes Markdown**: Informes estructurados con tablas y enlaces internos
- **Caché de Descubrimiento**: Evita re-descubrir si ya existe una caché para el mismo tenant/perfil/regiones

## Requisitos
- Python 3.8+
- SDK de OCI para Python
- Credenciales de OCI configuradas

## Instalación
```bash
pip install -r requirements.txt
```

## Uso

### Descubrimiento completo de red (con caché por defecto)
```bash
python oci_network_discovery.py --all-regions
```

### Especificar regiones concretas
```bash
python oci_network_discovery.py --regions eu-madrid-1 eu-frankfurt-1
```

### Control de caché
- Usar caché (por defecto si existe):
```bash
python oci_network_discovery.py --all-regions
```
- Forzar refresco de caché:
```bash
python oci_network_discovery.py --all-regions --refresh-cache
```
- Desactivar caché en esta ejecución:
```bash
python oci_network_discovery.py --all-regions --no-cache
```

La caché se guarda en `output/` con nombre `oci_network_cache_<profile>_<hash>.pkl` (clave por tenancy, perfil y lista de regiones).

## Salida
La herramienta genera:
1. **Archivo Markdown** con tablas detalladas de cada componente de red: `output/oci_network_report_<timestamp>.md`

> Nota: La generación de diagramas (DOT/PNG/Draw.io) ha sido retirada en esta versión.

## Configuración
Asegúrese de tener configurado el archivo de configuración de OCI (~/.oci/config) o proporcione las credenciales como variables de entorno.
