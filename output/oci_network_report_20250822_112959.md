# Informe de Infraestructura de Red en OCI

Generado el: 2025-08-22 11:29:59

## Índice
- [eu-madrid-1](#region-eu-madrid-1)
  - [VCNs](#region-eu-madrid-1-vcns)
  - [DRGs](#region-eu-madrid-1-drgs)
  - [Conexiones VPN IPSec](#region-eu-madrid-1-vpn)
  - [Conexiones FastConnect](#region-eu-madrid-1-fc)
  - [Recursos por VCN](#region-eu-madrid-1-vcns)
- [eu-amsterdam-1](#region-eu-amsterdam-1)
  - [VCNs](#region-eu-amsterdam-1-vcns)
  - [DRGs](#region-eu-amsterdam-1-drgs)
  - [Conexiones VPN IPSec](#region-eu-amsterdam-1-vpn)
  - [Conexiones FastConnect](#region-eu-amsterdam-1-fc)
  - [Recursos por VCN](#region-eu-amsterdam-1-vcns)

<a id="region-eu-madrid-1"></a>
## Región: eu-madrid-1

### Virtual Cloud Networks (VCNs)

| ID                                                                                     | Nombre                                                                                                                           | CIDR            | Estado    | Compartment                                                                                   |
|:---------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:----------------|:----------|:----------------------------------------------------------------------------------------------|
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqa6ljzhvq2wir3akbcehhzh4rh7ldp74pivry6mx6zbofa | [prueba-loganalytics](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqa6ljzhvq2wir3akbcehhzh4rh7ldp74pivry6mx6zbofa)               | 10.0.0.0/24     | AVAILABLE | lab (ocid1.compartment.oc1..aaaaaaaadggbrkmkqmkeuhj5e34heegrk7aut6sf6uforqha4cas6yiayena)     |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqazyjndml5veonnw4cv6r6nggt3xlmzra3kr2beucuntsa | [test](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqazyjndml5veonnw4cv6r6nggt3xlmzra3kr2beucuntsa)                              | 10.0.0.0/16     | AVAILABLE | lab (ocid1.compartment.oc1..aaaaaaaadggbrkmkqmkeuhj5e34heegrk7aut6sf6uforqha4cas6yiayena)     |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak2qmyvh2snjx47rugsmynh4tfnv6ktw2bydm2f6awtrq | [oci-mad-it-vnet-genai-dev](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak2qmyvh2snjx47rugsmynh4tfnv6ktw2bydm2f6awtrq)         | 10.201.6.192/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaav5dajjyzpfej6ryttmjodknp3f3txc6j4ob66zss2zq | [oci-mad-it-vnet-functions-dev](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaav5dajjyzpfej6ryttmjodknp3f3txc6j4ob66zss2zq)     | 10.201.2.128/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaacji2lss3a6gj6mbcvmvcjiafypd2i5cm7s4mmez6x5a | [oci-mad-it-vnet-forms-dev](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaacji2lss3a6gj6mbcvmvcjiafypd2i5cm7s4mmez6x5a)         | 10.201.2.64/26  | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqatr3prxqnl7stm443adrnllgt63lnwcryq4b3b7tqg22a | [oci-mad-it-vnet-functions-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqatr3prxqnl7stm443adrnllgt63lnwcryq4b3b7tqg22a)     | 10.201.2.192/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqazkakfjy63mfmjjxrtg2u7qpv2zr5rx5iczt6hgcu7sia | [oci-mad-it-vnet-vdipro-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqazkakfjy63mfmjjxrtg2u7qpv2zr5rx5iczt6hgcu7sia)        | 10.201.6.128/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqad4odlbg3o4ifzh74maz5ix7bwzxg4aglladl5ivn3pqa | [oci-mad-ot-vnet-mw-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqad4odlbg3o4ifzh74maz5ix7bwzxg4aglladl5ivn3pqa)            | 10.201.1.192/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqackqoptlccngvmili6wlwhuwnkeiyb3lbbmmbkyp7ql4a | [oci-mad-it-vnet-mw-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqackqoptlccngvmili6wlwhuwnkeiyb3lbbmmbkyp7ql4a)            | 10.201.1.64/26  | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqa73te6izbug6ojlzmgoy4uam7ny2c3j7cuqits6ux3swq | [oci-mad-ot-vnet-db-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqa73te6izbug6ojlzmgoy4uam7ny2c3j7cuqits6ux3swq)            | 10.201.0.192/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqamdoeypz2ypqsxray72wtx4didpbigg5xnguflaikxxwq | [oci-mad-it-vnet-db-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqamdoeypz2ypqsxray72wtx4didpbigg5xnguflaikxxwq)            | 10.201.0.64/26  | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqae3yvzexhcz7rlk2cr6znmvntybpmvnl5ve6syoci5b6a | [oci-mad-it-vnet-tools-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqae3yvzexhcz7rlk2cr6znmvntybpmvnl5ve6syoci5b6a)         | 10.201.6.0/26   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqasx3pjyo3ns26o6kcscd6k6ra5i2po37b67pohyq2rnda | [oci-mad-it-vnet-vdi-customers-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqasx3pjyo3ns26o6kcscd6k6ra5i2po37b67pohyq2rnda) | 10.201.4.0/23   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaojnh3jumgng25plrbx5fqpxc3hvebmu3tk3exvtbm6pq | [oci-mad-it-vnet-tools-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaojnh3jumgng25plrbx5fqpxc3hvebmu3tk3exvtbm6pq)         | 10.201.6.64/26  | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqawax7byicjrczregt6kkxorhklmebgbg33thaulnwzq4q | [oci-mad-it-vnet-db-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqawax7byicjrczregt6kkxorhklmebgbg33thaulnwzq4q)            | 10.201.0.128/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqartv6joutkh6ca6bm5mfvt543fgjal2oqzk36ek7lnqxa | [oci-mad-ot-vnet-db-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqartv6joutkh6ca6bm5mfvt543fgjal2oqzk36ek7lnqxa)            | 10.201.1.0/26   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqatnwllzc5fjv26vtxa3xi3ejkmdsjgrmgfjmsk2t4t2da | [oci-mad-it-vnet-mw-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqatnwllzc5fjv26vtxa3xi3ejkmdsjgrmgfjmsk2t4t2da)            | 10.201.1.128/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak3th2pjmr7nybv5kdvou2fdycfl6wialdm75vwxutcpq | [oci-mad-ot-vnet-mw-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak3th2pjmr7nybv5kdvou2fdycfl6wialdm75vwxutcpq)            | 10.201.2.0/26   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak3mn33cxhn3zcimaotuoxtwdw3hjcnv76g6mhfxcupiq | [oci-mad-vnet-hub-sha](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak3mn33cxhn3zcimaotuoxtwdw3hjcnv76g6mhfxcupiq)              | 10.201.0.0/26   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq) |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqa6ljzhvq2wir3akbcehhzh4rh7ldp74pivry6mx6zbofa"></a>
#### Recursos de VCN: prueba-loganalytics (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqa6ljzhvq2wir3akbcehhzh4rh7ldp74pivry6mx6zbofa)

##### Subnets

| ID                                                                                        | Nombre   | CIDR        | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                                      | Route Table ID                                                                                | Security Lists                                                                                                                                       |
|:------------------------------------------------------------------------------------------|:---------|:------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaamubyqbgn6k6gxv6sza4j3zgr45l6knyaffvgrmavg3xc3on34efa | prueba   | 10.0.0.0/26 | Regional         | Sí        | AVAILABLE | [Default Route Table for prueba-loganalytics](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaniijtev4wl3q2fgwvumlyjraifrl3fdi33fjicrn47gj33x6ysfa) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaniijtev4wl3q2fgwvumlyjraifrl3fdi33fjicrn47gj33x6ysfa | [Default Security List for prueba-loganalytics](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaobldrqtd2ohhwbbrync3hqtjai6l7ot3gsrv7mpcrsuvzt5ycokq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaniijtev4wl3q2fgwvumlyjraifrl3fdi33fjicrn47gj33x6ysfa"></a>
###### Default Route Table for prueba-loganalytics (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaniijtev4wl3q2fgwvumlyjraifrl3fdi33fjicrn47gj33x6ysfa)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaobldrqtd2ohhwbbrync3hqtjai6l7ot3gsrv7mpcrsuvzt5ycokq"></a>
###### Default Security List for prueba-loganalytics (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaobldrqtd2ohhwbbrync3hqtjai6l7ot3gsrv7mpcrsuvzt5ycokq)

####### Reglas de Entrada

| Origen      | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0   | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0   | CIDR_BLOCK       | ICMP        |           |               |
| 10.0.0.0/24 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

No se encontraron DRG Attachments en esta VCN.

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqazyjndml5veonnw4cv6r6nggt3xlmzra3kr2beucuntsa"></a>
#### Recursos de VCN: test (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqazyjndml5veonnw4cv6r6nggt3xlmzra3kr2beucuntsa)

##### Subnets

| ID                                                                                        | Nombre   | CIDR        | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                       | Route Table ID                                                                                | Security Lists                                                                                                                        |
|:------------------------------------------------------------------------------------------|:---------|:------------|:-----------------|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaosfcnqpvw5lps6f3jveg2oho2nxhhwi73wqvip26sfbxy3wr3sya | test     | 10.0.1.0/24 | Regional         | Sí        | AVAILABLE | [Default Route Table for test](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaq56rbmfkzw7azolowj7fbqa43pxrgmr5tzcxkksrj22t5wbxcyja) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaq56rbmfkzw7azolowj7fbqa43pxrgmr5tzcxkksrj22t5wbxcyja | [Default Security List for test](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaau3ufk4dj7colkybd3ogmzyppeoa7bynhpnv7fmhehnetia7exrma) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaq56rbmfkzw7azolowj7fbqa43pxrgmr5tzcxkksrj22t5wbxcyja"></a>
###### Default Route Table for test (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaq56rbmfkzw7azolowj7fbqa43pxrgmr5tzcxkksrj22t5wbxcyja)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                                              | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [Internet Gateway](#igw-ocid1_internetgateway_oc1_eu_madrid_1_aaaaaaaa5sm4gr2rtelfuk6d33mhgbkhcmiged76dgvnq6s6wt4b3tk537vq) | Internet Gateway  |               |

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaau3ufk4dj7colkybd3ogmzyppeoa7bynhpnv7fmhehnetia7exrma"></a>
###### Default Security List for test (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaau3ufk4dj7colkybd3ogmzyppeoa7bynhpnv7fmhehnetia7exrma)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.0.0.0/16     | CIDR_BLOCK       | ICMP        |           |               |
| 88.1.202.205/32 | CIDR_BLOCK       | TCP         | 22-22     |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

No se encontraron DRG Attachments en esta VCN.

##### Internet Gateways

<a id="igw-ocid1_internetgateway_oc1_eu_madrid_1_aaaaaaaa5sm4gr2rtelfuk6d33mhgbkhcmiged76dgvnq6s6wt4b3tk537vq"></a>
| ID                                                                                                 | Nombre   | Habilitado   | Estado    |
|:---------------------------------------------------------------------------------------------------|:---------|:-------------|:----------|
| ocid1.internetgateway.oc1.eu-madrid-1.aaaaaaaa5sm4gr2rtelfuk6d33mhgbkhcmiged76dgvnq6s6wt4b3tk537vq | test     | Sí           | AVAILABLE |

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak2qmyvh2snjx47rugsmynh4tfnv6ktw2bydm2f6awtrq"></a>
#### Recursos de VCN: oci-mad-it-vnet-genai-dev (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak2qmyvh2snjx47rugsmynh4tfnv6ktw2bydm2f6awtrq)

##### Subnets

| ID                                                                                        | Nombre                    | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                | Route Table ID                                                                                | Security Lists                                                                                                                                                                                                                                                                             |
|:------------------------------------------------------------------------------------------|:--------------------------|:----------------|:-----------------|:----------|:----------|:---------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaae7xkevtljh5cr2soom4cntchfzp5scrcm33grdowcdjato72cgfq | oci-mad-it-snet-genai-dev | 10.201.6.192/26 | Regional         | No        | AVAILABLE | [oci-mad-udr-genai-dev](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaq6jt24iucddlsbqsk3ayu3as6a2b3h2corqvf5v2efdz53ah7vaa) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaq6jt24iucddlsbqsk3ayu3as6a2b3h2corqvf5v2efdz53ah7vaa | [oci-mad-it-sl-genai-dev](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaevgfq4vhmp3w72jnpqa5j4gbpxqpfebdgufwxkrraogm7ya6kopa), [Default Security List for oci-mad-it-vnet-genai-dev](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaay3g6rfyrkkqn3o4pwnrlcupuyrsujknm3izkgz2mxuybf7lf4ula) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaq6jt24iucddlsbqsk3ayu3as6a2b3h2corqvf5v2efdz53ah7vaa"></a>
###### oci-mad-udr-genai-dev (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaq6jt24iucddlsbqsk3ayu3as6a2b3h2corqvf5v2efdz53ah7vaa)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                     | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaycbu7kfogqsign25skim66uzzmhru6c423wic6oszy2qsjrqhjaa"></a>
###### Default Route Table for oci-mad-it-vnet-genai-dev (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaycbu7kfogqsign25skim66uzzmhru6c423wic6oszy2qsjrqhjaa)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaevgfq4vhmp3w72jnpqa5j4gbpxqpfebdgufwxkrraogm7ya6kopa"></a>
###### oci-mad-it-sl-genai-dev (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaevgfq4vhmp3w72jnpqa5j4gbpxqpfebdgufwxkrraogm7ya6kopa)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 1521-1522 | ADB GenAI     |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

No hay reglas de salida definidas.

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaay3g6rfyrkkqn3o4pwnrlcupuyrsujknm3izkgz2mxuybf7lf4ula"></a>
###### Default Security List for oci-mad-it-vnet-genai-dev (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaay3g6rfyrkkqn3o4pwnrlcupuyrsujknm3izkgz2mxuybf7lf4ula)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.6.192/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                              | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaamozmwbs6ecnzsz7lyfgfxul6qap5uzevevb3gmgqfqyatapnyjqa | oci-mad-it-drgattach-vnet-genai-dev | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaav5dajjyzpfej6ryttmjodknp3f3txc6j4ob66zss2zq"></a>
#### Recursos de VCN: oci-mad-it-vnet-functions-dev (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaav5dajjyzpfej6ryttmjodknp3f3txc6j4ob66zss2zq)

##### Subnets

| ID                                                                                        | Nombre                        | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                       | Route Table ID                                                                                | Security Lists                                                                                                                       |
|:------------------------------------------------------------------------------------------|:------------------------------|:----------------|:-----------------|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaa5qbk7jya4lztncllwwfuag42qh3ia46a4vkztampk7vn32ixppsa | oci-mad-it-snet-functions-dev | 10.201.2.128/26 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-functions-dev](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaam5y6qlplmgbhbzwbbft3z3rhruuvwjhhdq7qgfs7hcuu546fmpvq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaam5y6qlplmgbhbzwbbft3z3rhruuvwjhhdq7qgfs7hcuu546fmpvq | [oci-mad-it-sl-functions-dev-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaailvppd46lvhcyeeadynjonuoodqjqjeh2os3mjnobdnvt4muzu7q) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaam5y6qlplmgbhbzwbbft3z3rhruuvwjhhdq7qgfs7hcuu546fmpvq"></a>
###### oci-mad-it-udr-functions-dev (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaam5y6qlplmgbhbzwbbft3z3rhruuvwjhhdq7qgfs7hcuu546fmpvq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |
| all-mad-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaapn6dxt7iv4vtwddnqj6m7bq57cvcks5rou5ipqt24kx4w55nprjq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaau2zrsx7wt22pmjg7iwp4lz4zu72baqqnfq4mvmnomzfix5uu35hq"></a>
###### Default Route Table for oci-mad-it-vnet-functions-dev (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaau2zrsx7wt22pmjg7iwp4lz4zu72baqqnfq4mvmnomzfix5uu35hq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaailvppd46lvhcyeeadynjonuoodqjqjeh2os3mjnobdnvt4muzu7q"></a>
###### oci-mad-it-sl-functions-dev-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaailvppd46lvhcyeeadynjonuoodqjqjeh2os3mjnobdnvt4muzu7q)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | Todos       |           |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa26mqu7x4tpeurqli3f4uwz7pfehpj7ty6dwnufkz3gx2e7rr3raa"></a>
###### Default Security List for oci-mad-it-vnet-functions-dev (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa26mqu7x4tpeurqli3f4uwz7pfehpj7ty6dwnufkz3gx2e7rr3raa)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.2.128/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                                  | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:----------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaai2qegxqm7ljrwb7iizey67rk7grmuusxzyokl5zyugnwxeoiiniq | oci-mad-it-drgattach-vnet-functions-dev | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaapn6dxt7iv4vtwddnqj6m7bq57cvcks5rou5ipqt24kx4w55nprjq"></a>
| ID                                                                                                | Nombre                            | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:----------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaapn6dxt7iv4vtwddnqj6m7bq57cvcks5rou5ipqt24kx4w55nprjq | oci-mad-it-vngw-svc-functions-dev | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaacji2lss3a6gj6mbcvmvcjiafypd2i5cm7s4mmez6x5a"></a>
#### Recursos de VCN: oci-mad-it-vnet-forms-dev (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaacji2lss3a6gj6mbcvmvcjiafypd2i5cm7s4mmez6x5a)

##### Subnets

| ID                                                                                        | Nombre                    | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                   | Route Table ID                                                                                | Security Lists                                                                                                                   |
|:------------------------------------------------------------------------------------------|:--------------------------|:---------------|:-----------------|:----------|:----------|:------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaazjy37knx3bxctz7qkfbn36o6omdxnsj5ovfd4bgvkwnephmfocpa | oci-mad-it-snet-forms-dev | 10.201.2.64/26 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-forms-dev](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaasjiosmq672hpxj6uffdmbnbssv72ozra7a7lalnpkra3fnprzhcq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaasjiosmq672hpxj6uffdmbnbssv72ozra7a7lalnpkra3fnprzhcq | [oci-mad-it-sl-forms-dev-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaajqzvnvlvczkmphyylwvb7rz4pftsdqkvg2mbiwfowommw5rdkhaa) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaasjiosmq672hpxj6uffdmbnbssv72ozra7a7lalnpkra3fnprzhcq"></a>
###### oci-mad-it-udr-forms-dev (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaasjiosmq672hpxj6uffdmbnbssv72ozra7a7lalnpkra3fnprzhcq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |
| all-mad-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaao4winpkvgk7o7rpda5j5phpwiotafpctgcwgvhdft2qukkddiyha) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaapm6ns3fhwm5lxauzjqdyxs2u57eas7acubzpeoqhamnkayc2bmwa"></a>
###### Default Route Table for oci-mad-it-vnet-forms-dev (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaapm6ns3fhwm5lxauzjqdyxs2u57eas7acubzpeoqhamnkayc2bmwa)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaajqzvnvlvczkmphyylwvb7rz4pftsdqkvg2mbiwfowommw5rdkhaa"></a>
###### oci-mad-it-sl-forms-dev-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaajqzvnvlvczkmphyylwvb7rz4pftsdqkvg2mbiwfowommw5rdkhaa)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0  | CIDR_BLOCK       | TCP         | 3389-3389 | rdp           |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |
| 0.0.0.0/0  | CIDR_BLOCK       | TCP         | 443-443   |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaag2zlfstgzmevzosfhcjwuyzlig4mtvnxfjmb7bg7i5etaxxolkqq"></a>
###### Default Security List for oci-mad-it-vnet-forms-dev (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaag2zlfstgzmevzosfhcjwuyzlig4mtvnxfjmb7bg7i5etaxxolkqq)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.2.64/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                              | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaaokzglw4vxei3bc7m6lrjiigjjfafvgpfqn2w2zaforcm2o6rqeea | oci-mad-it-drgattach-vnet-forms-dev | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaao4winpkvgk7o7rpda5j5phpwiotafpctgcwgvhdft2qukkddiyha"></a>
| ID                                                                                                | Nombre                        | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaao4winpkvgk7o7rpda5j5phpwiotafpctgcwgvhdft2qukkddiyha | oci-mad-it-vngw-svc-forms-dev | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqatr3prxqnl7stm443adrnllgt63lnwcryq4b3b7tqg22a"></a>
#### Recursos de VCN: oci-mad-it-vnet-functions-pro (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqatr3prxqnl7stm443adrnllgt63lnwcryq4b3b7tqg22a)

##### Subnets

| ID                                                                                        | Nombre                        | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                       | Route Table ID                                                                                | Security Lists                                                                                                                       |
|:------------------------------------------------------------------------------------------|:------------------------------|:----------------|:-----------------|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaqdcwcxdqo3f3fho33qtpxztpug33lsiiilnkccndb7cujadglsdq | oci-mad-it-snet-functions-pro | 10.201.2.192/26 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-functions-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaalkzw4yz6ttxh4xg5iymfqqo476af46qnr2sh64mmku6zbyy6doaa) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaalkzw4yz6ttxh4xg5iymfqqo476af46qnr2sh64mmku6zbyy6doaa | [oci-mad-it-sl-functions-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaw7sgrp5g7v4u3qfnl5ipereqsfmb33q7jpijwgey3rycb43fmxuq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaalkzw4yz6ttxh4xg5iymfqqo476af46qnr2sh64mmku6zbyy6doaa"></a>
###### oci-mad-it-udr-functions-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaalkzw4yz6ttxh4xg5iymfqqo476af46qnr2sh64mmku6zbyy6doaa)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| all-mad-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaatkoumquxz2cxyruybvmxnb4grg355rnr56f32wxrb6lgqsdmtcgq) | Service Gateway   |               |
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa4dvo7gg5n7et4kvf26gl7p6473maahrlulxn2sc3nqdo75can5sq"></a>
###### Default Route Table for oci-mad-it-vnet-functions-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa4dvo7gg5n7et4kvf26gl7p6473maahrlulxn2sc3nqdo75can5sq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaw7sgrp5g7v4u3qfnl5ipereqsfmb33q7jpijwgey3rycb43fmxuq"></a>
###### oci-mad-it-sl-functions-pro-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaw7sgrp5g7v4u3qfnl5ipereqsfmb33q7jpijwgey3rycb43fmxuq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | Todos       |           |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaynq52lspqjf44k7angrrfvd57vkdidkgbqabqjz6kp62yilj5jsa"></a>
###### Default Security List for oci-mad-it-vnet-functions-pro (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaynq52lspqjf44k7angrrfvd57vkdidkgbqabqjz6kp62yilj5jsa)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.2.192/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                                  | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:----------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaauau3iuhny2aluzcujgnxvhuhfuhnslzbg3h3k5jykgfnqqk3kiia | oci-mad-it-drgattach-vnet-functions-pro | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaatkoumquxz2cxyruybvmxnb4grg355rnr56f32wxrb6lgqsdmtcgq"></a>
| ID                                                                                                | Nombre                            | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:----------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaatkoumquxz2cxyruybvmxnb4grg355rnr56f32wxrb6lgqsdmtcgq | oci-mad-it-vngw-svc-functions-pro | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqazkakfjy63mfmjjxrtg2u7qpv2zr5rx5iczt6hgcu7sia"></a>
#### Recursos de VCN: oci-mad-it-vnet-vdipro-pro (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqazkakfjy63mfmjjxrtg2u7qpv2zr5rx5iczt6hgcu7sia)

##### Subnets

| ID                                                                                        | Nombre                  | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                    | Route Table ID                                                                                | Security Lists                                                                                                                    |
|:------------------------------------------------------------------------------------------|:------------------------|:----------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaad2td32uyafi7hzd7diqdifdhsd2o375umtznvcvtpx72ij3524ea | oci-mad-snet-vdipro-pro | 10.201.6.128/26 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-vdipro-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaawbecmxek5pz4eecdbaodzhgrjfmuemogf2fqayettenspgc5gyaa) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaawbecmxek5pz4eecdbaodzhgrjfmuemogf2fqayettenspgc5gyaa | [oci-mad-it-sl-vdipro-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa4ijziywm7ujcnhguf22qcoveu6amfndky7cgw2ltavuzrxnpbana) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaawbecmxek5pz4eecdbaodzhgrjfmuemogf2fqayettenspgc5gyaa"></a>
###### oci-mad-it-udr-vdipro-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaawbecmxek5pz4eecdbaodzhgrjfmuemogf2fqayettenspgc5gyaa)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| all-mad-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaazuhydbdqdrmxmz7pkgce4cno4amq62t5d7ytykwflcgbexzfapfq) | Service Gateway   |               |
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaxtzr3xebxhlmwftn76mo2pqkugmu5ot4z3mj73ryx6l5ddn36jaq"></a>
###### Default Route Table for oci-mad-it-vnet-vdipro-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaxtzr3xebxhlmwftn76mo2pqkugmu5ot4z3mj73ryx6l5ddn36jaq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa4ijziywm7ujcnhguf22qcoveu6amfndky7cgw2ltavuzrxnpbana"></a>
###### oci-mad-it-sl-vdipro-pro-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa4ijziywm7ujcnhguf22qcoveu6amfndky7cgw2ltavuzrxnpbana)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3389-3389 | rdp           |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaakzwxcgv2odo2xitcwf7tqmegsl4ey46csofhtiyedg57pp227jqa"></a>
###### Default Security List for oci-mad-it-vnet-vdipro-pro (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaakzwxcgv2odo2xitcwf7tqmegsl4ey46csofhtiyedg57pp227jqa)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.6.128/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                               | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:-------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaadqafad3na6yeckbkr4wuz6uk3imw5mqctni6gqkqbpwwerwfy4gq | oci-mad-it-drgattach-vnet-vdipro-pro | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaazuhydbdqdrmxmz7pkgce4cno4amq62t5d7ytykwflcgbexzfapfq"></a>
| ID                                                                                                | Nombre                         | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:-------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaazuhydbdqdrmxmz7pkgce4cno4amq62t5d7ytykwflcgbexzfapfq | oci-mad-it-vngw-svc-vdipro-pro | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqad4odlbg3o4ifzh74maz5ix7bwzxg4aglladl5ivn3pqa"></a>
#### Recursos de VCN: oci-mad-ot-vnet-mw-pro (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqad4odlbg3o4ifzh74maz5ix7bwzxg4aglladl5ivn3pqa)

##### Subnets

| ID                                                                                        | Nombre                       | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                      | Route Table ID                                                                                | Security Lists                                                                                                                |
|:------------------------------------------------------------------------------------------|:-----------------------------|:----------------|:-----------------|:----------|:----------|:---------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaxlryf5d5i6vyimixdskoxivsvgcnra7mlqpjdpmnqppqz3wuox2q | oci-mad-ot-snet-mw-back-pro  | 10.201.1.208/28 | Regional         | No        | AVAILABLE | [oci-mad-ot-udr-mw-back-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaai6onnkaurqylsb26vvz5m3gsjnnzvc3pmy2lbce7todamn2cm4cq)  | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaai6onnkaurqylsb26vvz5m3gsjnnzvc3pmy2lbce7todamn2cm4cq | [oci-mad-ot-sl-mw-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa5saa4gxeg5ybxt64sqa4vegiitxesdgdv6awfkr5llibkanykxkq) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaahtnugopnr4huhzicx2d6ple5fx6bvxg4et4sdksjlcmmkdmjs35a | oci-mad-ot-snet-mw-front-pro | 10.201.1.192/28 | Regional         | No        | AVAILABLE | [oci-mad-ot-udr-mw-front-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa6qjzwlfczbbjm6fouwqwf56z5kgaflbnaocm4xl4khjszznfkndq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa6qjzwlfczbbjm6fouwqwf56z5kgaflbnaocm4xl4khjszznfkndq | [oci-mad-ot-sl-mw-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa5saa4gxeg5ybxt64sqa4vegiitxesdgdv6awfkr5llibkanykxkq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaai6onnkaurqylsb26vvz5m3gsjnnzvc3pmy2lbce7todamn2cm4cq"></a>
###### oci-mad-ot-udr-mw-back-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaai6onnkaurqylsb26vvz5m3gsjnnzvc3pmy2lbce7todamn2cm4cq)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción                                                                          |
|:----------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:-------------------------------------------------------------------------------------|
| 0.0.0.0/0             | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |                                                                                      |
| oci-mad-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaltnhtbmnk6pfxzsgd5byzmtmf5w3rwmdnnz5xi2chintm5ifwqaa) | Service Gateway   | The run command needs acces to object storage when the script is stored in a abucket |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa6qjzwlfczbbjm6fouwqwf56z5kgaflbnaocm4xl4khjszznfkndq"></a>
###### oci-mad-ot-udr-mw-front-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa6qjzwlfczbbjm6fouwqwf56z5kgaflbnaocm4xl4khjszznfkndq)

No hay reglas de ruta definidas.

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaoremqel4xid4croen6pj2cnrjw6g7nrwgyldakp2qteuzehnvdza"></a>
###### Default Route Table for oci-mad-ot-vnet-mw-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaoremqel4xid4croen6pj2cnrjw6g7nrwgyldakp2qteuzehnvdza)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa5saa4gxeg5ybxt64sqa4vegiitxesdgdv6awfkr5llibkanykxkq"></a>
###### oci-mad-ot-sl-mw-pro-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa5saa4gxeg5ybxt64sqa4vegiitxesdgdv6awfkr5llibkanykxkq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300 | Veeam Backup  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22     |               |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160 | Veeam Backup  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8080-8081 |               |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3389-3389 | rdp           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162 | Veeam Backup  |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaszumpxsnc7tz5bnylvut7uh2ei2kfjq3fo5y6e2azife5cr2kkfa"></a>
###### Default Security List for oci-mad-ot-vnet-mw-pro (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaszumpxsnc7tz5bnylvut7uh2ei2kfjq3fo5y6e2azife5cr2kkfa)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.1.192/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                           | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaacecxf5x562g65w3vveo2acpepkdrw4wqkg6qnm4iwbsp2bk3a6pa | oci-mad-ot-drgattach-vnet-mw-pro | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaltnhtbmnk6pfxzsgd5byzmtmf5w3rwmdnnz5xi2chintm5ifwqaa"></a>
| ID                                                                                                | Nombre                     | Servicios              | Estado    |
|:--------------------------------------------------------------------------------------------------|:---------------------------|:-----------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaaltnhtbmnk6pfxzsgd5byzmtmf5w3rwmdnnz5xi2chintm5ifwqaa | oci-mad-ot-vngw-svc-mw-pro | OCI MAD Object Storage | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqackqoptlccngvmili6wlwhuwnkeiyb3lbbmmbkyp7ql4a"></a>
#### Recursos de VCN: oci-mad-it-vnet-mw-pro (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqackqoptlccngvmili6wlwhuwnkeiyb3lbbmmbkyp7ql4a)

##### Subnets

| ID                                                                                        | Nombre                       | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                      | Route Table ID                                                                                | Security Lists                                                                                                                |
|:------------------------------------------------------------------------------------------|:-----------------------------|:---------------|:-----------------|:----------|:----------|:---------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaa6n4akwpqc2stg2ggvvfo3bfsewpigl6xoe6mixhrfn7x47benqfq | oci-mad-it-snet-mw-back-pro  | 10.201.1.96/27 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-mw-back-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaha3xj3z5wxs3om65lh62ozn24lzavab2flhibrxcusqsycwfpdgq)  | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaha3xj3z5wxs3om65lh62ozn24lzavab2flhibrxcusqsycwfpdgq | [oci-mad-it-sl-mw-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa44zqsdve5jh3aj2zrtxlhroyxtthvsk7e653f73novx5fpsn2bya) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaamhcw63rnl7i4ijszctq6etjw4tq3ai5jpgetguto2ryb4uuzt3ia | oci-mad-it-snet-mw-front-pro | 10.201.1.64/28 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-mw-front-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaltqiphurrnxlxf4ecpp3awxsmpg37d5c3buswsccosgba7iowo6a) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaltqiphurrnxlxf4ecpp3awxsmpg37d5c3buswsccosgba7iowo6a | [oci-mad-it-sl-mw-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa44zqsdve5jh3aj2zrtxlhroyxtthvsk7e653f73novx5fpsn2bya) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaha3xj3z5wxs3om65lh62ozn24lzavab2flhibrxcusqsycwfpdgq"></a>
###### oci-mad-it-udr-mw-back-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaha3xj3z5wxs3om65lh62ozn24lzavab2flhibrxcusqsycwfpdgq)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción                                                                          |
|:----------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:-------------------------------------------------------------------------------------|
| 0.0.0.0/0             | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |                                                                                      |
| oci-mad-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaad6sgbzebxid43sbmz6jypfprenbxhjhrtqgxzgztpthgfsoimiha) | Service Gateway   | The run command needs acces to object storage when the script is stored in a abucket |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaltqiphurrnxlxf4ecpp3awxsmpg37d5c3buswsccosgba7iowo6a"></a>
###### oci-mad-it-udr-mw-front-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaltqiphurrnxlxf4ecpp3awxsmpg37d5c3buswsccosgba7iowo6a)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                     | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa4uuo5b2zry5tlfifdhp2oae4oixraraoxg3s6fxpckuset2pftda"></a>
###### Default Route Table for oci-mad-it-vnet-mw-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa4uuo5b2zry5tlfifdhp2oae4oixraraoxg3s6fxpckuset2pftda)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa44zqsdve5jh3aj2zrtxlhroyxtthvsk7e653f73novx5fpsn2bya"></a>
###### oci-mad-it-sl-mw-pro-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa44zqsdve5jh3aj2zrtxlhroyxtthvsk7e653f73novx5fpsn2bya)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción                                      |
|:-----------|:-----------------|:------------|:------------|:-------------------------------------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 5556-5556   | Node Manager Port                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8393-8393   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8888-8888   | ohs forms                                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2048-2050   | traffic for ports: 2048-2050 nfs tcp             |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2370-2370   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7105-7106   | control-m server                                 |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup                                     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                                                  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2368-2368   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8443-8443   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 17000-17040 | reports                                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 13080-13120 | control-m                                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3900-3900   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup                                     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8002-8002   | wls admin                                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8743-8743   | siada                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 111-111     | traffic for ports: 111 nfs tcp                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2372-2380   | control-m                                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 9001-9004   | wls managed forms and reports                    |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 18080-18080 | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7777-7777   | ohs plain port                                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8081-8081   | siada                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8745-8745   | redef                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 12181-12181 | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6005-6005   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8007-8007   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8543-8543   | forms                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2925-2925   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 19092-19092 | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7001-7001   | wls admin                                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2369-2369   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup                                     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8744-8744   | silicie                                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8080-8083   | tomcats http for specific endpoints (db, devops) |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8544-8544   | test reports                                     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8084-8084   | siada                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 111-111     | traffic for ports: 111 nfs tcp                   |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping                                             |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 2048-2050   | traffic for ports: 2048-2050 nfs tcp             |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaak3jbmviwktuvndspeny3aflgomhlmzdfsb6ttjotoddu4gfavwta"></a>
###### Default Security List for oci-mad-it-vnet-mw-pro (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaak3jbmviwktuvndspeny3aflgomhlmzdfsb6ttjotoddu4gfavwta)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.1.64/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                           | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaakhhqfyumjp5ywzx3y4pj2kvdwbmbl343yr2tqez642owgebiwvmq | oci-mad-it-drgattach-vnet-mw-pro | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaad6sgbzebxid43sbmz6jypfprenbxhjhrtqgxzgztpthgfsoimiha"></a>
| ID                                                                                                | Nombre                     | Servicios              | Estado    |
|:--------------------------------------------------------------------------------------------------|:---------------------------|:-----------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaad6sgbzebxid43sbmz6jypfprenbxhjhrtqgxzgztpthgfsoimiha | oci-mad-it-vngw-svc-mw-pro | OCI MAD Object Storage | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqa73te6izbug6ojlzmgoy4uam7ny2c3j7cuqits6ux3swq"></a>
#### Recursos de VCN: oci-mad-ot-vnet-db-pro (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqa73te6izbug6ojlzmgoy4uam7ny2c3j7cuqits6ux3swq)

##### Subnets

| ID                                                                                        | Nombre                     | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                    | Route Table ID                                                                                | Security Lists                                                                                                                |
|:------------------------------------------------------------------------------------------|:---------------------------|:----------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaap6f7rjmrio2jegdk25f4wugaitds6lu3mkkwokeu2pxj6pe7thwq | oci-mad-ot-snet-db-svc-pro | 10.201.0.192/27 | Regional         | No        | AVAILABLE | [oci-mad-ot-udr-db-svc-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaapllqnnr54dmgg2ltwsbremd4rrybdx3hjmziu3d7e3kcc6e5eoqq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaapllqnnr54dmgg2ltwsbremd4rrybdx3hjmziu3d7e3kcc6e5eoqq | [oci-mad-ot-sl-db-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaeuhntcn2qbpegl4jd4bcobsxqtpkua2r35hw5f3wsoy3z4fvdvna) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaadxpkyv5qmzew4qlqnd4xv3we3mgtdd3mpvowqunuvjyplweqgpq | oci-mad-ot-snet-db-bck-pro | 10.201.0.224/28 | Regional         | No        | AVAILABLE | [oci-mad-ot-udr-db-bck-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaasmygb3llozzcm4yl2lfa6tpid4ueegcc37r4hnejmvis6llm6gva) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaasmygb3llozzcm4yl2lfa6tpid4ueegcc37r4hnejmvis6llm6gva | [oci-mad-ot-sl-db-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaeuhntcn2qbpegl4jd4bcobsxqtpkua2r35hw5f3wsoy3z4fvdvna) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaapllqnnr54dmgg2ltwsbremd4rrybdx3hjmziu3d7e3kcc6e5eoqq"></a>
###### oci-mad-ot-udr-db-svc-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaapllqnnr54dmgg2ltwsbremd4rrybdx3hjmziu3d7e3kcc6e5eoqq)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-mad-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaadu2ymgpzxrewzdcwxvbelrb7tiw3sfdkhjbd52iw3eu6fhwca7fq) | Service Gateway   |               |
| 0.0.0.0/0             | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaasmygb3llozzcm4yl2lfa6tpid4ueegcc37r4hnejmvis6llm6gva"></a>
###### oci-mad-ot-udr-db-bck-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaasmygb3llozzcm4yl2lfa6tpid4ueegcc37r4hnejmvis6llm6gva)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-mad-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaadu2ymgpzxrewzdcwxvbelrb7tiw3sfdkhjbd52iw3eu6fhwca7fq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaot3iiqcobksy6262prppywubhbsk77bk3q2c4rwwu4ci46byhtza"></a>
###### Default Route Table for oci-mad-ot-vnet-db-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaot3iiqcobksy6262prppywubhbsk77bk3q2c4rwwu4ci46byhtza)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaeuhntcn2qbpegl4jd4bcobsxqtpkua2r35hw5f3wsoy3z4fvdvna"></a>
###### oci-mad-ot-sl-db-pro-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaeuhntcn2qbpegl4jd4bcobsxqtpkua2r35hw5f3wsoy3z4fvdvna)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción                 |
|:-----------|:-----------------|:------------|:------------|:----------------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 3370-3370   | control-m                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                             |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 4370-4370   | control-m                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3772-3772   |                             |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 52311-52311 | besclient                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 1363-1363   | connect direct              |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 1363-1363   | connect direct              |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2484-2484   | Autonomous Recovery Service |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8005-8005   | Autonomous Recovery Service |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup                |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa3aavdx33r2iesbhyc5sktsrgqk5qpgpbpws3zepliqnavsemkrxa"></a>
###### Default Security List for oci-mad-ot-vnet-db-pro (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa3aavdx33r2iesbhyc5sktsrgqk5qpgpbpws3zepliqnavsemkrxa)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.0.192/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                           | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaahza2zuwsm7hxhnf74fthol2wl6j7jjen7iw4nnugvqlblpn5t3yq | oci-mad-ot-drgattach-vnet-db-pro | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaadu2ymgpzxrewzdcwxvbelrb7tiw3sfdkhjbd52iw3eu6fhwca7fq"></a>
| ID                                                                                                | Nombre                  | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaadu2ymgpzxrewzdcwxvbelrb7tiw3sfdkhjbd52iw3eu6fhwca7fq | oci-mad-ot-vngw-svc-pro | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqamdoeypz2ypqsxray72wtx4didpbigg5xnguflaikxxwq"></a>
#### Recursos de VCN: oci-mad-it-vnet-db-pro (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqamdoeypz2ypqsxray72wtx4didpbigg5xnguflaikxxwq)

##### Subnets

| ID                                                                                        | Nombre                     | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                    | Route Table ID                                                                                | Security Lists                                                                                                                |
|:------------------------------------------------------------------------------------------|:---------------------------|:---------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaal3yel3inaijsorqmrt4bxnackebjjgapqwomcbgpqagrgzkcildq | oci-mad-it-snet-db-svc-pro | 10.201.0.64/27 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-db-svc-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaanau5papcbk6ni2rrieva3y744y2gjhg54tfyby4en3jy5q2yt6lq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaanau5papcbk6ni2rrieva3y744y2gjhg54tfyby4en3jy5q2yt6lq | [oci-mad-it-sl-db-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaapnez27sqllvoogwg5frxl5fsde22qsx47e3i37muq5iiivd6vvfq) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaavq5dlejratkj4x5nrlm26ljsri2u7bxjb3voxcrn6bvzdyrvte5q | oci-mad-it-snet-db-bck-pro | 10.201.0.96/28 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-db-bck-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaashwsmt7lvb6olp3hmu4ufjfv3pwjquco7ixspmadkigd3t3nwinq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaashwsmt7lvb6olp3hmu4ufjfv3pwjquco7ixspmadkigd3t3nwinq | [oci-mad-it-sl-db-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaapnez27sqllvoogwg5frxl5fsde22qsx47e3i37muq5iiivd6vvfq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaanau5papcbk6ni2rrieva3y744y2gjhg54tfyby4en3jy5q2yt6lq"></a>
###### oci-mad-it-udr-db-svc-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaanau5papcbk6ni2rrieva3y744y2gjhg54tfyby4en3jy5q2yt6lq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |
| all-mad-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaggc65el6qljl4xcx677xargvy55fkamfnpv4lvis6m3tn4ojjecq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaashwsmt7lvb6olp3hmu4ufjfv3pwjquco7ixspmadkigd3t3nwinq"></a>
###### oci-mad-it-udr-db-bck-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaashwsmt7lvb6olp3hmu4ufjfv3pwjquco7ixspmadkigd3t3nwinq)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-mad-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaggc65el6qljl4xcx677xargvy55fkamfnpv4lvis6m3tn4ojjecq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaazocikxyqjisah4d66bebfmmksm3adoxgsswld7uyfesfjizx6m3q"></a>
###### Default Route Table for oci-mad-it-vnet-db-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaazocikxyqjisah4d66bebfmmksm3adoxgsswld7uyfesfjizx6m3q)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaapnez27sqllvoogwg5frxl5fsde22qsx47e3i37muq5iiivd6vvfq"></a>
###### oci-mad-it-sl-db-pro-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaapnez27sqllvoogwg5frxl5fsde22qsx47e3i37muq5iiivd6vvfq)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos     | Descripción                          |
|:---------------|:-----------------|:------------|:------------|:-------------------------------------|
| 10.0.0.0/8     | CIDR_BLOCK       | UDP         | 3370-3370   | control-m                            |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 22-22       |                                      |
| 10.0.0.0/8     | CIDR_BLOCK       | UDP         | 4370-4370   | control-m                            |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 52311-52311 | besclient                            |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 1363-1364   | connect direct                       |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 3771-3771   | db listener                          |
| 10.0.0.0/8     | CIDR_BLOCK       | ICMP        |             | ping                                 |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 2484-2484   | Autonomous Recovery Service          |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 8005-8005   | Autonomous Recovery Service          |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 7106-7106   | control-m                            |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 20-21       | FTP de Aviación y de Tierra          |
| 10.201.0.64/27 | CIDR_BLOCK       | UDP         | 111-111     | Temporal rule for database migration |
| 10.201.0.64/27 | CIDR_BLOCK       | UDP         | 2048-2048   | Temporal rule for database migration |
| 10.201.0.64/27 | CIDR_BLOCK       | TCP         | 111-111     | Temporal rule for database migration |
| 10.201.0.64/27 | CIDR_BLOCK       | TCP         | 2048-2048   | Temporal rule for database migration |
| 10.201.0.64/27 | CIDR_BLOCK       | TCP         | 2049-2049   | Temporal rule for database migration |
| 10.201.0.64/27 | CIDR_BLOCK       | TCP         | 2050-2050   | Temporal rule for database migration |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup                         |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup                         |
| 10.0.0.0/8     | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup                         |
| 10.0.0.0/8     | CIDR_BLOCK       | UDP         | 52311-52311 | besclient                            |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa5hddvwmls7cm57dy6nvyhsewuipterxvophqfq2mmt3mpsyxvddq"></a>
###### Default Security List for oci-mad-it-vnet-db-pro (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa5hddvwmls7cm57dy6nvyhsewuipterxvophqfq2mmt3mpsyxvddq)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.0.64/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                           | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaayzx3vmqwmwgiwjzrbbzh346pgcpjs2fyedngefczuxzes4ahn2bq | oci-mad-it-drgattach-vnet-db-pro | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaggc65el6qljl4xcx677xargvy55fkamfnpv4lvis6m3tn4ojjecq"></a>
| ID                                                                                                | Nombre                     | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:---------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaaggc65el6qljl4xcx677xargvy55fkamfnpv4lvis6m3tn4ojjecq | oci-mad-it-vngw-svc-db-pro | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqae3yvzexhcz7rlk2cr6znmvntybpmvnl5ve6syoci5b6a"></a>
#### Recursos de VCN: oci-mad-it-vnet-tools-pro (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqae3yvzexhcz7rlk2cr6znmvntybpmvnl5ve6syoci5b6a)

##### Subnets

| ID                                                                                        | Nombre                    | CIDR          | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                   | Route Table ID                                                                                | Security Lists                                                                                                                   |
|:------------------------------------------------------------------------------------------|:--------------------------|:--------------|:-----------------|:----------|:----------|:------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaaytgjvxkped2extldxpdbhuuzf3drnylfifgcqchlf5cyjnvcdfq | oci-mad-it-snet-tools-pro | 10.201.6.0/26 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-tools-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa77qzsbio6gqpzqadxchaeiwfjiyg2orm6tcth5stnq5fnzkm2bra) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa77qzsbio6gqpzqadxchaeiwfjiyg2orm6tcth5stnq5fnzkm2bra | [oci-mad-it-sl-tools-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaay6yvilqokrmmp2hik3dagwjdwixvhh7atr64bvl6nbyq6thtoxua) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa77qzsbio6gqpzqadxchaeiwfjiyg2orm6tcth5stnq5fnzkm2bra"></a>
###### oci-mad-it-udr-tools-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa77qzsbio6gqpzqadxchaeiwfjiyg2orm6tcth5stnq5fnzkm2bra)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                     | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaw2qzrgwzowgytijuicz5mgpuva2qa4g5jxwosufgqfll56u5dvsq"></a>
###### Default Route Table for oci-mad-it-vnet-tools-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaw2qzrgwzowgytijuicz5mgpuva2qa4g5jxwosufgqfll56u5dvsq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaay6yvilqokrmmp2hik3dagwjdwixvhh7atr64bvl6nbyq6thtoxua"></a>
###### oci-mad-it-sl-tools-pro-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaay6yvilqokrmmp2hik3dagwjdwixvhh7atr64bvl6nbyq6thtoxua)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción                                               |
|:-----------|:-----------------|:------------|:----------|:----------------------------------------------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22     |                                                           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3771-3771 |                                                           |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping                                                      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3000-3000 |                                                           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8001-8001 | fwviewer-app deployed in maditvmtoolspro1 as docker image |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa5bp4favb6luywlwdi5huia2i3rjoqmhihlketext5dskdwguulnq"></a>
###### Default Security List for oci-mad-it-vnet-tools-pro (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa5bp4favb6luywlwdi5huia2i3rjoqmhihlketext5dskdwguulnq)

####### Reglas de Entrada

| Origen        | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:--------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0     | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0     | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.6.0/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                              | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaa25p7ko4dfujvmwra7kw244ze6tdqqkn236quyxojjqhqakuwh7fq | oci-mad-it-drgattach-vnet-tools-pro | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqasx3pjyo3ns26o6kcscd6k6ra5i2po37b67pohyq2rnda"></a>
#### Recursos de VCN: oci-mad-it-vnet-vdi-customers-pro (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqasx3pjyo3ns26o6kcscd6k6ra5i2po37b67pohyq2rnda)

##### Subnets

| ID                                                                                        | Nombre                            | CIDR          | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                           | Route Table ID                                                                                | Security Lists                                                                                                                           |
|:------------------------------------------------------------------------------------------|:----------------------------------|:--------------|:-----------------|:----------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaagglsxmjnekfabmzu2filubw3fjcarm6mypbe47lzimg4c2jcyb2a | oci-mad-it-snet-vdi-customers-pro | 10.201.4.0/23 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-vdi-customers-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaafck6kgva6u4ra2wdrb3adm6ojohwdb2v3tglod4lxeigqkwezqlq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaafck6kgva6u4ra2wdrb3adm6ojohwdb2v3tglod4lxeigqkwezqlq | [oci-mad-it-sl-vdi-customers-pro-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa4ktuzjb7icvuxezy5ij54234gtyph45ia3vgecn6e3r3na3qbbaa) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaafck6kgva6u4ra2wdrb3adm6ojohwdb2v3tglod4lxeigqkwezqlq"></a>
###### oci-mad-it-udr-vdi-customers-pro (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaafck6kgva6u4ra2wdrb3adm6ojohwdb2v3tglod4lxeigqkwezqlq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |
| all-mad-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaa3j6tc3tboz2q2xswwyq6rl4btfdanwcghhp5v7gvhjiu2uigk5mq) | Service Gateway   |               |

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa4ktuzjb7icvuxezy5ij54234gtyph45ia3vgecn6e3r3na3qbbaa"></a>
###### oci-mad-it-sl-vdi-customers-pro-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa4ktuzjb7icvuxezy5ij54234gtyph45ia3vgecn6e3r3na3qbbaa)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0  | CIDR_BLOCK       | TCP         | 3389-3389 |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                                      | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:--------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaal434djl4dubzmzjchx5dijmw3ueqmfnjfr5al5nax7qjlxqeex7q | oci-mad-it-drgattach-vnet-vdi-customers-pro | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaa3j6tc3tboz2q2xswwyq6rl4btfdanwcghhp5v7gvhjiu2uigk5mq"></a>
| ID                                                                                                | Nombre                            | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:----------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaa3j6tc3tboz2q2xswwyq6rl4btfdanwcghhp5v7gvhjiu2uigk5mq | oci-mad-it-vngw-svc-customers-pro | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaojnh3jumgng25plrbx5fqpxc3hvebmu3tk3exvtbm6pq"></a>
#### Recursos de VCN: oci-mad-it-vnet-tools-stg (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaojnh3jumgng25plrbx5fqpxc3hvebmu3tk3exvtbm6pq)

##### Subnets

| ID                                                                                        | Nombre                    | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                   | Route Table ID                                                                                | Security Lists                                                                                                                   |
|:------------------------------------------------------------------------------------------|:--------------------------|:---------------|:-----------------|:----------|:----------|:------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaa7thznnv366notsb2ypc2222km4i66npp3rmps3s2ekppyjvydopq | oci-mad-it-snet-tools-stg | 10.201.6.64/26 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-tools-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaahhvmvowzc4glehvrqwodpckh7dtpxyo4uyy2gmrsya3damz3fvq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaahhvmvowzc4glehvrqwodpckh7dtpxyo4uyy2gmrsya3damz3fvq | [oci-mad-it-sl-tools-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaaetdxbxqbvnbhrviqdhk2win63xxktp57is6afmeuh3wlie4pz7q) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaahhvmvowzc4glehvrqwodpckh7dtpxyo4uyy2gmrsya3damz3fvq"></a>
###### oci-mad-it-udr-tools-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaahhvmvowzc4glehvrqwodpckh7dtpxyo4uyy2gmrsya3damz3fvq)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                     | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaahdgr75zgn6dnkphyljgpbgs2mdly6c3emi2xv4zmn5o3jy5teeca"></a>
###### Default Route Table for oci-mad-it-vnet-tools-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaahdgr75zgn6dnkphyljgpbgs2mdly6c3emi2xv4zmn5o3jy5teeca)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaaetdxbxqbvnbhrviqdhk2win63xxktp57is6afmeuh3wlie4pz7q"></a>
###### oci-mad-it-sl-tools-stg-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaaetdxbxqbvnbhrviqdhk2win63xxktp57is6afmeuh3wlie4pz7q)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22     |               |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3761-3761 |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaqdvtjekxm3zlglxuob2dbbwpvt46dtw7w3k3xkikjmbaxqe4qjva"></a>
###### Default Security List for oci-mad-it-vnet-tools-stg (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaqdvtjekxm3zlglxuob2dbbwpvt46dtw7w3k3xkikjmbaxqe4qjva)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.6.64/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                              | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaaufrkc4ywqutzi3zuz53uavh7mcfjnl7elvpxgvpurlaifmy7epvq | oci-mad-it-drgattach-vnet-tools-stg | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqawax7byicjrczregt6kkxorhklmebgbg33thaulnwzq4q"></a>
#### Recursos de VCN: oci-mad-it-vnet-db-stg (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqawax7byicjrczregt6kkxorhklmebgbg33thaulnwzq4q)

##### Subnets

| ID                                                                                        | Nombre                     | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                    | Route Table ID                                                                                | Security Lists                                                                                                                |
|:------------------------------------------------------------------------------------------|:---------------------------|:----------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaop5p27w7rhgmx7yxh7bkcbtfrgat6frwd5kgqojgdjjkqdkwxvja | oci-mad-it-snet-db-svc-stg | 10.201.0.128/27 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-db-svc-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaagktcnyaxpt42g27jylgtd5p5mma73gzxrcwyk3zsxue4y43lgvwq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaagktcnyaxpt42g27jylgtd5p5mma73gzxrcwyk3zsxue4y43lgvwq | [oci-mad-it-sl-db-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa66sl57wxheoi5zbigcqxgo3cyxjg7f5j4pjqutzzffdrktdv7l4q) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaa56jy2gcsj43sxxijdlofdg6bxdr7ik7h6ho22yun7vuzww45lchq | oci-mad-it-snet-db-bck-stg | 10.201.0.160/28 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-db-bck-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaanex4srlnqk7sidsk24a4kn656yjrqnpnltbb3wt5msl7xqmum6zq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaanex4srlnqk7sidsk24a4kn656yjrqnpnltbb3wt5msl7xqmum6zq | [oci-mad-it-sl-db-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa66sl57wxheoi5zbigcqxgo3cyxjg7f5j4pjqutzzffdrktdv7l4q) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaagktcnyaxpt42g27jylgtd5p5mma73gzxrcwyk3zsxue4y43lgvwq"></a>
###### oci-mad-it-udr-db-svc-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaagktcnyaxpt42g27jylgtd5p5mma73gzxrcwyk3zsxue4y43lgvwq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |
| all-mad-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaabndgxu42daiyl2upnz7qqeb7pom37cwr6l5cisdrsjxwc6pyrhqq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaanex4srlnqk7sidsk24a4kn656yjrqnpnltbb3wt5msl7xqmum6zq"></a>
###### oci-mad-it-udr-db-bck-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaanex4srlnqk7sidsk24a4kn656yjrqnpnltbb3wt5msl7xqmum6zq)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-mad-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaabndgxu42daiyl2upnz7qqeb7pom37cwr6l5cisdrsjxwc6pyrhqq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaajydvxg7m67fa2zawwmqegaban44crkgorrer5ra653uyxhjleima"></a>
###### Default Route Table for oci-mad-it-vnet-db-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaajydvxg7m67fa2zawwmqegaban44crkgorrer5ra653uyxhjleima)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa66sl57wxheoi5zbigcqxgo3cyxjg7f5j4pjqutzzffdrktdv7l4q"></a>
###### oci-mad-it-sl-db-stg-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa66sl57wxheoi5zbigcqxgo3cyxjg7f5j4pjqutzzffdrktdv7l4q)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos     | Descripción                          |
|:----------------|:-----------------|:------------|:------------|:-------------------------------------|
| 10.201.0.128/27 | CIDR_BLOCK       | UDP         | 111-111     | Temporal rule for database migration |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 1363-1364   | connect direct                       |
| 10.0.0.0/8      | CIDR_BLOCK       | UDP         | 52311-52311 | besclient                            |
| 10.201.0.128/27 | CIDR_BLOCK       | TCP         | 111-111     | Temporal rule for database migration |
| 10.201.0.128/27 | CIDR_BLOCK       | UDP         | 2048-2048   | Temporal rule for database migration |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 22-22       |                                      |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 52311-52311 | besclient                            |
| 10.201.0.128/27 | CIDR_BLOCK       | TCP         | 2049-2049   | Temporal rule for database migration |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 3761-3761   | db listener                          |
| 10.0.0.0/8      | CIDR_BLOCK       | UDP         | 1363-1363   | connect direct                       |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 7106-7106   | control-m                            |
| 10.201.0.128/27 | CIDR_BLOCK       | TCP         | 2050-2050   | Temporal rule for database migration |
| 10.201.0.128/27 | CIDR_BLOCK       | TCP         | 2048-2048   | Temporal rule for database migration |
| 10.0.0.0/8      | CIDR_BLOCK       | ICMP        |             | ping                                 |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 20-21       | FTP de Aviación y de Tierra          |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup                         |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup                         |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup                         |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaapuiyh4qyiz2rqjn26iiq2d6yrest53hw6x4mldqc3kkfmdwwhmpq"></a>
###### Default Security List for oci-mad-it-vnet-db-stg (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaapuiyh4qyiz2rqjn26iiq2d6yrest53hw6x4mldqc3kkfmdwwhmpq)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.0.128/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                           | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaapojss67qfz2apmm2ckrchxqped6hczl6r6y6boaaa2e57wzbvefq | oci-mad-it-drgattach-vnet-db-stg | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaabndgxu42daiyl2upnz7qqeb7pom37cwr6l5cisdrsjxwc6pyrhqq"></a>
| ID                                                                                                | Nombre                     | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:---------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaabndgxu42daiyl2upnz7qqeb7pom37cwr6l5cisdrsjxwc6pyrhqq | oci-mad-it-vngw-svc-db-stg | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqartv6joutkh6ca6bm5mfvt543fgjal2oqzk36ek7lnqxa"></a>
#### Recursos de VCN: oci-mad-ot-vnet-db-stg (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqartv6joutkh6ca6bm5mfvt543fgjal2oqzk36ek7lnqxa)

##### Subnets

| ID                                                                                        | Nombre                     | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                    | Route Table ID                                                                                | Security Lists                                                                                                                |
|:------------------------------------------------------------------------------------------|:---------------------------|:---------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaanwuw7ks63ozoejekkj6u24ab2tjemb3k6kyzrmpmt7jjfumq46la | oci-mad-ot-snet-db-svc-stg | 10.201.1.0/27  | Regional         | No        | AVAILABLE | [oci-mad-ot-udr-db-svc-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaittu3mhqidw5qtum6i7lmt6ely6ww4wmchr4ikrvrsfa65ewao3a) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaittu3mhqidw5qtum6i7lmt6ely6ww4wmchr4ikrvrsfa65ewao3a | [oci-mad-ot-sl-db-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaauyj4ms7n57w2we7fjo5tiaex7chjtbyadrm3222bvkectvycwa4q) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaanz5ssfzuo7dhcurqd4punqmw4hwub2pqrboedhfbn3xzmqgfwrq | oci-mad-ot-snet-db-bck-stg | 10.201.1.32/28 | Regional         | No        | AVAILABLE | [oci-mad-ot-udr-db-bck-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaanzcin3snpwmikewrjmu5xqmvisrxf7uloqne4b5qtfxhkb6bl55a) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaanzcin3snpwmikewrjmu5xqmvisrxf7uloqne4b5qtfxhkb6bl55a | [oci-mad-ot-sl-db-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaauyj4ms7n57w2we7fjo5tiaex7chjtbyadrm3222bvkectvycwa4q) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaittu3mhqidw5qtum6i7lmt6ely6ww4wmchr4ikrvrsfa65ewao3a"></a>
###### oci-mad-ot-udr-db-svc-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaittu3mhqidw5qtum6i7lmt6ely6ww4wmchr4ikrvrsfa65ewao3a)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-mad-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaxhpj7pisqjbdfbncym3mbxsodgzigy2lnmhm22hbnqqgmjkvmlja) | Service Gateway   |               |
| 0.0.0.0/0             | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                        | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaanzcin3snpwmikewrjmu5xqmvisrxf7uloqne4b5qtfxhkb6bl55a"></a>
###### oci-mad-ot-udr-db-bck-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaanzcin3snpwmikewrjmu5xqmvisrxf7uloqne4b5qtfxhkb6bl55a)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                            | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-mad-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaxhpj7pisqjbdfbncym3mbxsodgzigy2lnmhm22hbnqqgmjkvmlja) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaylceyloxffsfytuazuwbnr2dlvkzvpv4tunosclxljn3ahvxpquq"></a>
###### Default Route Table for oci-mad-ot-vnet-db-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaylceyloxffsfytuazuwbnr2dlvkzvpv4tunosclxljn3ahvxpquq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaauyj4ms7n57w2we7fjo5tiaex7chjtbyadrm3222bvkectvycwa4q"></a>
###### oci-mad-ot-sl-db-stg-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaauyj4ms7n57w2we7fjo5tiaex7chjtbyadrm3222bvkectvycwa4q)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción    |
|:-----------|:-----------------|:------------|:------------|:---------------|
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 3370-3370   | control-m      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 4370-4370   | control-m      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 52311-52311 | besclient      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 1363-1363   | connect direct |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3762-3762   | db listener    |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 1363-1363   | connect direct |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup   |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaiemgt733b6xwsk6k3aqdobdv5fjemlkr57ga4rrwvnrr2pwb665q"></a>
###### Default Security List for oci-mad-ot-vnet-db-stg (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaiemgt733b6xwsk6k3aqdobdv5fjemlkr57ga4rrwvnrr2pwb665q)

####### Reglas de Entrada

| Origen        | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:--------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0     | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0     | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.1.0/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                           | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaavqmpchmmc6kyk5eslho677uh7cdp24vm7b4t6nddxv2yjfn53aia | oci-mad-ot-drgattach-vnet-db-stg | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaxhpj7pisqjbdfbncym3mbxsodgzigy2lnmhm22hbnqqgmjkvmlja"></a>
| ID                                                                                                | Nombre                     | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:---------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaaxhpj7pisqjbdfbncym3mbxsodgzigy2lnmhm22hbnqqgmjkvmlja | oci-mad-ot-vngw-svc-db-stg | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqatnwllzc5fjv26vtxa3xi3ejkmdsjgrmgfjmsk2t4t2da"></a>
#### Recursos de VCN: oci-mad-it-vnet-mw-stg (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqatnwllzc5fjv26vtxa3xi3ejkmdsjgrmgfjmsk2t4t2da)

##### Subnets

| ID                                                                                        | Nombre                       | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                      | Route Table ID                                                                                | Security Lists                                                                                                                |
|:------------------------------------------------------------------------------------------|:-----------------------------|:----------------|:-----------------|:----------|:----------|:---------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaadkmm6pkksh6ysowcpis2xhow2myqwl3tiiw2lddlvxeklcn7ghcq | oci-mad-it-snet-mw-back-stg  | 10.201.1.144/28 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-mw-back-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa547ruvosigjckhgpwzjl34wegp7e63hr5zr3khbcvrjdfl4lnuqa)  | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa547ruvosigjckhgpwzjl34wegp7e63hr5zr3khbcvrjdfl4lnuqa | [oci-mad-it-sl-mw-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaal6rv3zlt5eqqytzeoitzg5wbiyw5asocfitd23rtt5bbdtzp4ota) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaghjh5zsrocksf53o2qphaqygu7cbw67p2mgasifhpw27jk2krvya | oci-mad-it-snet-mw-front-stg | 10.201.1.128/28 | Regional         | No        | AVAILABLE | [oci-mad-it-udr-mw-front-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaqjizydyb3vr3xle3l37cqj4dfv6sr43qou4ebeqeciedzke3hk6a) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaqjizydyb3vr3xle3l37cqj4dfv6sr43qou4ebeqeciedzke3hk6a | [oci-mad-it-sl-mw-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaal6rv3zlt5eqqytzeoitzg5wbiyw5asocfitd23rtt5bbdtzp4ota) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa547ruvosigjckhgpwzjl34wegp7e63hr5zr3khbcvrjdfl4lnuqa"></a>
###### oci-mad-it-udr-mw-back-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa547ruvosigjckhgpwzjl34wegp7e63hr5zr3khbcvrjdfl4lnuqa)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                     | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaqjizydyb3vr3xle3l37cqj4dfv6sr43qou4ebeqeciedzke3hk6a"></a>
###### oci-mad-it-udr-mw-front-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaqjizydyb3vr3xle3l37cqj4dfv6sr43qou4ebeqeciedzke3hk6a)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                     | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaav6yhngvxxbcc7itlij65sigdabxxe7lsd6lbbgni2xskekunstla"></a>
###### Default Route Table for oci-mad-it-vnet-mw-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaav6yhngvxxbcc7itlij65sigdabxxe7lsd6lbbgni2xskekunstla)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaal6rv3zlt5eqqytzeoitzg5wbiyw5asocfitd23rtt5bbdtzp4ota"></a>
###### oci-mad-it-sl-mw-stg-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaal6rv3zlt5eqqytzeoitzg5wbiyw5asocfitd23rtt5bbdtzp4ota)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción                    |
|:-----------|:-----------------|:------------|:------------|:-------------------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8393-8393   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2370-2370   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6005-6005   | control-m prod a control-m stg |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2368-2368   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6080-6080   | redef dev                      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8443-8443   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 17000-17040 | reports                        |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 33434-33689 | traceroute                     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 9002-9002   | wls managed reports            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6743-6743   |                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6745-6745   | dsilicieredef                  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3900-3900   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 18080-18080 | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 1000-1050   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 12181-12181 | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6005-6005   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8007-8007   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7777-7777   |                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8888-8888   |                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7743-7745   |                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2925-2925   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 19092-19092 | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8393-8393   | control-m prod a control-m stg |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7106-7106   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7105-7105   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 2048-2049   | nfs udp                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2369-2369   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2367-2370   | control-m prod a control-m stg |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7105-7106   | control-m server and em        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 9001-9001   | wls managed forms              |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2048-2049   | nfs tcp                        |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 111-111     | nfs udp                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7543-7543   |                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2050-2050   | nfs                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7080-7083   |                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7001-7002   | wls adminserver                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 111-111     | nfs tcp                        |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping                           |

####### Reglas de Salida

| Destino         | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK        | Todos       |           |               |
| 10.201.1.144/28 | CIDR_BLOCK        | TCP         | 7001-7001 |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaavsueosxyszgyc34zws4ocjchpdrt56bxq3jh3eur6bmc4cylomca"></a>
###### Default Security List for oci-mad-it-vnet-mw-stg (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaavsueosxyszgyc34zws4ocjchpdrt56bxq3jh3eur6bmc4cylomca)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.1.128/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                           | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaaml3ynnyv3yavsyedkmsqekmg5gou3xjd2p4yfbbxogydsmgs25ia | oci-mad-it-drgattach-vnet-mw-stg | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak3th2pjmr7nybv5kdvou2fdycfl6wialdm75vwxutcpq"></a>
#### Recursos de VCN: oci-mad-ot-vnet-mw-stg (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak3th2pjmr7nybv5kdvou2fdycfl6wialdm75vwxutcpq)

##### Subnets

| ID                                                                                        | Nombre                       | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                      | Route Table ID                                                                                | Security Lists                                                                                                                |
|:------------------------------------------------------------------------------------------|:-----------------------------|:---------------|:-----------------|:----------|:----------|:---------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaa4rb57isde32shtozl62hdpjxiwrtqrjlrftcchmuqat5ocqsqieq | oci-mad-ot-snet-mw-back-stg  | 10.201.2.16/28 | Regional         | No        | AVAILABLE | [oci-mad-ot-udr-mw-back-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaap3vkqcn6zqggmek5xfqxt3ztraevtyuyc3szq35dnznq2c6suekq)  | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaap3vkqcn6zqggmek5xfqxt3ztraevtyuyc3szq35dnznq2c6suekq | [oci-mad-ot-sl-mw-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaarucccvlob6224a22lobnhdm4pszhwuffk6qa5s36zdi74lzly74a) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaajbn6qoig3rwud4735j3n2ef6rnt4jrzd2v5eyixw4gjc7alyv75q | oci-mad-ot-snet-mw-front-stg | 10.201.2.0/28  | Regional         | No        | AVAILABLE | [oci-mad-ot-udr-mw-front-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaardrjjg6gy3fyjkio5d7p3tt2fefd7ltymidtq5sm2cakbahba3tq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaardrjjg6gy3fyjkio5d7p3tt2fefd7ltymidtq5sm2cakbahba3tq | [oci-mad-ot-sl-mw-stg-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaarucccvlob6224a22lobnhdm4pszhwuffk6qa5s36zdi74lzly74a) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaap3vkqcn6zqggmek5xfqxt3ztraevtyuyc3szq35dnznq2c6suekq"></a>
###### oci-mad-ot-udr-mw-back-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaap3vkqcn6zqggmek5xfqxt3ztraevtyuyc3szq35dnznq2c6suekq)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                     | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaardrjjg6gy3fyjkio5d7p3tt2fefd7ltymidtq5sm2cakbahba3tq"></a>
###### oci-mad-ot-udr-mw-front-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaardrjjg6gy3fyjkio5d7p3tt2fefd7ltymidtq5sm2cakbahba3tq)

No hay reglas de ruta definidas.

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaawscnkox7ctd7jfy7lc5s7tbrevi6dw6qtahjkfzngllv4njhf5eq"></a>
###### Default Route Table for oci-mad-ot-vnet-mw-stg (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaawscnkox7ctd7jfy7lc5s7tbrevi6dw6qtahjkfzngllv4njhf5eq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaarucccvlob6224a22lobnhdm4pszhwuffk6qa5s36zdi74lzly74a"></a>
###### oci-mad-ot-sl-mw-stg-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaarucccvlob6224a22lobnhdm4pszhwuffk6qa5s36zdi74lzly74a)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción       |
|:-----------|:-----------------|:------------|:----------|:------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 21-22     |                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7080-7081 | tomcats           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3389-3389 | rdp for oleoducto |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping              |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaawunqzousfuzggfjqe66ic53rqbea2txuv6qkhlkyefg3fjlekhaa"></a>
###### Default Security List for oci-mad-ot-vnet-mw-stg (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaawunqzousfuzggfjqe66ic53rqbea2txuv6qkhlkyefg3fjlekhaa)

####### Reglas de Entrada

| Origen        | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:--------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0     | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0     | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.2.0/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                           | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaang2dxq3qlhlqgzhpnei6dbqwulgrusvohkw7u2dej7ljegqzo6fq | oci-mad-ot-drgattach-vnet-mw-stg | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak3mn33cxhn3zcimaotuoxtwdw3hjcnv76g6mhfxcupiq"></a>
#### Recursos de VCN: oci-mad-vnet-hub-sha (ID: ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak3mn33cxhn3zcimaotuoxtwdw3hjcnv76g6mhfxcupiq)

##### Subnets

| ID                                                                                        | Nombre                   | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                  | Route Table ID                                                                                | Security Lists                                                                                                                                        |
|:------------------------------------------------------------------------------------------|:-------------------------|:---------------|:-----------------|:----------|:----------|:-----------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaanukqbpz62rurx45mvirmg3pq5vtqx6eintqcisk7zrsaqvwn2gsa | oci-mad-snet-hub-int-sha | 10.201.0.32/28 | Regional         | No        | AVAILABLE | [oci-mad-udr-hub-int-sha](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaafgj2m2blgizoo42jk2hzqhtxd4qoybykryr725hu3swn5ksprzjq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaafgj2m2blgizoo42jk2hzqhtxd4qoybykryr725hu3swn5ksprzjq | [oci-mad-sl-hub-int-sha-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaalqqn6klyizaqhptqhxa5lypu5mexsyglot2v6m5ei5ssz2fgt2ta)                       |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaa65vh4slqqgckcviei4adjgx236jtanz64caoebm54mzenpkgzzda | oci-mad-snet-hub-dmz-sha | 10.201.0.16/28 | Regional         | Sí        | AVAILABLE | [oci-mad-udr-hub-dmz-sha](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa2x4wq4fkjv6utqrub73d2xfasclou62aqa422zeqvcgz2tnarkuq) | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa2x4wq4fkjv6utqrub73d2xfasclou62aqa422zeqvcgz2tnarkuq | [Default Security List for oci-mad-vnet-hub-sha](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa4unhq5aum32yd3vt5f4k5lxio3grp5fay5jb2om3jel7w3vphqsa) |
| ocid1.subnet.oc1.eu-madrid-1.aaaaaaaaxnteihgp7elpoqwzobx26byaycou6bvdxqvbdpeky3esirrsqlqq | oci-mad-snet-hub-fw-sha  | 10.201.0.0/28  | Regional         | No        | AVAILABLE | [oci-mad-udr-hub-fw-sha](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa3rufuihpwzob55tnnkjxsno35qngqrpun3k7uudswdic3xkgwuva)  | ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa3rufuihpwzob55tnnkjxsno35qngqrpun3k7uudswdic3xkgwuva | [oci-mad-sl-hub-fw-all-sha-1](#sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaa7yauchsjyna7rraj26y2iwkfhfz2tmsa4usqjtgq46ugzrhxh6q)                    |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaafgj2m2blgizoo42jk2hzqhtxd4qoybykryr725hu3swn5ksprzjq"></a>
###### oci-mad-udr-hub-int-sha (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaafgj2m2blgizoo42jk2hzqhtxd4qoybykryr725hu3swn5ksprzjq)

| Destino    | Tipo de Destino   | Entidad de Red                                                                                                    | Tipo de Entidad   | Descripción   |
|:-----------|:------------------|:------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                | DRG               |               |
| 0.0.0.0/0  | CIDR_BLOCK        | [NAT Gateway](#nat-ocid1_natgateway_oc1_eu_madrid_1_aaaaaaaa2p32v6gndmeiqdoxqy42gz5hsl36epphfyottxjndputg4jc7nxa) | NAT Gateway       |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaalhmejni2npfjfh4qrwgn3cxh2eaclkcebtqand5pn2hhmiolunga"></a>
###### oci-mad-udr-hub-vngw-nat-sha (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaalhmejni2npfjfh4qrwgn3cxh2eaclkcebtqand5pn2hhmiolunga)

| Destino   | Tipo de Destino   | Entidad de Red                                                                               | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | ocid1.privateip.oc1.eu-madrid-1.abwwcljrscvxeljioy3dpkhcj7ur7xbvhepbo74dq7fvjj3w6tldbhgzdlza | Desconocido       |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaabr5zckjwevcrtesvhzy7dszflbjzirbv5zzjhgoyfdtvckgv6sq"></a>
###### oci-mad-udr-hub-vngw-inet-sha (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaabr5zckjwevcrtesvhzy7dszflbjzirbv5zzjhgoyfdtvckgv6sq)

No hay reglas de ruta definidas.

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa2x4wq4fkjv6utqrub73d2xfasclou62aqa422zeqvcgz2tnarkuq"></a>
###### oci-mad-udr-hub-dmz-sha (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa2x4wq4fkjv6utqrub73d2xfasclou62aqa422zeqvcgz2tnarkuq)

No hay reglas de ruta definidas.

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaghc2plfmy2xbwkyqamtpinjisvludndkdpcasjufzntisttkbrea"></a>
###### oci-mad-udr-hub-ingress-sha (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaaghc2plfmy2xbwkyqamtpinjisvludndkdpcasjufzntisttkbrea)

| Destino   | Tipo de Destino   | Entidad de Red                                                                               | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:---------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | ocid1.privateip.oc1.eu-madrid-1.abwwcljrscvxeljioy3dpkhcj7ur7xbvhepbo74dq7fvjj3w6tldbhgzdlza | Desconocido       |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa3rufuihpwzob55tnnkjxsno35qngqrpun3k7uudswdic3xkgwuva"></a>
###### oci-mad-udr-hub-fw-sha (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaa3rufuihpwzob55tnnkjxsno35qngqrpun3k7uudswdic3xkgwuva)

| Destino    | Tipo de Destino   | Entidad de Red                                                                                                    | Tipo de Entidad   | Descripción   |
|:-----------|:------------------|:------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0  | CIDR_BLOCK        | [NAT Gateway](#nat-ocid1_natgateway_oc1_eu_madrid_1_aaaaaaaa2p32v6gndmeiqdoxqy42gz5hsl36epphfyottxjndputg4jc7nxa) | NAT Gateway       |               |
| 10.0.0.0/8 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq)                | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaarkgtg3a76wb7qb234qlwpsignqgwv332vsjasparcjqpqb2lo7da"></a>
###### Default Route Table for oci-mad-vnet-hub-sha (ID: ocid1.routetable.oc1.eu-madrid-1.aaaaaaaarkgtg3a76wb7qb234qlwpsignqgwv332vsjasparcjqpqb2lo7da)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaalqqn6klyizaqhptqhxa5lypu5mexsyglot2v6m5ei5ssz2fgt2ta"></a>
###### oci-mad-sl-hub-int-sha-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaalqqn6klyizaqhptqhxa5lypu5mexsyglot2v6m5ei5ssz2fgt2ta)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300 | Veeam Backup  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160 | Veeam Backup  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22     | SSH           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162 | Veeam Backup  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 443-443   | Veeam Backup  |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaaa7yauchsjyna7rraj26y2iwkfhfz2tmsa4usqjtgq46ugzrhxh6q"></a>
###### oci-mad-sl-hub-fw-all-sha-1 (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaaa7yauchsjyna7rraj26y2iwkfhfz2tmsa4usqjtgq46ugzrhxh6q)

####### Reglas de Entrada

| Origen    | Tipo de Origen   | Protocolo   | Puertos   | Descripción                                                   |
|:----------|:-----------------|:------------|:----------|:--------------------------------------------------------------|
| 0.0.0.0/0 | CIDR_BLOCK       | Todos       |           | 28/5/2025 - changed to stateless according to SR 4-0000679354 |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción                                                   |
|:----------|:------------------|:------------|:----------|:--------------------------------------------------------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           | 28/5/2025 - changed to stateless according to SR 4-0000679354 |

<a id="sl-ocid1_securitylist_oc1_eu_madrid_1_aaaaaaaa4unhq5aum32yd3vt5f4k5lxio3grp5fay5jb2om3jel7w3vphqsa"></a>
###### Default Security List for oci-mad-vnet-hub-sha (ID: ocid1.securitylist.oc1.eu-madrid-1.aaaaaaaa4unhq5aum32yd3vt5f4k5lxio3grp5fay5jb2om3jel7w3vphqsa)

####### Reglas de Entrada

| Origen        | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:--------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0     | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0     | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.0.0/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                               | Nombre                    | DRG                                                                                                                   | Estado   |
|:-------------------------------------------------------------------------------------------------|:--------------------------|:----------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaalsn222vjo6oz4unra4tmtmsjuan7yf3zyjpfecy2wuulh47lvmka | oci-mad-drgattach-hub-sha | [oci-mad-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

<a id="nat-ocid1_natgateway_oc1_eu_madrid_1_aaaaaaaa2p32v6gndmeiqdoxqy42gz5hsl36epphfyottxjndputg4jc7nxa"></a>
| ID                                                                                            | Nombre                   | IP Pública      | Habilitado   | Estado    |
|:----------------------------------------------------------------------------------------------|:-------------------------|:----------------|:-------------|:----------|
| ocid1.natgateway.oc1.eu-madrid-1.aaaaaaaa2p32v6gndmeiqdoxqy42gz5hsl36epphfyottxjndputg4jc7nxa | oci-mad-vngw-nat-hub-sha | 158.179.222.222 | No           | AVAILABLE |

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_madrid_1_aaaaaaaaoijskmorvzhaaf4zlbweu5cmpuyzk6roeqyi3kx53wmfhdunqduq"></a>
| ID                                                                                                | Nombre                   | Servicios                                   | Estado    |
|:--------------------------------------------------------------------------------------------------|:-------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-madrid-1.aaaaaaaaoijskmorvzhaaf4zlbweu5cmpuyzk6roeqyi3kx53wmfhdunqduq | oci-mad-vngw-svc-hub-sha | All MAD Services In Oracle Services Network | AVAILABLE |

<a id="region-eu-madrid-1-drgs"></a>
### Dynamic Routing Gateways (DRGs)

<a id="drg-ocid1_drg_oc1_eu_madrid_1_aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq"></a>
| ID                                                                                     | Nombre                 | Compartment                                                                         | Estado    |
|:---------------------------------------------------------------------------------------|:-----------------------|:------------------------------------------------------------------------------------|:----------|
| ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | oci-mad-vngw-drg-sha-1 | ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq | AVAILABLE |

#### DRG Attachments

<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaamozmwbs6ecnzsz7lyfgfxul6qap5uzevevb3gmgqfqyatapnyjqa"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaai2qegxqm7ljrwb7iizey67rk7grmuusxzyokl5zyugnwxeoiiniq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaaokzglw4vxei3bc7m6lrjiigjjfafvgpfqn2w2zaforcm2o6rqeea"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaauau3iuhny2aluzcujgnxvhuhfuhnslzbg3h3k5jykgfnqqk3kiia"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaadqafad3na6yeckbkr4wuz6uk3imw5mqctni6gqkqbpwwerwfy4gq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaacecxf5x562g65w3vveo2acpepkdrw4wqkg6qnm4iwbsp2bk3a6pa"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaakhhqfyumjp5ywzx3y4pj2kvdwbmbl343yr2tqez642owgebiwvmq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaahza2zuwsm7hxhnf74fthol2wl6j7jjen7iw4nnugvqlblpn5t3yq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaayzx3vmqwmwgiwjzrbbzh346pgcpjs2fyedngefczuxzes4ahn2bq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaa25p7ko4dfujvmwra7kw244ze6tdqqkn236quyxojjqhqakuwh7fq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaal434djl4dubzmzjchx5dijmw3ueqmfnjfr5al5nax7qjlxqeex7q"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaaufrkc4ywqutzi3zuz53uavh7mcfjnl7elvpxgvpurlaifmy7epvq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaapojss67qfz2apmm2ckrchxqped6hczl6r6y6boaaa2e57wzbvefq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaavqmpchmmc6kyk5eslho677uh7cdp24vm7b4t6nddxv2yjfn53aia"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaaml3ynnyv3yavsyedkmsqekmg5gou3xjd2p4yfbbxogydsmgs25ia"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaang2dxq3qlhlqgzhpnei6dbqwulgrusvohkw7u2dej7ljegqzo6fq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaalsn222vjo6oz4unra4tmtmsjuan7yf3zyjpfecy2wuulh47lvmka"></a>
| ID                                                                                               | Nombre                                      | DRG ID                                                                                 | Tipo   | Recurso                                                                                | Nombre Recurso                                                                                                                   | Route Table                                                                                                                           | Compartment                                                               | Estado   |
|:-------------------------------------------------------------------------------------------------|:--------------------------------------------|:---------------------------------------------------------------------------------------|:-------|:---------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaamozmwbs6ecnzsz7lyfgfxul6qap5uzevevb3gmgqfqyatapnyjqa | oci-mad-it-drgattach-vnet-genai-dev         | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak2qmyvh2snjx47rugsmynh4tfnv6ktw2bydm2f6awtrq | [oci-mad-it-vnet-genai-dev](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak2qmyvh2snjx47rugsmynh4tfnv6ktw2bydm2f6awtrq)         | [oci-mad-udr-genai-dev](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaq6jt24iucddlsbqsk3ayu3as6a2b3h2corqvf5v2efdz53ah7vaa)            | Compartment: aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaai2qegxqm7ljrwb7iizey67rk7grmuusxzyokl5zyugnwxeoiiniq | oci-mad-it-drgattach-vnet-functions-dev     | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaav5dajjyzpfej6ryttmjodknp3f3txc6j4ob66zss2zq | [oci-mad-it-vnet-functions-dev](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaav5dajjyzpfej6ryttmjodknp3f3txc6j4ob66zss2zq)     | [oci-mad-it-udr-functions-dev](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaam5y6qlplmgbhbzwbbft3z3rhruuvwjhhdq7qgfs7hcuu546fmpvq)     | Compartment: aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaaokzglw4vxei3bc7m6lrjiigjjfafvgpfqn2w2zaforcm2o6rqeea | oci-mad-it-drgattach-vnet-forms-dev         | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaacji2lss3a6gj6mbcvmvcjiafypd2i5cm7s4mmez6x5a | [oci-mad-it-vnet-forms-dev](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaacji2lss3a6gj6mbcvmvcjiafypd2i5cm7s4mmez6x5a)         | [oci-mad-it-udr-forms-dev](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaasjiosmq672hpxj6uffdmbnbssv72ozra7a7lalnpkra3fnprzhcq)         | Compartment: aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaauau3iuhny2aluzcujgnxvhuhfuhnslzbg3h3k5jykgfnqqk3kiia | oci-mad-it-drgattach-vnet-functions-pro     | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqatr3prxqnl7stm443adrnllgt63lnwcryq4b3b7tqg22a | [oci-mad-it-vnet-functions-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqatr3prxqnl7stm443adrnllgt63lnwcryq4b3b7tqg22a)     | [oci-mad-it-udr-functions-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaalkzw4yz6ttxh4xg5iymfqqo476af46qnr2sh64mmku6zbyy6doaa)     | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaadqafad3na6yeckbkr4wuz6uk3imw5mqctni6gqkqbpwwerwfy4gq | oci-mad-it-drgattach-vnet-vdipro-pro        | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqazkakfjy63mfmjjxrtg2u7qpv2zr5rx5iczt6hgcu7sia | [oci-mad-it-vnet-vdipro-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqazkakfjy63mfmjjxrtg2u7qpv2zr5rx5iczt6hgcu7sia)        | [oci-mad-it-udr-vdipro-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaawbecmxek5pz4eecdbaodzhgrjfmuemogf2fqayettenspgc5gyaa)        | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaacecxf5x562g65w3vveo2acpepkdrw4wqkg6qnm4iwbsp2bk3a6pa | oci-mad-ot-drgattach-vnet-mw-pro            | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqad4odlbg3o4ifzh74maz5ix7bwzxg4aglladl5ivn3pqa | [oci-mad-ot-vnet-mw-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqad4odlbg3o4ifzh74maz5ix7bwzxg4aglladl5ivn3pqa)            | [oci-mad-ot-udr-mw-back-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaai6onnkaurqylsb26vvz5m3gsjnnzvc3pmy2lbce7todamn2cm4cq)       | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaakhhqfyumjp5ywzx3y4pj2kvdwbmbl343yr2tqez642owgebiwvmq | oci-mad-it-drgattach-vnet-mw-pro            | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqackqoptlccngvmili6wlwhuwnkeiyb3lbbmmbkyp7ql4a | [oci-mad-it-vnet-mw-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqackqoptlccngvmili6wlwhuwnkeiyb3lbbmmbkyp7ql4a)            | [oci-mad-it-udr-mw-back-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaha3xj3z5wxs3om65lh62ozn24lzavab2flhibrxcusqsycwfpdgq)       | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaahza2zuwsm7hxhnf74fthol2wl6j7jjen7iw4nnugvqlblpn5t3yq | oci-mad-ot-drgattach-vnet-db-pro            | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqa73te6izbug6ojlzmgoy4uam7ny2c3j7cuqits6ux3swq | [oci-mad-ot-vnet-db-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqa73te6izbug6ojlzmgoy4uam7ny2c3j7cuqits6ux3swq)            | [oci-mad-ot-udr-db-svc-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaapllqnnr54dmgg2ltwsbremd4rrybdx3hjmziu3d7e3kcc6e5eoqq)        | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaayzx3vmqwmwgiwjzrbbzh346pgcpjs2fyedngefczuxzes4ahn2bq | oci-mad-it-drgattach-vnet-db-pro            | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqamdoeypz2ypqsxray72wtx4didpbigg5xnguflaikxxwq | [oci-mad-it-vnet-db-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqamdoeypz2ypqsxray72wtx4didpbigg5xnguflaikxxwq)            | [oci-mad-it-udr-db-svc-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaanau5papcbk6ni2rrieva3y744y2gjhg54tfyby4en3jy5q2yt6lq)        | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaa25p7ko4dfujvmwra7kw244ze6tdqqkn236quyxojjqhqakuwh7fq | oci-mad-it-drgattach-vnet-tools-pro         | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqae3yvzexhcz7rlk2cr6znmvntybpmvnl5ve6syoci5b6a | [oci-mad-it-vnet-tools-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqae3yvzexhcz7rlk2cr6znmvntybpmvnl5ve6syoci5b6a)         | [oci-mad-it-udr-tools-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa77qzsbio6gqpzqadxchaeiwfjiyg2orm6tcth5stnq5fnzkm2bra)         | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaal434djl4dubzmzjchx5dijmw3ueqmfnjfr5al5nax7qjlxqeex7q | oci-mad-it-drgattach-vnet-vdi-customers-pro | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqasx3pjyo3ns26o6kcscd6k6ra5i2po37b67pohyq2rnda | [oci-mad-it-vnet-vdi-customers-pro](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqasx3pjyo3ns26o6kcscd6k6ra5i2po37b67pohyq2rnda) | [oci-mad-it-udr-vdi-customers-pro](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaafck6kgva6u4ra2wdrb3adm6ojohwdb2v3tglod4lxeigqkwezqlq) | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaaufrkc4ywqutzi3zuz53uavh7mcfjnl7elvpxgvpurlaifmy7epvq | oci-mad-it-drgattach-vnet-tools-stg         | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqaojnh3jumgng25plrbx5fqpxc3hvebmu3tk3exvtbm6pq | [oci-mad-it-vnet-tools-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqaojnh3jumgng25plrbx5fqpxc3hvebmu3tk3exvtbm6pq)         | [oci-mad-it-udr-tools-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaahhvmvowzc4glehvrqwodpckh7dtpxyo4uyy2gmrsya3damz3fvq)         | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaapojss67qfz2apmm2ckrchxqped6hczl6r6y6boaaa2e57wzbvefq | oci-mad-it-drgattach-vnet-db-stg            | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqawax7byicjrczregt6kkxorhklmebgbg33thaulnwzq4q | [oci-mad-it-vnet-db-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqawax7byicjrczregt6kkxorhklmebgbg33thaulnwzq4q)            | [oci-mad-it-udr-db-svc-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaagktcnyaxpt42g27jylgtd5p5mma73gzxrcwyk3zsxue4y43lgvwq)        | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaavqmpchmmc6kyk5eslho677uh7cdp24vm7b4t6nddxv2yjfn53aia | oci-mad-ot-drgattach-vnet-db-stg            | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqartv6joutkh6ca6bm5mfvt543fgjal2oqzk36ek7lnqxa | [oci-mad-ot-vnet-db-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqartv6joutkh6ca6bm5mfvt543fgjal2oqzk36ek7lnqxa)            | [oci-mad-ot-udr-db-svc-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaaittu3mhqidw5qtum6i7lmt6ely6ww4wmchr4ikrvrsfa65ewao3a)        | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaaml3ynnyv3yavsyedkmsqekmg5gou3xjd2p4yfbbxogydsmgs25ia | oci-mad-it-drgattach-vnet-mw-stg            | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqatnwllzc5fjv26vtxa3xi3ejkmdsjgrmgfjmsk2t4t2da | [oci-mad-it-vnet-mw-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqatnwllzc5fjv26vtxa3xi3ejkmdsjgrmgfjmsk2t4t2da)            | [oci-mad-it-udr-mw-back-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaa547ruvosigjckhgpwzjl34wegp7e63hr5zr3khbcvrjdfl4lnuqa)       | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaang2dxq3qlhlqgzhpnei6dbqwulgrusvohkw7u2dej7ljegqzo6fq | oci-mad-ot-drgattach-vnet-mw-stg            | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak3th2pjmr7nybv5kdvou2fdycfl6wialdm75vwxutcpq | [oci-mad-ot-vnet-mw-stg](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak3th2pjmr7nybv5kdvou2fdycfl6wialdm75vwxutcpq)            | [oci-mad-ot-udr-mw-back-stg](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaap3vkqcn6zqggmek5xfqxt3ztraevtyuyc3szq35dnznq2c6suekq)       | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaalsn222vjo6oz4unra4tmtmsjuan7yf3zyjpfecy2wuulh47lvmka | oci-mad-drgattach-hub-sha                   | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | VCN    | ocid1.vcn.oc1.eu-madrid-1.amaaaaaa6k4uvdqak3mn33cxhn3zcimaotuoxtwdw3hjcnv76g6mhfxcupiq | [oci-mad-vnet-hub-sha](#vcn-ocid1_vcn_oc1_eu_madrid_1_amaaaaaa6k4uvdqak3mn33cxhn3zcimaotuoxtwdw3hjcnv76g6mhfxcupiq)              | [oci-mad-udr-hub-int-sha](#rt-ocid1_routetable_oc1_eu_madrid_1_aaaaaaaafgj2m2blgizoo42jk2hzqhtxd4qoybykryr725hu3swn5ksprzjq)          | Compartment: aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq | ATTACHED |

#### DRG Route Tables

##### oci-mad-udr-hub-sha (ID: ocid1.drgroutetable.oc1.eu-madrid-1.aaaaaaaaxepomj4w7cmvy5yth6vikanpmc27tacoscqebse7gilr67o5sgoa)

Import Distribution: [oci-mad-importrd-hub-sha](#drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaary76rhkb2mvxhgixejrvxpm2qli2p2tq37km2whsprrucx6meb6a)

No hay reglas de ruta estáticas definidas.

##### oci-mad-udr-spokes-sha (ID: ocid1.drgroutetable.oc1.eu-madrid-1.aaaaaaaaowxfjyptb7pyq4lieeitwh5og5pptqcycouyhd5mhrn5dvlmfija)

Import Distribution: No configurada

| Destino   | Tipo de Destino   | Next Hop DRG Attachment                                                                                                            | Origen   | Tipo de Ruta   |
|:----------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [oci-mad-drgattach-hub-sha](#dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaalsn222vjo6oz4unra4tmtmsjuan7yf3zyjpfecy2wuulh47lvmka) |          | STATIC         |

##### oci-mad-udr-ipsec-sha (ID: ocid1.drgroutetable.oc1.eu-madrid-1.aaaaaaaacf5ii5djnsaxrhmawrng3ajhyhqczxo6e6dm6vqb5tqbwavfte3q)

Import Distribution: [oci-mad-importrd-ipsec-sha](#drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaa4mpc4rqhggw7ed4rq76wbodnzer6qagchnfcpxifztaeahj67dbq)

| Destino        | Tipo de Destino   | Next Hop DRG Attachment                                                                                                            | Origen   | Tipo de Ruta   |
|:---------------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------|
| 10.201.32.0/19 | CIDR_BLOCK        | ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaagbegoyyt7oarxu2qg4db3b2z5hyci3byod4ejcrfy5yf2b5my6ya (Attachment no encontrado)        |          | STATIC         |
| 10.201.0.0/19  | CIDR_BLOCK        | [oci-mad-drgattach-hub-sha](#dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaalsn222vjo6oz4unra4tmtmsjuan7yf3zyjpfecy2wuulh47lvmka) |          | STATIC         |

##### oci-mad-udr-rpc-ams-sha (ID: ocid1.drgroutetable.oc1.eu-madrid-1.aaaaaaaawzx33xwzw6e6ktkgvxsr5qv4it6qbl75qzggrhbvygs6zww6gfyq)

Import Distribution: [oci-mad-importrd-rpc-ams-sha](#drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaaoxpw5les2cnjlt7nxtfrdiqbtwisifqh7ppfg26gyhjq2w4dx5ma)

| Destino       | Tipo de Destino   | Next Hop DRG Attachment                                                                                                            | Origen   | Tipo de Ruta   |
|:--------------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------|
| 10.201.0.0/19 | CIDR_BLOCK        | [oci-mad-drgattach-hub-sha](#dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaalsn222vjo6oz4unra4tmtmsjuan7yf3zyjpfecy2wuulh47lvmka) |          | STATIC         |

##### oci-mad-udr-fastconnect-sha (ID: ocid1.drgroutetable.oc1.eu-madrid-1.aaaaaaaa7fgxe36mzfdf5vedmrq4s5g576bjwelzgl4kvtu5wire7juf3w2a)

Import Distribution: [oci-mad-importrd-fastconnect-sha](#drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaaj5vfbfn4lbsyd6xqsmrkm3t2ayjlgk4yugrjfpc7olnd5qnm2b2q)

| Destino        | Tipo de Destino   | Next Hop DRG Attachment                                                                                                            | Origen   | Tipo de Ruta   |
|:---------------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------|
| 10.201.32.0/19 | CIDR_BLOCK        | ocid1.drgattachment.oc1.eu-madrid-1.aaaaaaaagbegoyyt7oarxu2qg4db3b2z5hyci3byod4ejcrfy5yf2b5my6ya (Attachment no encontrado)        |          | STATIC         |
| 10.201.0.0/19  | CIDR_BLOCK        | [oci-mad-drgattach-hub-sha](#dra-ocid1_drgattachment_oc1_eu_madrid_1_aaaaaaaalsn222vjo6oz4unra4tmtmsjuan7yf3zyjpfecy2wuulh47lvmka) |          | STATIC         |

##### DONT USE - Autogenerated Drg Route Table for VCN attachments  (ID: ocid1.drgroutetable.oc1.eu-madrid-1.aaaaaaaabh62gzxu6pgn7exobtbopxbvhe4zvg75cjkqquxhiygjdohkht7a)

Import Distribution: [DONT USE - Autogenerated Import Route Distribution for ALL routes](#drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaa64vqc4ncs4sb7s4e6pn3pjnkhbmntlodl5qh74gswytzhsyjedba)

No hay reglas de ruta estáticas definidas.

##### DONT USE - Autogenerated Drg Route Table for RPC, VC, and IPSec attachments  (ID: ocid1.drgroutetable.oc1.eu-madrid-1.aaaaaaaa3q2ilecgajak6mk7l5e3qso4ykh3o2ktxvxj7f34bjaeiajogvla)

Import Distribution: [DONT USE - Autogenerated Import Route Distribution for VCN Routes](#drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaa6frgfucknvrtodyv3kostftum5mzltddpismerzydtzqll7gempa)

No hay reglas de ruta estáticas definidas.

#### DRG Route Distributions (Import/Export)

<a id="drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaaj5vfbfn4lbsyd6xqsmrkm3t2ayjlgk4yugrjfpc7olnd5qnm2b2q"></a>
##### oci-mad-importrd-fastconnect-sha (ID: ocid1.drgroutedistribution.oc1.eu-madrid-1.aaaaaaaaj5vfbfn4lbsyd6xqsmrkm3t2ayjlgk4yugrjfpc7olnd5qnm2b2q)

Tipo de Distribución: IMPORT

No hay statements de distribución definidos.

<a id="drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaa4mpc4rqhggw7ed4rq76wbodnzer6qagchnfcpxifztaeahj67dbq"></a>
##### oci-mad-importrd-ipsec-sha (ID: ocid1.drgroutedistribution.oc1.eu-madrid-1.aaaaaaaa4mpc4rqhggw7ed4rq76wbodnzer6qagchnfcpxifztaeahj67dbq)

Tipo de Distribución: IMPORT

No hay statements de distribución definidos.

<a id="drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaaoxpw5les2cnjlt7nxtfrdiqbtwisifqh7ppfg26gyhjq2w4dx5ma"></a>
##### oci-mad-importrd-rpc-ams-sha (ID: ocid1.drgroutedistribution.oc1.eu-madrid-1.aaaaaaaaoxpw5les2cnjlt7nxtfrdiqbtwisifqh7ppfg26gyhjq2w4dx5ma)

Tipo de Distribución: IMPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|          10 | DESCONOCIDO     |                   |                     | ACCEPT   |
|          20 | DESCONOCIDO     |                   |                     | ACCEPT   |

<a id="drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaary76rhkb2mvxhgixejrvxpm2qli2p2tq37km2whsprrucx6meb6a"></a>
##### oci-mad-importrd-hub-sha (ID: ocid1.drgroutedistribution.oc1.eu-madrid-1.aaaaaaaary76rhkb2mvxhgixejrvxpm2qli2p2tq37km2whsprrucx6meb6a)

Tipo de Distribución: IMPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|          40 | DESCONOCIDO     |                   |                     | ACCEPT   |
|          30 | DESCONOCIDO     |                   |                     | ACCEPT   |
|          10 | DESCONOCIDO     |                   |                     | ACCEPT   |
|          20 | DESCONOCIDO     |                   |                     | ACCEPT   |

<a id="drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaaiavompwfxotkan7dsx52rkldkzcdk4aahalizl4imch22i6wetwq"></a>
##### Default Export Route Distribution for DRG: test (ID: ocid1.drgroutedistribution.oc1.eu-madrid-1.aaaaaaaaiavompwfxotkan7dsx52rkldkzcdk4aahalizl4imch22i6wetwq)

Tipo de Distribución: EXPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|           1 | DESCONOCIDO     |                   |                     | ACCEPT   |

<a id="drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaa64vqc4ncs4sb7s4e6pn3pjnkhbmntlodl5qh74gswytzhsyjedba"></a>
##### DONT USE - Autogenerated Import Route Distribution for ALL routes (ID: ocid1.drgroutedistribution.oc1.eu-madrid-1.aaaaaaaa64vqc4ncs4sb7s4e6pn3pjnkhbmntlodl5qh74gswytzhsyjedba)

Tipo de Distribución: IMPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|           1 | DESCONOCIDO     |                   |                     | ACCEPT   |

<a id="drd-ocid1_drgroutedistribution_oc1_eu_madrid_1_aaaaaaaa6frgfucknvrtodyv3kostftum5mzltddpismerzydtzqll7gempa"></a>
##### DONT USE - Autogenerated Import Route Distribution for VCN Routes (ID: ocid1.drgroutedistribution.oc1.eu-madrid-1.aaaaaaaa6frgfucknvrtodyv3kostftum5mzltddpismerzydtzqll7gempa)

Tipo de Distribución: IMPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|           1 | DESCONOCIDO     |                   |                     | ACCEPT   |

#### Remote Peering Connections

| ID                                                                                                         | Nombre                | DRG ID                                                                                 | Región Peer    | RPC Peer ID                                                                                                   | Estado    | Estado Peering   |
|:-----------------------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------|:---------------|:--------------------------------------------------------------------------------------------------------------|:----------|:-----------------|
| ocid1.remotepeeringconnection.oc1.eu-madrid-1.aaaaaaaaicr5yjr34uihgdxsqavz4muipbnm66ujeaahygdmxehbmrklcnja | oci-mad-rpc-ams-sha-1 | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | eu-amsterdam-1 | ocid1.remotepeeringconnection.oc1.eu-amsterdam-1.aaaaaaaaqsqwz4looswqkwzh7fkbadfszy6ig7cozc3ql7jnkrs6nfzp453q | AVAILABLE | PEERED           |

<a id="region-eu-madrid-1-vpn"></a>
### Conexiones VPN IPSec

| ID                                                                                                 | Nombre              | DRG ID                                                                                 | CPE ID                                                                                 | IP CPE      | IP CPE Tipo   | Estado    |
|:---------------------------------------------------------------------------------------------------|:--------------------|:---------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|:------------|:--------------|:----------|
| ocid1.ipsecconnection.oc1.eu-madrid-1.aaaaaaaamnspqje7txthzziistfgeu56w7btlsdsdzk5jhir6hakdvfkmnfq | oci-mad-ipsec-sha-1 | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | ocid1.cpe.oc1.eu-madrid-1.aaaaaaaa6jsxoacqu3c4lngvjmruwdq4o6rykcn3z36bhcl7sy75okpvkyra | 195.57.2.66 | IP_ADDRESS    | AVAILABLE |

#### Detalles de Túneles VPN

##### Túneles de oci-mad-ipsec-sha-1

No se encontraron túneles para esta conexión VPN.

<a id="region-eu-madrid-1-fc"></a>
### Conexiones FastConnect

| ID                                                                                                | Nombre                      | Tipo    | Ancho de Banda (Gbps)   | DRG ID                                                                                 | Proveedor   | Estado      |
|:--------------------------------------------------------------------------------------------------|:----------------------------|:--------|:------------------------|:---------------------------------------------------------------------------------------|:------------|:------------|
| ocid1.virtualcircuit.oc1.eu-madrid-1.aaaaaaaayskuzab2vo2jvfwl5lo4yhdojyfoa7im73lakxygvkfjqjmluyga | oci-mad-vc-interxion1-sha-1 | PRIVATE | 1 Gbps                  | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | N/A         | PROVISIONED |
| ocid1.virtualcircuit.oc1.eu-madrid-1.aaaaaaaaw7gcgznfay6d2oclqka52lwl6gj64kkersrnsuk2wnxmgeqb2sna | oci-mad-vc-interxion2-sha-1 | PRIVATE | 1 Gbps                  | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq | N/A         | PROVISIONED |

#### Detalles de Virtual Circuits y Cross-Connects

##### Cross-Connects

| ID                                                                                              | Nombre                 | Estado      | Tipo   | Grupo   | Compartment                                                                         |
|:------------------------------------------------------------------------------------------------|:-----------------------|:------------|:-------|:--------|:------------------------------------------------------------------------------------|
| ocid1.crossconnect.oc1.eu-madrid-1.aaaaaaaafdn5xfiyeern665fzws6fpq5vka6stcg7d3m5m27l2dlaei27bba | oci-mad-fc-interxion-1 | PROVISIONED | 1 Gbps |         | ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq |
| ocid1.crossconnect.oc1.eu-madrid-1.aaaaaaaaxrq7p5honqf6s3peeqhvhr3bg4uy7yysepvzitda4tal73fj4q3a | oci-mad-fc-interxion-2 | PROVISIONED | 1 Gbps |         | ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq |
| ocid1.crossconnect.oc1.eu-madrid-1.aaaaaaaafdn5xfiyeern665fzws6fpq5vka6stcg7d3m5m27l2dlaei27bba | oci-mad-fc-interxion-1 | PROVISIONED | 1 Gbps |         | ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq |
| ocid1.crossconnect.oc1.eu-madrid-1.aaaaaaaaxrq7p5honqf6s3peeqhvhr3bg4uy7yysepvzitda4tal73fj4q3a | oci-mad-fc-interxion-2 | PROVISIONED | 1 Gbps |         | ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq |

##### Detalles de Virtual Circuits

###### Virtual Circuit: oci-mad-vc-interxion1-sha-1

|                | Valor                                                                                             |
|:---------------|:--------------------------------------------------------------------------------------------------|
| ID             | ocid1.virtualcircuit.oc1.eu-madrid-1.aaaaaaaayskuzab2vo2jvfwl5lo4yhdojyfoa7im73lakxygvkfjqjmluyga |
| Nombre         | oci-mad-vc-interxion1-sha-1                                                                       |
| Tipo           | PRIVATE                                                                                           |
| Ancho de Banda | 1 Gbps                                                                                            |
| DRG ID         | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq            |
| Proveedor      | N/A                                                                                               |
| Estado         | PROVISIONED                                                                                       |
| Compartment    | ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq               |
| Fecha Creación | 2024-10-18 08:08:22                                                                               |

No se encontraron Cross-Connects claramente asociados a este Virtual Circuit.

*Nota: Los Cross-Connects pueden estar asociados indirectamente a través de grupos o DRGs.*

###### Virtual Circuit: oci-mad-vc-interxion2-sha-1

|                | Valor                                                                                             |
|:---------------|:--------------------------------------------------------------------------------------------------|
| ID             | ocid1.virtualcircuit.oc1.eu-madrid-1.aaaaaaaaw7gcgznfay6d2oclqka52lwl6gj64kkersrnsuk2wnxmgeqb2sna |
| Nombre         | oci-mad-vc-interxion2-sha-1                                                                       |
| Tipo           | PRIVATE                                                                                           |
| Ancho de Banda | 1 Gbps                                                                                            |
| DRG ID         | ocid1.drg.oc1.eu-madrid-1.aaaaaaaa4nyyya6zahfukxshlj7hmtq65q6tkyw2uu7ftcghcde56uiku4rq            |
| Proveedor      | N/A                                                                                               |
| Estado         | PROVISIONED                                                                                       |
| Compartment    | ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq               |
| Fecha Creación | 2024-10-18 08:10:19                                                                               |

No se encontraron Cross-Connects claramente asociados a este Virtual Circuit.

*Nota: Los Cross-Connects pueden estar asociados indirectamente a través de grupos o DRGs.*

<a id="region-eu-amsterdam-1"></a>
## Región: eu-amsterdam-1

### Virtual Cloud Networks (VCNs)

| ID                                                                                        | Nombre                                                                                                                              | CIDR             | Estado    | Compartment                                                                                   |
|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:-----------------|:----------|:----------------------------------------------------------------------------------------------|
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqa242pn4z3clc3fjfehoctvx6dmba7w7uimlxtfmpptepa | [test](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqa242pn4z3clc3fjfehoctvx6dmba7w7uimlxtfmpptepa)                              | 10.0.0.0/16      | AVAILABLE | lab (ocid1.compartment.oc1..aaaaaaaadggbrkmkqmkeuhj5e34heegrk7aut6sf6uforqha4cas6yiayena)     |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqas6ii7orfb5ieq3yh7v5sz3odqpdz3xmga325l6riba7q | [oci-ams-it-vnet-functions-dev](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqas6ii7orfb5ieq3yh7v5sz3odqpdz3xmga325l6riba7q)     | 10.201.34.128/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqagxwcp7t334bf6phogoczfdpyrpbhvaochvw2nb2osbxa | [oci-ams-it-vnet-forms-dev](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqagxwcp7t334bf6phogoczfdpyrpbhvaochvw2nb2osbxa)         | 10.201.34.64/26  | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqapn3vuk62v3z24vqxirjmdnlu5udqwwqhxmdnjfefr45a | [oci-ams-it-vnet-vdipro-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqapn3vuk62v3z24vqxirjmdnlu5udqwwqhxmdnjfefr45a)        | 10.201.38.128/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqabnaw37eb3fyqw7nrigkqb2tmahrzwak6d5pz6asltm5a | [oci-ams-it-vnet-tools-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqabnaw37eb3fyqw7nrigkqb2tmahrzwak6d5pz6asltm5a)         | 10.201.38.0/26   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqanulxctlc7mhujlrxufblf4vkcctqz4zerpqbmytd7o6q | [oci-ams-it-vnet-vdi-customers-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqanulxctlc7mhujlrxufblf4vkcctqz4zerpqbmytd7o6q) | 10.201.36.0/23   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaaps62ygw643sijetx6rwn5qr3w6gikqcexkxvyz7y4oq | [oci-ams-it-vnet-functions-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaaps62ygw643sijetx6rwn5qr3w6gikqcexkxvyz7y4oq)     | 10.201.34.192/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaweyhygwptai46wmh2xcqynumk5vyhivkxctfllhbdupa | [oci-ams-ot-vnet-mw-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaweyhygwptai46wmh2xcqynumk5vyhivkxctfllhbdupa)            | 10.201.33.192/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqarmgitbkpdy5h5pwcyxd3gptxxhopq22bmqpp67rfmega | [oci-ams-it-vnet-mw-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqarmgitbkpdy5h5pwcyxd3gptxxhopq22bmqpp67rfmega)            | 10.201.33.64/26  | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaojplkm7p4ywh42abafmkq4xkti7qmzwh4ebo2avp53la | [oci-ams-ot-vnet-db-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaojplkm7p4ywh42abafmkq4xkti7qmzwh4ebo2avp53la)            | 10.201.32.192/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaebgsjzpxg26bf6nevmi6prnl52mqx25dnxv6b4mpllpa | [oci-ams-it-vnet-db-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaebgsjzpxg26bf6nevmi6prnl52mqx25dnxv6b4mpllpa)            | 10.201.32.64/26  | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaeccutpjlmlmk635jpba37qcmoomhcfl7cmvze43xvqsq | [oci-ams-it-vnet-tools-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaeccutpjlmlmk635jpba37qcmoomhcfl7cmvze43xvqsq)         | 10.201.38.64/26  | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqayzueatthiz3v6ls2qfqge3pedyyusuve4ddytnwwbmfa | [oci-ams-ot-vnet-mw-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqayzueatthiz3v6ls2qfqge3pedyyusuve4ddytnwwbmfa)            | 10.201.34.0/26   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqavkpxggb7lunwrptanl6tndqjuj3netvdjgc5enhq7rfa | [oci-ams-it-vnet-mw-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqavkpxggb7lunwrptanl6tndqjuj3netvdjgc5enhq7rfa)            | 10.201.33.128/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaumsllyvdgfkyo3rfgrx2nb2taecrqanopuy3x33omgga | [oci-ams-ot-vnet-db-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaumsllyvdgfkyo3rfgrx2nb2taecrqanopuy3x33omgga)            | 10.201.33.0/26   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaczixf26gyqw4o7p2mnwhd2cx2k2e6uhgzcgy7kcg3kfq | [oci-ams-it-vnet-db-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaczixf26gyqw4o7p2mnwhd2cx2k2e6uhgzcgy7kcg3kfq)            | 10.201.32.128/26 | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a) |
| ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqabpiciz67q2ud5hpn2i3eqzv7pwgqcsoynovow26kzfvq | [oci-ams-vnet-hub-sha](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqabpiciz67q2ud5hpn2i3eqzv7pwgqcsoynovow26kzfvq)              | 10.201.32.0/26   | AVAILABLE | network (ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq) |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqa242pn4z3clc3fjfehoctvx6dmba7w7uimlxtfmpptepa"></a>
#### Recursos de VCN: test (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqa242pn4z3clc3fjfehoctvx6dmba7w7uimlxtfmpptepa)

##### Subnets

| ID                                                                                           | Nombre   | CIDR        | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                          | Route Table ID                                                                                   | Security Lists                                                                                                                           |
|:---------------------------------------------------------------------------------------------|:---------|:------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaajyhunfqg3cyjouqthm3ulm5wsqk67h2x4shdmpb6onjusbpxraua | test     | 10.0.1.0/24 | Regional         | No        | AVAILABLE | [Default Route Table for test](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaabytnzprhb2jkj7ifcmnzw2ffv5diwqicxew32or4njoztalubixa) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaabytnzprhb2jkj7ifcmnzw2ffv5diwqicxew32or4njoztalubixa | [Default Security List for test](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaa3wqvqeqqenewto6y6cw4amegyfrfeilpxz2rd624no44opk3hxma) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaabytnzprhb2jkj7ifcmnzw2ffv5diwqicxew32or4njoztalubixa"></a>
###### Default Route Table for test (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaabytnzprhb2jkj7ifcmnzw2ffv5diwqicxew32or4njoztalubixa)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| all-ams-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaa7ocyiamw2bc6fim7es3p6rzt4xzc5kees76bpp5svxwxtwzt3juq) | Service Gateway   |               |

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaa3wqvqeqqenewto6y6cw4amegyfrfeilpxz2rd624no44opk3hxma"></a>
###### Default Security List for test (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaa3wqvqeqqenewto6y6cw4amegyfrfeilpxz2rd624no44opk3hxma)

####### Reglas de Entrada

| Origen      | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0   | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0   | CIDR_BLOCK       | ICMP        |           |               |
| 10.0.0.0/16 | CIDR_BLOCK       | ICMP        |           |               |
| 10.0.0.0/8  | CIDR_BLOCK       | TCP         | 3389-3389 |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

No se encontraron DRG Attachments en esta VCN.

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaa7ocyiamw2bc6fim7es3p6rzt4xzc5kees76bpp5svxwxtwzt3juq"></a>
| ID                                                                                                   | Nombre   | Servicios   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:---------|:------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaa7ocyiamw2bc6fim7es3p6rzt4xzc5kees76bpp5svxwxtwzt3juq | test     |             | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqas6ii7orfb5ieq3yh7v5sz3odqpdz3xmga325l6riba7q"></a>
#### Recursos de VCN: oci-ams-it-vnet-functions-dev (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqas6ii7orfb5ieq3yh7v5sz3odqpdz3xmga325l6riba7q)

##### Subnets

| ID                                                                                           | Nombre                        | CIDR             | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                          | Route Table ID                                                                                   | Security Lists                                                                                                                          |
|:---------------------------------------------------------------------------------------------|:------------------------------|:-----------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaazvwsgvayuhfatflasbqdnh35f5awlnx4bxnchafdxwo2fo5mu66q | oci-ams-it-snet-functions-dev | 10.201.34.128/26 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-functions-dev](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa76vqladcgy3gmi62unseqs52tmahzh5xgbvx235nl4ru4qa547la) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa76vqladcgy3gmi62unseqs52tmahzh5xgbvx235nl4ru4qa547la | [oci-ams-it-sl-functions-dev-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaao3gjkraiopmj3nlbn6cim33zvmu6lcjkascvkabpa7xqmdxezspa) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa76vqladcgy3gmi62unseqs52tmahzh5xgbvx235nl4ru4qa547la"></a>
###### oci-ams-it-udr-functions-dev (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa76vqladcgy3gmi62unseqs52tmahzh5xgbvx235nl4ru4qa547la)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |
| all-ams-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaq3irsqetth5r4o32rckdcclelumytqz7t3klsfbm2mr3ma4ss3ua) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa2qyiejmsmb7dsuav7frgf4etkv6x6otq7emfnygacn32n44axwuq"></a>
###### Default Route Table for oci-ams-it-vnet-functions-dev (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa2qyiejmsmb7dsuav7frgf4etkv6x6otq7emfnygacn32n44axwuq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaao3gjkraiopmj3nlbn6cim33zvmu6lcjkascvkabpa7xqmdxezspa"></a>
###### oci-ams-it-sl-functions-dev-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaao3gjkraiopmj3nlbn6cim33zvmu6lcjkascvkabpa7xqmdxezspa)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3389-3389 |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaamtp6vfqigasaqcgmaw3ow7cdezgrygprebteq35i4sphcjof6s4a"></a>
###### Default Security List for oci-ams-it-vnet-functions-dev (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaamtp6vfqigasaqcgmaw3ow7cdezgrygprebteq35i4sphcjof6s4a)

####### Reglas de Entrada

| Origen           | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0        | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0        | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.34.128/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                                  | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:----------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaao2yhm42l37ggl4se23v4w2icgu42etgb5qmpot32iejhsbz762ma | oci-ams-it-drgattach-vnet-functions-dev | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaq3irsqetth5r4o32rckdcclelumytqz7t3klsfbm2mr3ma4ss3ua"></a>
| ID                                                                                                   | Nombre                            | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:----------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaaq3irsqetth5r4o32rckdcclelumytqz7t3klsfbm2mr3ma4ss3ua | oci-ams-it-vngw-svc-functions-dev | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqagxwcp7t334bf6phogoczfdpyrpbhvaochvw2nb2osbxa"></a>
#### Recursos de VCN: oci-ams-it-vnet-forms-dev (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqagxwcp7t334bf6phogoczfdpyrpbhvaochvw2nb2osbxa)

##### Subnets

| ID                                                                                           | Nombre                    | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                      | Route Table ID                                                                                   | Security Lists                                                                                                                      |
|:---------------------------------------------------------------------------------------------|:--------------------------|:----------------|:-----------------|:----------|:----------|:---------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaaufyrevypl6gvss3wtl2hjqabewwkxymadgc7blj4rarn5bc2gq3a | oci-ams-it-snet-forms-dev | 10.201.34.64/26 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-forms-dev](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaxlrhqzewqts6fl53vrp26fkgrmi7ykga4gjcbzdqkvzdimt6brlq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaxlrhqzewqts6fl53vrp26fkgrmi7ykga4gjcbzdqkvzdimt6brlq | [oci-ams-it-sl-forms-dev-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaamdl3fj7yck4bz5xllmj7ff6ubbgvczunlojydf52xp4sksqaggra) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaxlrhqzewqts6fl53vrp26fkgrmi7ykga4gjcbzdqkvzdimt6brlq"></a>
###### oci-ams-it-udr-forms-dev (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaxlrhqzewqts6fl53vrp26fkgrmi7ykga4gjcbzdqkvzdimt6brlq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| all-ams-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaobjw2owclhkur5unjzsxommzg2pjosbaduczdig3iwvtlcqpmqna) | Service Gateway   |               |
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaan37utw2jomtjgf52frh2evsophxihc524yahviixhuywrzxtvb6a"></a>
###### Default Route Table for oci-ams-it-vnet-forms-dev (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaan37utw2jomtjgf52frh2evsophxihc524yahviixhuywrzxtvb6a)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaamdl3fj7yck4bz5xllmj7ff6ubbgvczunlojydf52xp4sksqaggra"></a>
###### oci-ams-it-sl-forms-dev-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaamdl3fj7yck4bz5xllmj7ff6ubbgvczunlojydf52xp4sksqaggra)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0  | CIDR_BLOCK       | Todos       |           |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaapms2cctne6dtvbigqgn73prgo6wdz2yzhhs2b4l2nim4ht37na7q"></a>
###### Default Security List for oci-ams-it-vnet-forms-dev (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaapms2cctne6dtvbigqgn73prgo6wdz2yzhhs2b4l2nim4ht37na7q)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.34.64/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                              | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaaodvhzayjdxmjg4uqjvtwunacmm2wkpeqimvewoxzzvgbrcxixcga | oci-ams-it-drgattach-vnet-forms-dev | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaobjw2owclhkur5unjzsxommzg2pjosbaduczdig3iwvtlcqpmqna"></a>
| ID                                                                                                   | Nombre                        | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaaobjw2owclhkur5unjzsxommzg2pjosbaduczdig3iwvtlcqpmqna | oci-ams-it-vngw-svc-forms-dev | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqapn3vuk62v3z24vqxirjmdnlu5udqwwqhxmdnjfefr45a"></a>
#### Recursos de VCN: oci-ams-it-vnet-vdipro-pro (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqapn3vuk62v3z24vqxirjmdnlu5udqwwqhxmdnjfefr45a)

##### Subnets

| ID                                                                                           | Nombre                  | CIDR             | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                       | Route Table ID                                                                                   | Security Lists                                                                                                                       |
|:---------------------------------------------------------------------------------------------|:------------------------|:-----------------|:-----------------|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaaajxnz3ziwsii2bze65foa7pekyhfmto7yud2bne5llzj5zswd4fa | oci-ams-snet-vdipro-pro | 10.201.38.128/26 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-vdipro-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaap45as3kdzoku4u77o5ychtqe7hgdsopiopiv2gk4wt6mwwebikvq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaap45as3kdzoku4u77o5ychtqe7hgdsopiopiv2gk4wt6mwwebikvq | [oci-ams-it-sl-vdipro-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaal5q2gjundjl2tofdzmwnuerp2xtb3r676qfnanywdywu7lhwpsfq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaap45as3kdzoku4u77o5ychtqe7hgdsopiopiv2gk4wt6mwwebikvq"></a>
###### oci-ams-it-udr-vdipro-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaap45as3kdzoku4u77o5ychtqe7hgdsopiopiv2gk4wt6mwwebikvq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| all-ams-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaab4ke6xvnsr7tcdc6iiv3yetynizgqtd26ikrbeoroek3fhptl26q) | Service Gateway   |               |
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaafvvef5ojx62qnrfpa3dk2bdjwn7n4dyxdfvigppn26s42nu5wquq"></a>
###### Default Route Table for oci-ams-it-vnet-vdipro-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaafvvef5ojx62qnrfpa3dk2bdjwn7n4dyxdfvigppn26s42nu5wquq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaal5q2gjundjl2tofdzmwnuerp2xtb3r676qfnanywdywu7lhwpsfq"></a>
###### oci-ams-it-sl-vdipro-pro-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaal5q2gjundjl2tofdzmwnuerp2xtb3r676qfnanywdywu7lhwpsfq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3389-3389 | rdp           |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaal3cdmkksn6qwlpwh6q57wmovmgwovt76tdstnqaioog437d4hwra"></a>
###### Default Security List for oci-ams-it-vnet-vdipro-pro (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaal3cdmkksn6qwlpwh6q57wmovmgwovt76tdstnqaioog437d4hwra)

####### Reglas de Entrada

| Origen           | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0        | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0        | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.38.128/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                               | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:-------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaamak4hr3nhmpui5rfdvcixgc3zaiywtcg3pcxvmj5wun6ih6uaaha | oci-ams-it-drgattach-vnet-vdipro-pro | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaab4ke6xvnsr7tcdc6iiv3yetynizgqtd26ikrbeoroek3fhptl26q"></a>
| ID                                                                                                   | Nombre                         | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:-------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaab4ke6xvnsr7tcdc6iiv3yetynizgqtd26ikrbeoroek3fhptl26q | oci-ams-it-vngw-svc-vdipro-pro | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqabnaw37eb3fyqw7nrigkqb2tmahrzwak6d5pz6asltm5a"></a>
#### Recursos de VCN: oci-ams-it-vnet-tools-pro (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqabnaw37eb3fyqw7nrigkqb2tmahrzwak6d5pz6asltm5a)

##### Subnets

| ID                                                                                           | Nombre                    | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                      | Route Table ID                                                                                   | Security Lists                                                                                                                      |
|:---------------------------------------------------------------------------------------------|:--------------------------|:---------------|:-----------------|:----------|:----------|:---------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaa5ur7tkq7e726vwbkop7yx2eswlv2pb2hdyso437bahtblds3lzda | oci-ams-it-snet-tools-pro | 10.201.38.0/26 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-tools-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaad26hkb6apwidjgsrrqejacjpzrx7hkvjwywjk22ny2eippk27ifq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaad26hkb6apwidjgsrrqejacjpzrx7hkvjwywjk22ny2eippk27ifq | [oci-ams-it-sl-tools-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaac3vuukz733map6o73yvwinwjfbdknnqvkavwc3y3fwbdpi76bczq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaad26hkb6apwidjgsrrqejacjpzrx7hkvjwywjk22ny2eippk27ifq"></a>
###### oci-ams-it-udr-tools-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaad26hkb6apwidjgsrrqejacjpzrx7hkvjwywjk22ny2eippk27ifq)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                        | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaccmgdds6onirp7yc7ohw5xju6tkpyn4a5mpurelsp76nfzbp3z5a"></a>
###### Default Route Table for oci-ams-it-vnet-tools-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaccmgdds6onirp7yc7ohw5xju6tkpyn4a5mpurelsp76nfzbp3z5a)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaac3vuukz733map6o73yvwinwjfbdknnqvkavwc3y3fwbdpi76bczq"></a>
###### oci-ams-it-sl-tools-pro-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaac3vuukz733map6o73yvwinwjfbdknnqvkavwc3y3fwbdpi76bczq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | Todos       |           |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaojpulpzswd3fi7ah54ekx6w2wuhyvkkgk4briru3324tgsia7jpa"></a>
###### Default Security List for oci-ams-it-vnet-tools-pro (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaaojpulpzswd3fi7ah54ekx6w2wuhyvkkgk4briru3324tgsia7jpa)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.38.0/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                              | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaagevgvwlhhpiyfp5id4xe7exwmju3bex34idcjrx7wcumncl3xioq | oci-ams-it-drgattach-vnet-tools-pro | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqanulxctlc7mhujlrxufblf4vkcctqz4zerpqbmytd7o6q"></a>
#### Recursos de VCN: oci-ams-it-vnet-vdi-customers-pro (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqanulxctlc7mhujlrxufblf4vkcctqz4zerpqbmytd7o6q)

##### Subnets

| ID                                                                                           | Nombre                            | CIDR           | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                              | Route Table ID                                                                                   | Security Lists                                                                                                                              |
|:---------------------------------------------------------------------------------------------|:----------------------------------|:---------------|:-----------------|:----------|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaaucej2y5jzomlcscll6xgvyli22vx3jfdq7o2ahdfzucpinf4rvkq | oci-ams-it-snet-vdi-customers-pro | 10.201.36.0/23 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-vdi-customers-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaruuqsqvnsvj2go3ldr5adksmrkrxvig4o6asblr3q3yvmvmgxmha) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaruuqsqvnsvj2go3ldr5adksmrkrxvig4o6asblr3q3yvmvmgxmha | [oci-ams-it-sl-vdi-customers-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaahcsxtsamun2zkf6aiq6l36ys4i3stvf7ylydt5nmqv3ywkn5k6eq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaruuqsqvnsvj2go3ldr5adksmrkrxvig4o6asblr3q3yvmvmgxmha"></a>
###### oci-ams-it-udr-vdi-customers-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaruuqsqvnsvj2go3ldr5adksmrkrxvig4o6asblr3q3yvmvmgxmha)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |
| all-ams-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaok3ksufwuthh534322nfvqwfi43caq4ytaz42uqsaary6s5c7bva) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaq2ie7nkt43o4ltcak3jk5ttaugrtckgwc4dbmkepdgwu3k3gljia"></a>
###### Default Route Table for oci-ams-it-vnet-vdi-customers-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaq2ie7nkt43o4ltcak3jk5ttaugrtckgwc4dbmkepdgwu3k3gljia)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaahcsxtsamun2zkf6aiq6l36ys4i3stvf7ylydt5nmqv3ywkn5k6eq"></a>
###### oci-ams-it-sl-vdi-customers-pro-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaahcsxtsamun2zkf6aiq6l36ys4i3stvf7ylydt5nmqv3ywkn5k6eq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3389-3389 |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaqq4dzjsz4cved34eww4rrlbi5imadhhb2lzjk4gib2y343s3de4a"></a>
###### Default Security List for oci-ams-it-vnet-vdi-customers-pro (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaaqq4dzjsz4cved34eww4rrlbi5imadhhb2lzjk4gib2y343s3de4a)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.36.0/23 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                                      | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:--------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaa7pinr3mnargqmu5stb44ev5j2rxms23shuic3ppbjbfcamuirqka | oci-ams-it-drgattach-vnet-vdi-customers-pro | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaok3ksufwuthh534322nfvqwfi43caq4ytaz42uqsaary6s5c7bva"></a>
| ID                                                                                                   | Nombre                            | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:----------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaaok3ksufwuthh534322nfvqwfi43caq4ytaz42uqsaary6s5c7bva | oci-ams-it-vngw-svc-customers-pro | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaaps62ygw643sijetx6rwn5qr3w6gikqcexkxvyz7y4oq"></a>
#### Recursos de VCN: oci-ams-it-vnet-functions-pro (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaaps62ygw643sijetx6rwn5qr3w6gikqcexkxvyz7y4oq)

##### Subnets

| ID                                                                                           | Nombre                        | CIDR             | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                          | Route Table ID                                                                                   | Security Lists                                                                                                                          |
|:---------------------------------------------------------------------------------------------|:------------------------------|:-----------------|:-----------------|:----------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaawpwenrtewyemydrtslmyh4wnntxbl4eald7y6dv6o4eozb2mm7ya | oci-ams-it-snet-functions-pro | 10.201.34.192/26 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-functions-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa3ae4v5dua7efywpliibd25rtcu4a5353jjgdlod7bxt3wfqzpfqq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa3ae4v5dua7efywpliibd25rtcu4a5353jjgdlod7bxt3wfqzpfqq | [oci-ams-it-sl-functions-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaarhwhd2tsynji4cvrodhi5f2nmjicdarnvs5hmslsykn7oqjk5kvq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa3ae4v5dua7efywpliibd25rtcu4a5353jjgdlod7bxt3wfqzpfqq"></a>
###### oci-ams-it-udr-functions-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa3ae4v5dua7efywpliibd25rtcu4a5353jjgdlod7bxt3wfqzpfqq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |
| all-ams-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaasaar22q7zupr6xgqeki5utdjlcfffrqqtphxblojtnc57s3hvp5a) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaaxsuuxi5bghbyfehskgnrgqijlqa43eswunz4wwjn3p2o6h5fepa"></a>
###### Default Route Table for oci-ams-it-vnet-functions-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaaxsuuxi5bghbyfehskgnrgqijlqa43eswunz4wwjn3p2o6h5fepa)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaarhwhd2tsynji4cvrodhi5f2nmjicdarnvs5hmslsykn7oqjk5kvq"></a>
###### oci-ams-it-sl-functions-pro-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaarhwhd2tsynji4cvrodhi5f2nmjicdarnvs5hmslsykn7oqjk5kvq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | Todos       |           |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaat5lxjboiergdchgfowr7zqgo7g5gxay53x5gswojqrcyutq7yl2a"></a>
###### Default Security List for oci-ams-it-vnet-functions-pro (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaat5lxjboiergdchgfowr7zqgo7g5gxay53x5gswojqrcyutq7yl2a)

####### Reglas de Entrada

| Origen           | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0        | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0        | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.34.192/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                                  | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:----------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaab3uqwjuya4zw44kpkv5yjwos4fwocixqdmdjzamwlxhncr4pqoca | oci-ams-it-drgattach-vnet-functions-pro | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaasaar22q7zupr6xgqeki5utdjlcfffrqqtphxblojtnc57s3hvp5a"></a>
| ID                                                                                                   | Nombre                            | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:----------------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaasaar22q7zupr6xgqeki5utdjlcfffrqqtphxblojtnc57s3hvp5a | oci-ams-it-vngw-svc-functions-pro | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaweyhygwptai46wmh2xcqynumk5vyhivkxctfllhbdupa"></a>
#### Recursos de VCN: oci-ams-ot-vnet-mw-pro (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaweyhygwptai46wmh2xcqynumk5vyhivkxctfllhbdupa)

##### Subnets

| ID                                                                                           | Nombre                       | CIDR             | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                         | Route Table ID                                                                                   | Security Lists                                                                                                                   |
|:---------------------------------------------------------------------------------------------|:-----------------------------|:-----------------|:-----------------|:----------|:----------|:------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaa4vbx43xfqpieggblf5wxehr6omrj3rjukdlzzumxjljqx26df22q | oci-ams-ot-snet-mw-front-pro | 10.201.33.192/28 | Regional         | No        | AVAILABLE | [oci-ams-ot-udr-mw-front-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa2xkcmk6677iro3mv6737hygeotehwngg33whpwyyiwnipiniiv7a) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa2xkcmk6677iro3mv6737hygeotehwngg33whpwyyiwnipiniiv7a | [oci-ams-ot-sl-mw-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaae2i44tqicmc5onoaaurtmjvefxdksg2dgp6fs6uqm7dtqzaccfia) |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaazh3vnd44njhmbetsmhilazboynhearm4r5gvb6fnlmtmli26drnq | oci-ams-ot-snet-mw-back-pro  | 10.201.33.208/28 | Regional         | No        | AVAILABLE | [oci-ams-ot-udr-mw-back-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaavxe76czrqe65n4lrjao6jlfu6yn5a7r5iwasof4zh4oft5i2yjma)  | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaavxe76czrqe65n4lrjao6jlfu6yn5a7r5iwasof4zh4oft5i2yjma | [oci-ams-ot-sl-mw-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaae2i44tqicmc5onoaaurtmjvefxdksg2dgp6fs6uqm7dtqzaccfia) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaavxe76czrqe65n4lrjao6jlfu6yn5a7r5iwasof4zh4oft5i2yjma"></a>
###### oci-ams-ot-udr-mw-back-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaavxe76czrqe65n4lrjao6jlfu6yn5a7r5iwasof4zh4oft5i2yjma)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción                                                                          |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:-------------------------------------------------------------------------------------|
| 0.0.0.0/0             | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |                                                                                      |
| oci-ams-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaagsupe4z7xcvwvaj4vxa4a5hn7cgvf3jac4zyuuaacynj44miaaqa) | Service Gateway   | The run command needs acces to object storage when the script is stored in a abucket |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa2xkcmk6677iro3mv6737hygeotehwngg33whpwyyiwnipiniiv7a"></a>
###### oci-ams-ot-udr-mw-front-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa2xkcmk6677iro3mv6737hygeotehwngg33whpwyyiwnipiniiv7a)

No hay reglas de ruta definidas.

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaawvidgkjn3tncqnk4pjqza3ktvt2zns5umjkk722g3lhyxo5gia4q"></a>
###### Default Route Table for oci-ams-ot-vnet-mw-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaawvidgkjn3tncqnk4pjqza3ktvt2zns5umjkk722g3lhyxo5gia4q)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaae2i44tqicmc5onoaaurtmjvefxdksg2dgp6fs6uqm7dtqzaccfia"></a>
###### oci-ams-ot-sl-mw-pro-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaae2i44tqicmc5onoaaurtmjvefxdksg2dgp6fs6uqm7dtqzaccfia)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción       |
|:-----------|:-----------------|:------------|:----------|:------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22     |                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8080-8081 | tomcats           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3389-3389 | rdp for oleoducto |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping              |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaahe2dhzu26rvbcd5h2xo7zoravdf4kruyytkr6gobhrv6xtco7aoq"></a>
###### Default Security List for oci-ams-ot-vnet-mw-pro (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaahe2dhzu26rvbcd5h2xo7zoravdf4kruyytkr6gobhrv6xtco7aoq)

####### Reglas de Entrada

| Origen           | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0        | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0        | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.33.192/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                           | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaab6yp2escotsd22bdnv2haipwpo7v6lzrvuvbrhmxme5iaarzsaua | oci-ams-ot-drgattach-vnet-mw-pro | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaagsupe4z7xcvwvaj4vxa4a5hn7cgvf3jac4zyuuaacynj44miaaqa"></a>
| ID                                                                                                   | Nombre                     | Servicios              | Estado    |
|:-----------------------------------------------------------------------------------------------------|:---------------------------|:-----------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaagsupe4z7xcvwvaj4vxa4a5hn7cgvf3jac4zyuuaacynj44miaaqa | oci-ams-ot-vngw-svc-mw-pro | OCI AMS Object Storage | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqarmgitbkpdy5h5pwcyxd3gptxxhopq22bmqpp67rfmega"></a>
#### Recursos de VCN: oci-ams-it-vnet-mw-pro (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqarmgitbkpdy5h5pwcyxd3gptxxhopq22bmqpp67rfmega)

##### Subnets

| ID                                                                                           | Nombre                       | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                         | Route Table ID                                                                                   | Security Lists                                                                                                                   |
|:---------------------------------------------------------------------------------------------|:-----------------------------|:----------------|:-----------------|:----------|:----------|:------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaadahnag24iy5w3lxznvjooel3kwfq2vjtbq6yxbybnsvowacutota | oci-ams-it-snet-mw-back-pro  | 10.201.33.96/27 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-mw-back-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaap5kupa5qxks6ohuxthfspt4udljkgwux5mprlg6thzjugvjqu6fa)  | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaap5kupa5qxks6ohuxthfspt4udljkgwux5mprlg6thzjugvjqu6fa | [oci-ams-it-sl-mw-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaamnxvwnpnhpbrwsbidwmsk3afmk2wxu6tx5l5fget6soh2qkenta) |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaagzj4finflii23pe64gfyr6vgcuaunxxpqkaq5u4ersvhmhehmgqq | oci-ams-it-snet-mw-front-pro | 10.201.33.64/28 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-mw-front-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa3vcmns47nh5pjqxpxxhlfl426wlblmh4w2ulrky3cymk5gqbgpma) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa3vcmns47nh5pjqxpxxhlfl426wlblmh4w2ulrky3cymk5gqbgpma | [oci-ams-it-sl-mw-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaamnxvwnpnhpbrwsbidwmsk3afmk2wxu6tx5l5fget6soh2qkenta) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaap5kupa5qxks6ohuxthfspt4udljkgwux5mprlg6thzjugvjqu6fa"></a>
###### oci-ams-it-udr-mw-back-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaap5kupa5qxks6ohuxthfspt4udljkgwux5mprlg6thzjugvjqu6fa)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción                                                                          |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:-------------------------------------------------------------------------------------|
| 0.0.0.0/0             | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |                                                                                      |
| oci-ams-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaawkk3e3jqzobqxnrhsux75gzmqx6m5nswkutfpmqybrng65xfu4yq) | Service Gateway   | The run command needs acces to object storage when the script is stored in a abucket |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa3vcmns47nh5pjqxpxxhlfl426wlblmh4w2ulrky3cymk5gqbgpma"></a>
###### oci-ams-it-udr-mw-front-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa3vcmns47nh5pjqxpxxhlfl426wlblmh4w2ulrky3cymk5gqbgpma)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                        | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaez2jjhuwztnbngtawmmky7kt4yv6piggm7h2mcrgubsw5nikxukq"></a>
###### Default Route Table for oci-ams-it-vnet-mw-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaez2jjhuwztnbngtawmmky7kt4yv6piggm7h2mcrgubsw5nikxukq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaamnxvwnpnhpbrwsbidwmsk3afmk2wxu6tx5l5fget6soh2qkenta"></a>
###### oci-ams-it-sl-mw-pro-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaaamnxvwnpnhpbrwsbidwmsk3afmk2wxu6tx5l5fget6soh2qkenta)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción                                      |
|:-----------|:-----------------|:------------|:------------|:-------------------------------------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 5556-5556   | Node Manager Port                                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8393-8393   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8888-8888   | ohs forms                                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2048-2050   | traffic for ports: 2048-2050 nfs tcp             |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7001-7001   | Forms Admin Port                                 |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2370-2370   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 2048-2049   | traffic for ports: 2048-2050 nfs tcp             |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup                                     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                                                  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2368-2368   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8443-8443   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 17000-17040 | reports                                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 13080-13120 | control-m                                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3900-3900   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup                                     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8743-8743   | siada                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 111-111     | traffic for ports: 111 nfs tcp                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2372-2380   | control-m                                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 18080-18080 | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7777-7777   | ohs plain port                                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8081-8081   | siada                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8745-8745   | redef                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 12181-12181 | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6005-6005   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8007-8007   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8001-8002   | wls admin forms                                  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8543-8543   | forms                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2925-2925   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 19092-19092 | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2369-2369   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup                                     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7105-7106   | control-m server and em                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8744-8744   | silicie                                          |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8080-8083   | tomcats http for specific endpoints (db, devops) |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8084-8084   | siada                                            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 9001-9004   | wls managed servers forms and reports            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8002-8002   | Forms Admin Port                                 |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 111-111     | traffic for ports: 111 nfs tcp                   |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping                                             |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaam5atnupxpcbcrwlls4y6vfvcv52bizt7eheswwcwz46k3jllh2pa"></a>
###### Default Security List for oci-ams-it-vnet-mw-pro (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaam5atnupxpcbcrwlls4y6vfvcv52bizt7eheswwcwz46k3jllh2pa)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.33.64/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                           | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaajjqvazgfp5xqgopzucr4xisyigeakafcduo6bzs4zvkcco6bvqfq | oci-ams-it-drgattach-vnet-mw-pro | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaawkk3e3jqzobqxnrhsux75gzmqx6m5nswkutfpmqybrng65xfu4yq"></a>
| ID                                                                                                   | Nombre                     | Servicios              | Estado    |
|:-----------------------------------------------------------------------------------------------------|:---------------------------|:-----------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaawkk3e3jqzobqxnrhsux75gzmqx6m5nswkutfpmqybrng65xfu4yq | oci-ams-it-vngw-svc-mw-pro | OCI AMS Object Storage | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaojplkm7p4ywh42abafmkq4xkti7qmzwh4ebo2avp53la"></a>
#### Recursos de VCN: oci-ams-ot-vnet-db-pro (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaojplkm7p4ywh42abafmkq4xkti7qmzwh4ebo2avp53la)

##### Subnets

| ID                                                                                           | Nombre                     | CIDR             | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                       | Route Table ID                                                                                   | Security Lists                                                                                                                   |
|:---------------------------------------------------------------------------------------------|:---------------------------|:-----------------|:-----------------|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaayvi2r2gayv25saewbwvejxt3erfwyq56edfsd27tbuasrvderisq | oci-ams-ot-snet-db-svc-pro | 10.201.32.192/27 | Regional         | No        | AVAILABLE | [oci-ams-ot-udr-db-svc-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaazwshhcljti3ju5rqjpxmi7xnvnc6b4cqrbrwyfjxqxcnd64jmzja) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaazwshhcljti3ju5rqjpxmi7xnvnc6b4cqrbrwyfjxqxcnd64jmzja | [oci-ams-ot-sl-db-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaggxcvx5erehgs36abk4fx7xsbziulr6ol37gx6uw7yl4fwchp6qq) |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaaomct3ix3ahc3ce2z3va327pls63ir3q4ygcjkoizhnqf2gsyxx6q | oci-ams-ot-snet-db-bck-pro | 10.201.32.224/28 | Regional         | No        | AVAILABLE | [oci-ams-ot-udr-db-bck-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaayi2qdpgpujx3z26m2welh2lr2glwp5whq6kyk7v6ig4triklkkmq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaayi2qdpgpujx3z26m2welh2lr2glwp5whq6kyk7v6ig4triklkkmq | [oci-ams-ot-sl-db-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaggxcvx5erehgs36abk4fx7xsbziulr6ol37gx6uw7yl4fwchp6qq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaayi2qdpgpujx3z26m2welh2lr2glwp5whq6kyk7v6ig4triklkkmq"></a>
###### oci-ams-ot-udr-db-bck-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaayi2qdpgpujx3z26m2welh2lr2glwp5whq6kyk7v6ig4triklkkmq)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-ams-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaalb6slbbvna3vx52z2d4qwyeqxoyrsjt75d7fpunjprsvcw2gqhmq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaazwshhcljti3ju5rqjpxmi7xnvnc6b4cqrbrwyfjxqxcnd64jmzja"></a>
###### oci-ams-ot-udr-db-svc-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaazwshhcljti3ju5rqjpxmi7xnvnc6b4cqrbrwyfjxqxcnd64jmzja)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-ams-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaalb6slbbvna3vx52z2d4qwyeqxoyrsjt75d7fpunjprsvcw2gqhmq) | Service Gateway   |               |
| 0.0.0.0/0             | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaal3vkmbtmmocmz3pphjyyib2fpotkejghz5jbtnmhu4wc34odosga"></a>
###### Default Route Table for oci-ams-ot-vnet-db-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaal3vkmbtmmocmz3pphjyyib2fpotkejghz5jbtnmhu4wc34odosga)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaggxcvx5erehgs36abk4fx7xsbziulr6ol37gx6uw7yl4fwchp6qq"></a>
###### oci-ams-ot-sl-db-pro-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaaggxcvx5erehgs36abk4fx7xsbziulr6ol37gx6uw7yl4fwchp6qq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción    |
|:-----------|:-----------------|:------------|:------------|:---------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 1363-1364   | connect direct |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 52311-52311 | besclient      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7106-7106   | connect direct |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 4772-4772   | db listener    |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 52311-52311 | besclient      |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup   |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaafh3o52zsefezdjobmcxqls33izuhgju2gypddmaop7longbxxvaq"></a>
###### Default Security List for oci-ams-ot-vnet-db-pro (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaafh3o52zsefezdjobmcxqls33izuhgju2gypddmaop7longbxxvaq)

####### Reglas de Entrada

| Origen           | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0        | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0        | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.32.192/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                           | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaactymilykvbz74guqmngwkhgad7hk5bojdprwwr4u4gp44deogmuq | oci-ams-ot-drgattach-vnet-db-pro | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaalb6slbbvna3vx52z2d4qwyeqxoyrsjt75d7fpunjprsvcw2gqhmq"></a>
| ID                                                                                                   | Nombre                  | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaalb6slbbvna3vx52z2d4qwyeqxoyrsjt75d7fpunjprsvcw2gqhmq | oci-ams-ot-vngw-svc-pro | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaebgsjzpxg26bf6nevmi6prnl52mqx25dnxv6b4mpllpa"></a>
#### Recursos de VCN: oci-ams-it-vnet-db-pro (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaebgsjzpxg26bf6nevmi6prnl52mqx25dnxv6b4mpllpa)

##### Subnets

| ID                                                                                           | Nombre                     | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                       | Route Table ID                                                                                   | Security Lists                                                                                                                   |
|:---------------------------------------------------------------------------------------------|:---------------------------|:----------------|:-----------------|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaabc5fz6ph2b45xwehslbaed6gnoqbkpftkbdvcotfqtbpqgxq6q7a | oci-ams-it-snet-db-svc-pro | 10.201.32.64/27 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-db-svc-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaapofh3gua34i2cpl23tmtzsdbdcp4mej37b2g2pxcdor4nzmufvwq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaapofh3gua34i2cpl23tmtzsdbdcp4mej37b2g2pxcdor4nzmufvwq | [oci-ams-it-sl-db-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaadb53cqylysxcfa33qfvdki22neacfzcspeqlpjmn2f73tfaexueq) |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaarjybg2iplirhej3xjussnoxo56koyfrwxsnclw7sjl4gt3evkama | oci-ams-it-snet-db-bck-pro | 10.201.32.96/28 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-db-bck-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaar54ilrrhqlxnhuacctbjvwqil7uhfblk2yof7plo3lxmuvoowu4q) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaar54ilrrhqlxnhuacctbjvwqil7uhfblk2yof7plo3lxmuvoowu4q | [oci-ams-it-sl-db-pro-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaadb53cqylysxcfa33qfvdki22neacfzcspeqlpjmn2f73tfaexueq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaar54ilrrhqlxnhuacctbjvwqil7uhfblk2yof7plo3lxmuvoowu4q"></a>
###### oci-ams-it-udr-db-bck-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaar54ilrrhqlxnhuacctbjvwqil7uhfblk2yof7plo3lxmuvoowu4q)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-ams-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaavetjzdzicg776cijvnjnrdervpsdyhntvckwegnqvhkn3w6bdyiq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaapofh3gua34i2cpl23tmtzsdbdcp4mej37b2g2pxcdor4nzmufvwq"></a>
###### oci-ams-it-udr-db-svc-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaapofh3gua34i2cpl23tmtzsdbdcp4mej37b2g2pxcdor4nzmufvwq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |
| all-ams-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaavetjzdzicg776cijvnjnrdervpsdyhntvckwegnqvhkn3w6bdyiq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaal7nbcaxjvgmbi7ed5af7xrcct3xduwpjbnm7gc2crq4zjipmuoxa"></a>
###### Default Route Table for oci-ams-it-vnet-db-pro (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaal7nbcaxjvgmbi7ed5af7xrcct3xduwpjbnm7gc2crq4zjipmuoxa)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaadb53cqylysxcfa33qfvdki22neacfzcspeqlpjmn2f73tfaexueq"></a>
###### oci-ams-it-sl-db-pro-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaadb53cqylysxcfa33qfvdki22neacfzcspeqlpjmn2f73tfaexueq)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos     | Descripción                          |
|:----------------|:-----------------|:------------|:------------|:-------------------------------------|
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 1363-1364   | connect direct                       |
| 10.0.0.0/8      | CIDR_BLOCK       | UDP         | 52311-52311 | besclient                            |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 22-22       |                                      |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 52311-52311 | besclient                            |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 4771-4771   | db listener                          |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 7106-7106   | control-m                            |
| 10.0.0.0/8      | CIDR_BLOCK       | ICMP        |             | ping                                 |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 20-21       | FTP de Aviación y de Tierra          |
| 10.201.32.64/27 | CIDR_BLOCK       | UDP         | 111-111     | Temporal rule for database migration |
| 10.201.32.64/27 | CIDR_BLOCK       | UDP         | 2048-2048   | Temporal rule for database migration |
| 10.201.32.64/27 | CIDR_BLOCK       | TCP         | 111-111     | Temporal rule for database migration |
| 10.201.32.64/27 | CIDR_BLOCK       | TCP         | 2028-2028   | Temporal rule for database migration |
| 10.201.32.64/27 | CIDR_BLOCK       | TCP         | 2049-2049   | Temporal rule for database migration |
| 10.201.32.64/27 | CIDR_BLOCK       | TCP         | 2050-2050   | Temporal rule for database migration |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup                         |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup                         |
| 10.0.0.0/8      | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup                         |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaoaq3koudwnsoj3g43atkd2f3hoy75z27rm6tnagrxxjitvfzawzq"></a>
###### Default Security List for oci-ams-it-vnet-db-pro (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaaoaq3koudwnsoj3g43atkd2f3hoy75z27rm6tnagrxxjitvfzawzq)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.32.64/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                           | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaayll72ij2s6644dyz7qcxrn6wd2xqny7jwdqkxl3ieaju54jg7hva | oci-ams-it-drgattach-vnet-db-pro | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaavetjzdzicg776cijvnjnrdervpsdyhntvckwegnqvhkn3w6bdyiq"></a>
| ID                                                                                                   | Nombre                     | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:---------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaavetjzdzicg776cijvnjnrdervpsdyhntvckwegnqvhkn3w6bdyiq | oci-ams-it-vngw-svc-db-pro | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaeccutpjlmlmk635jpba37qcmoomhcfl7cmvze43xvqsq"></a>
#### Recursos de VCN: oci-ams-it-vnet-tools-stg (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaeccutpjlmlmk635jpba37qcmoomhcfl7cmvze43xvqsq)

##### Subnets

| ID                                                                                           | Nombre                    | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                      | Route Table ID                                                                                   | Security Lists                                                                                                                      |
|:---------------------------------------------------------------------------------------------|:--------------------------|:----------------|:-----------------|:----------|:----------|:---------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaa4gwm5wsnoy3qkebzflsqyfmvnjlrksyzwj4k6hxcojiukcoxosra | oci-ams-it-snet-tools-stg | 10.201.38.64/26 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-tools-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaarnmwnvw2ohiwh7yz4mfgb5zvpvttiptt6fppgmgfezbswailxanq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaarnmwnvw2ohiwh7yz4mfgb5zvpvttiptt6fppgmgfezbswailxanq | [oci-ams-it-sl-tools-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanz3e7ki37c5x7z2btrfuggp7miwmoc6mqd6epho4erb7d6d45mra) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaarnmwnvw2ohiwh7yz4mfgb5zvpvttiptt6fppgmgfezbswailxanq"></a>
###### oci-ams-it-udr-tools-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaarnmwnvw2ohiwh7yz4mfgb5zvpvttiptt6fppgmgfezbswailxanq)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                        | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaabbgnpz3wfctqewlj3rkfwzqr3l4gbpn6l65cy2k6fifmronwfmea"></a>
###### Default Route Table for oci-ams-it-vnet-tools-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaabbgnpz3wfctqewlj3rkfwzqr3l4gbpn6l65cy2k6fifmronwfmea)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanz3e7ki37c5x7z2btrfuggp7miwmoc6mqd6epho4erb7d6d45mra"></a>
###### oci-ams-it-sl-tools-stg-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaanz3e7ki37c5x7z2btrfuggp7miwmoc6mqd6epho4erb7d6d45mra)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22     |               |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3761-3761 |               |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping          |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaa3kxkfdoax3h27ltt65go4vb27dblftf6gyqy3nvlyux2tu4aa65a"></a>
###### Default Security List for oci-ams-it-vnet-tools-stg (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaa3kxkfdoax3h27ltt65go4vb27dblftf6gyqy3nvlyux2tu4aa65a)

####### Reglas de Entrada

| Origen          | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0       | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0       | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.38.64/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                              | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaaraes67z6l3mqsqryphr5pkut5rzcixim5m4lyl3t73dyyn6ga6zq | oci-ams-it-drgattach-vnet-tools-stg | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqayzueatthiz3v6ls2qfqge3pedyyusuve4ddytnwwbmfa"></a>
#### Recursos de VCN: oci-ams-ot-vnet-mw-stg (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqayzueatthiz3v6ls2qfqge3pedyyusuve4ddytnwwbmfa)

##### Subnets

| ID                                                                                           | Nombre                       | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                         | Route Table ID                                                                                   | Security Lists                                                                                                                   |
|:---------------------------------------------------------------------------------------------|:-----------------------------|:----------------|:-----------------|:----------|:----------|:------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaaaf6vc3fybwyvf42ijtt7pxdyuqsmv7smjo57nu66i4w3bgtxbgzq | oci-ams-ot-snet-mw-back-stg  | 10.201.34.16/28 | Regional         | No        | AVAILABLE | [oci-ams-ot-udr-mw-back-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa62eifqvuqt3uoeg7krnajmdctbpli45pffou6dxakf3orhchajta)  | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa62eifqvuqt3uoeg7krnajmdctbpli45pffou6dxakf3orhchajta | [oci-ams-ot-sl-mw-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanfxqfzpqrgvt6ssvol4us2h6gh754tji3me4ig4mzzbz62xcgdsa) |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaazz6f73tvvjd3djzpuxc2cgcgwkb3av4fviwy7n24tamdf3hz2zcq | oci-ams-ot-snet-mw-front-stg | 10.201.34.0/28  | Regional         | No        | AVAILABLE | [oci-ams-ot-udr-mw-front-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaykuq332s5x3bgexo5mj6kkxlsy75wkvitc7b2inmyzfwrfywoq5q) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaykuq332s5x3bgexo5mj6kkxlsy75wkvitc7b2inmyzfwrfywoq5q | [oci-ams-ot-sl-mw-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanfxqfzpqrgvt6ssvol4us2h6gh754tji3me4ig4mzzbz62xcgdsa) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa62eifqvuqt3uoeg7krnajmdctbpli45pffou6dxakf3orhchajta"></a>
###### oci-ams-ot-udr-mw-back-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa62eifqvuqt3uoeg7krnajmdctbpli45pffou6dxakf3orhchajta)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                        | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaykuq332s5x3bgexo5mj6kkxlsy75wkvitc7b2inmyzfwrfywoq5q"></a>
###### oci-ams-ot-udr-mw-front-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaykuq332s5x3bgexo5mj6kkxlsy75wkvitc7b2inmyzfwrfywoq5q)

No hay reglas de ruta definidas.

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaapzejwpctxwhoitxkahkrtfd5o2v6dsww6s5ljraamr2lhq43awaq"></a>
###### Default Route Table for oci-ams-ot-vnet-mw-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaapzejwpctxwhoitxkahkrtfd5o2v6dsww6s5ljraamr2lhq43awaq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanfxqfzpqrgvt6ssvol4us2h6gh754tji3me4ig4mzzbz62xcgdsa"></a>
###### oci-ams-ot-sl-mw-stg-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaanfxqfzpqrgvt6ssvol4us2h6gh754tji3me4ig4mzzbz62xcgdsa)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción       |
|:-----------|:-----------------|:------------|:----------|:------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7080-7081 | tomcats           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22     |                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162 | Veeam Backup      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3389-3389 | rdp for oleoducto |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |           | ping              |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanonulin2znhgfjnb5leu5rv7azpfxidgqbe7v7yhgzmb64n2vqkq"></a>
###### Default Security List for oci-ams-ot-vnet-mw-stg (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaanonulin2znhgfjnb5leu5rv7azpfxidgqbe7v7yhgzmb64n2vqkq)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.34.0/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                           | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaavyv5dzia4oedsldwbdlemp7wjze7yettyo2bqt6ddzqhm2zbmmwa | oci-ams-ot-drgattach-vnet-mw-stg | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqavkpxggb7lunwrptanl6tndqjuj3netvdjgc5enhq7rfa"></a>
#### Recursos de VCN: oci-ams-it-vnet-mw-stg (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqavkpxggb7lunwrptanl6tndqjuj3netvdjgc5enhq7rfa)

##### Subnets

| ID                                                                                           | Nombre                       | CIDR             | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                         | Route Table ID                                                                                   | Security Lists                                                                                                                   |
|:---------------------------------------------------------------------------------------------|:-----------------------------|:-----------------|:-----------------|:----------|:----------|:------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaays2bgoqiqi2exsvl365ccfestln2cctbmyyba74xuwrmuu5t62eq | oci-ams-it-snet-mw-front-stg | 10.201.33.128/28 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-mw-front-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa656j5ghzilnnscurvccynk63kvflgr7ya6ibbgh5s4svd2c6mdxa) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa656j5ghzilnnscurvccynk63kvflgr7ya6ibbgh5s4svd2c6mdxa | [oci-ams-it-sl-mw-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaa3ygg7ybjbdvt5oz7djxi4hcnucvccnkp2rynnqxajnwp6fldz3bq) |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaarol4iozhqlk2pb2fnhqgzexfgysygvdptgqpp72af4zsuld5kopq | oci-ams-it-snet-mw-back-stg  | 10.201.33.144/28 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-mw-back-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaasxgloorj4bxsl3l4gjknlj6b2n7w7ysaamn45x2ndpmfuu4nyaka)  | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaasxgloorj4bxsl3l4gjknlj6b2n7w7ysaamn45x2ndpmfuu4nyaka | [oci-ams-it-sl-mw-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaa3ygg7ybjbdvt5oz7djxi4hcnucvccnkp2rynnqxajnwp6fldz3bq) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaasxgloorj4bxsl3l4gjknlj6b2n7w7ysaamn45x2ndpmfuu4nyaka"></a>
###### oci-ams-it-udr-mw-back-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaasxgloorj4bxsl3l4gjknlj6b2n7w7ysaamn45x2ndpmfuu4nyaka)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                        | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa656j5ghzilnnscurvccynk63kvflgr7ya6ibbgh5s4svd2c6mdxa"></a>
###### oci-ams-it-udr-mw-front-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa656j5ghzilnnscurvccynk63kvflgr7ya6ibbgh5s4svd2c6mdxa)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                        | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | DRG               |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaabizzf25f4i7qbtngn3bbp64j4h3jtl46xv4ocnkv64ut42nqqgfq"></a>
###### Default Route Table for oci-ams-it-vnet-mw-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaabizzf25f4i7qbtngn3bbp64j4h3jtl46xv4ocnkv64ut42nqqgfq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaa3ygg7ybjbdvt5oz7djxi4hcnucvccnkp2rynnqxajnwp6fldz3bq"></a>
###### oci-ams-it-sl-mw-stg-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaa3ygg7ybjbdvt5oz7djxi4hcnucvccnkp2rynnqxajnwp6fldz3bq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción             |
|:-----------|:-----------------|:------------|:------------|:------------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8393-8393   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2370-2370   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                         |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2368-2368   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8443-8443   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 9002-9002   | wls managed reports     |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6743-6743   |                         |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 3900-3900   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 18080-18080 | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 1000-1050   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2048-2050   | nfs tcp                 |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 12181-12181 | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6005-6005   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 8007-8007   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7777-7777   |                         |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7743-7745   |                         |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2925-2925   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 19092-19092 | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7106-7106   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7105-7105   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 2048-2049   | nfs udp                 |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2369-2369   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup            |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7105-7106   | control-m server and em |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 9001-9001   | wls managed forms       |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 111-111     | nfs udp                 |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7543-7543   |                         |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7080-7083   |                         |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7001-7002   | wls adminserver         |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 111-111     | nfs tcp                 |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping                    |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanzmlservlfouop5ymja7g7stmb3synhifh3p46ztufhmac6bwn7a"></a>
###### Default Security List for oci-ams-it-vnet-mw-stg (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaanzmlservlfouop5ymja7g7stmb3synhifh3p46ztufhmac6bwn7a)

####### Reglas de Entrada

| Origen           | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0        | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0        | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.33.128/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                           | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaafogr6npefrwj3ccodpwyloboo7fjj7dnd6ru56i5u2ysxkntbyba | oci-ams-it-drgattach-vnet-mw-stg | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

No se encontraron Service Gateways en esta VCN.

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaumsllyvdgfkyo3rfgrx2nb2taecrqanopuy3x33omgga"></a>
#### Recursos de VCN: oci-ams-ot-vnet-db-stg (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaumsllyvdgfkyo3rfgrx2nb2taecrqanopuy3x33omgga)

##### Subnets

| ID                                                                                           | Nombre                     | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                       | Route Table ID                                                                                   | Security Lists                                                                                                                   |
|:---------------------------------------------------------------------------------------------|:---------------------------|:----------------|:-----------------|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaajrlgy37gxci5fgsxp2uvezstnaxgglezvbrbf5p2jopdxdzv7uha | oci-ams-ot-snet-db-bck-stg | 10.201.33.32/28 | Regional         | No        | AVAILABLE | [oci-ams-ot-udr-db-bck-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaapwuzrkbc5lr3dhsb4fucguhzaau4jgb6qxfpqtssuojkmtegqapa) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaapwuzrkbc5lr3dhsb4fucguhzaau4jgb6qxfpqtssuojkmtegqapa | [oci-ams-ot-sl-db-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaah6tfhfma34l2bzfndofes3lzixgo2yu34pdpkecwedvv7lmmia6a) |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaallxtefr4gjb457adr2kce7bc3p5k7kmolycvmjbz3k77gbxxorkq | oci-ams-ot-snet-db-svc-stg | 10.201.33.0/27  | Regional         | No        | AVAILABLE | [oci-ams-ot-udr-db-svc-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaapw5myhvuwhymhqadcaga3qz565jc5e6zgjiu5llpwphbyejj6jvq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaapw5myhvuwhymhqadcaga3qz565jc5e6zgjiu5llpwphbyejj6jvq | [oci-ams-ot-sl-db-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaah6tfhfma34l2bzfndofes3lzixgo2yu34pdpkecwedvv7lmmia6a) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaapwuzrkbc5lr3dhsb4fucguhzaau4jgb6qxfpqtssuojkmtegqapa"></a>
###### oci-ams-ot-udr-db-bck-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaapwuzrkbc5lr3dhsb4fucguhzaau4jgb6qxfpqtssuojkmtegqapa)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-ams-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaekq3ue2clhptuwvh4ycfc44wwkksubcw2fjldsfimltrdljfihfa) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaapw5myhvuwhymhqadcaga3qz565jc5e6zgjiu5llpwphbyejj6jvq"></a>
###### oci-ams-ot-udr-db-svc-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaapw5myhvuwhymhqadcaga3qz565jc5e6zgjiu5llpwphbyejj6jvq)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0             | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |
| oci-ams-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaekq3ue2clhptuwvh4ycfc44wwkksubcw2fjldsfimltrdljfihfa) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaaa4b7oy3hufxziz7mqcg452qj63l6fqqfluys4xtduskcn2pjusq"></a>
###### Default Route Table for oci-ams-ot-vnet-db-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaaa4b7oy3hufxziz7mqcg452qj63l6fqqfluys4xtduskcn2pjusq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaah6tfhfma34l2bzfndofes3lzixgo2yu34pdpkecwedvv7lmmia6a"></a>
###### oci-ams-ot-sl-db-stg-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaah6tfhfma34l2bzfndofes3lzixgo2yu34pdpkecwedvv7lmmia6a)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción    |
|:-----------|:-----------------|:------------|:------------|:---------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 1363-1364   | connect direct |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 52311-52311 | besclient      |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 7106-7106   | connect direct |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 4762-4762   | db listener    |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 52311-52311 | besclient      |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup   |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaapeho7shz3xmrovm3gxo6olxqnqorn2ldqswfr5xk7b255ighpu7q"></a>
###### Default Security List for oci-ams-ot-vnet-db-stg (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaapeho7shz3xmrovm3gxo6olxqnqorn2ldqswfr5xk7b255ighpu7q)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.33.0/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                           | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaavr3ysndhiyqaplludsun2q5zgmcu5br6m2k2ntruomczevqz3eba | oci-ams-ot-drgattach-vnet-db-stg | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaekq3ue2clhptuwvh4ycfc44wwkksubcw2fjldsfimltrdljfihfa"></a>
| ID                                                                                                   | Nombre                     | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:---------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaaekq3ue2clhptuwvh4ycfc44wwkksubcw2fjldsfimltrdljfihfa | oci-ams-ot-vngw-svc-db-stg | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaczixf26gyqw4o7p2mnwhd2cx2k2e6uhgzcgy7kcg3kfq"></a>
#### Recursos de VCN: oci-ams-it-vnet-db-stg (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaczixf26gyqw4o7p2mnwhd2cx2k2e6uhgzcgy7kcg3kfq)

##### Subnets

| ID                                                                                           | Nombre                     | CIDR             | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                       | Route Table ID                                                                                   | Security Lists                                                                                                                   |
|:---------------------------------------------------------------------------------------------|:---------------------------|:-----------------|:-----------------|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaalk4ngxxdndxkxhq627fsquy5w4o2coyqgovuhmp3i2dhwtpqznta | oci-ams-it-snet-db-bck-stg | 10.201.32.160/28 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-db-bck-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaag2wumu2cpuawpjbupqh53ymo667se5fmlk472r33t7hfmui6lcpq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaag2wumu2cpuawpjbupqh53ymo667se5fmlk472r33t7hfmui6lcpq | [oci-ams-it-sl-db-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaayz5nrjtm3mmnq2tetqauqeospxffendrbbsq5qv7ch4teaz5qtwa) |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaadw2hzplqleupadi5dqo6ulgdfdg54ygpt52mzgccmjdmcp7wqzua | oci-ams-it-snet-db-svc-stg | 10.201.32.128/27 | Regional         | No        | AVAILABLE | [oci-ams-it-udr-db-svc-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaajno33vz2zzvczi2fba2k3hbc4tam2dhsmp54hgy62c6l7hikifuq) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaajno33vz2zzvczi2fba2k3hbc4tam2dhsmp54hgy62c6l7hikifuq | [oci-ams-it-sl-db-stg-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaayz5nrjtm3mmnq2tetqauqeospxffendrbbsq5qv7ch4teaz5qtwa) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaag2wumu2cpuawpjbupqh53ymo667se5fmlk472r33t7hfmui6lcpq"></a>
###### oci-ams-it-udr-db-bck-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaag2wumu2cpuawpjbupqh53ymo667se5fmlk472r33t7hfmui6lcpq)

| Destino               | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:----------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| oci-ams-objectstorage | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaj5mat3vtxuhk5frlaejofno2fsgmc7j6gd5ukj4qfer5sq4y7pjq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaajno33vz2zzvczi2fba2k3hbc4tam2dhsmp54hgy62c6l7hikifuq"></a>
###### oci-ams-it-udr-db-svc-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaajno33vz2zzvczi2fba2k3hbc4tam2dhsmp54hgy62c6l7hikifuq)

| Destino                                     | Tipo de Destino    | Entidad de Red                                                                                                               | Tipo de Entidad   | Descripción   |
|:--------------------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0                                   | CIDR_BLOCK         | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                        | DRG               |               |
| all-ams-services-in-oracle-services-network | SERVICE_CIDR_BLOCK | [Service Gateway](#sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaj5mat3vtxuhk5frlaejofno2fsgmc7j6gd5ukj4qfer5sq4y7pjq) | Service Gateway   |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaamwxqkcfnsgqwbigoxme5akfimpnwaygnpc72fvbcsk427jrzeggq"></a>
###### Default Route Table for oci-ams-it-vnet-db-stg (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaamwxqkcfnsgqwbigoxme5akfimpnwaygnpc72fvbcsk427jrzeggq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaayz5nrjtm3mmnq2tetqauqeospxffendrbbsq5qv7ch4teaz5qtwa"></a>
###### oci-ams-it-sl-db-stg-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaayz5nrjtm3mmnq2tetqauqeospxffendrbbsq5qv7ch4teaz5qtwa)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos     | Descripción                 |
|:-----------|:-----------------|:------------|:------------|:----------------------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 1363-1364   | connect direct              |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 52311-52311 | besclient                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22       |                             |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 52311-52311 | besclient                   |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 4761-4761   | db listener                 |
| 10.0.0.0/8 | CIDR_BLOCK       | UDP         | 7106-7106   | control-m                   |
| 10.0.0.0/8 | CIDR_BLOCK       | ICMP        |             | ping                        |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 20-21       | FTP de Aviación y de Tierra |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160   | Veeam Backup                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162   | Veeam Backup                |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300   | Veeam Backup                |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaapwtscym4x4mdlmqxgkbkl2gq253wwpczdggji5xhyaucdpd2arba"></a>
###### Default Security List for oci-ams-it-vnet-db-stg (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaapwtscym4x4mdlmqxgkbkl2gq253wwpczdggji5xhyaucdpd2arba)

####### Reglas de Entrada

| Origen           | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0        | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0        | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.32.128/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                           | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaa4v2jqsqorqpb4e7bbdjtsooc27r6liq354o3vgqcug6nt4yakoaa | oci-ams-it-drgattach-vnet-db-stg | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

No se encontraron Internet Gateways en esta VCN.

##### NAT Gateways

No se encontraron NAT Gateways en esta VCN.

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaaj5mat3vtxuhk5frlaejofno2fsgmc7j6gd5ukj4qfer5sq4y7pjq"></a>
| ID                                                                                                   | Nombre                     | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:---------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaaj5mat3vtxuhk5frlaejofno2fsgmc7j6gd5ukj4qfer5sq4y7pjq | oci-ams-it-vngw-svc-db-stg | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqabpiciz67q2ud5hpn2i3eqzv7pwgqcsoynovow26kzfvq"></a>
#### Recursos de VCN: oci-ams-vnet-hub-sha (ID: ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqabpiciz67q2ud5hpn2i3eqzv7pwgqcsoynovow26kzfvq)

##### Subnets

| ID                                                                                           | Nombre                   | CIDR            | Disponibilidad   | Pública   | Estado    | Route Table                                                                                                                     | Route Table ID                                                                                   | Security Lists                                                                                                                                           |
|:---------------------------------------------------------------------------------------------|:-------------------------|:----------------|:-----------------|:----------|:----------|:--------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaamtnqo352wspylkbteo42zermt5cge2ydcdvv6uumbhaqd37e2k4q | oci-ams-snet-hub-int-sha | 10.201.32.32/28 | Regional         | No        | AVAILABLE | [oci-ams-udr-hub-int-sha](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa3pbpbbpva6susjspc2ecuisdig3djh2gaj3u3wxdesiwvzcaxqla) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa3pbpbbpva6susjspc2ecuisdig3djh2gaj3u3wxdesiwvzcaxqla | [oci-ams-sl-hub-int-sha-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaar3zkals63jl6n4s22b26sjrqpguivwnnpkcy6rtf4luqcctvoghq)                       |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaa2fwliaxfru6i3sca4mhsrks45dnjmcaouansqld7zshhrdutyufq | oci-ams-snet-hub-fw-sha  | 10.201.32.0/28  | Regional         | No        | AVAILABLE | [oci-ams-udr-hub-fw-sha](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaawhhcaueskwz4orxozegrslegnqfmv2aczxyz7ryov3ashm6prqdq)  | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaawhhcaueskwz4orxozegrslegnqfmv2aczxyz7ryov3ashm6prqdq | [oci-ams-sl-hub-fw-all-sha-1](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanio5mombhijhwdcqi7j6l64n7ogmb6pmbl3kzadbjhunxsxyndlq)                    |
| ocid1.subnet.oc1.eu-amsterdam-1.aaaaaaaapcapw72bcdyhbypu2cfjsj4qprwymgu3p37g22ldylnaalq6y4ga | oci-ams-snet-hub-dmz-sha | 10.201.32.16/28 | Regional         | Sí        | AVAILABLE | [oci-ams-udr-hub-dmz-sha](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaajwkh3j6tz73gtaf4ams5tk7kwt5lo3nnszldmkox4mpowo24hdoa) | ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaajwkh3j6tz73gtaf4ams5tk7kwt5lo3nnszldmkox4mpowo24hdoa | [Default Security List for oci-ams-vnet-hub-sha](#sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaoqndnwqtlzuh5oq2po6frubsccz2ycxnjqzshkha2reoiqcdccoa) |

##### Tablas de Rutas

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa3pbpbbpva6susjspc2ecuisdig3djh2gaj3u3wxdesiwvzcaxqla"></a>
###### oci-ams-udr-hub-int-sha (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaa3pbpbbpva6susjspc2ecuisdig3djh2gaj3u3wxdesiwvzcaxqla)

| Destino    | Tipo de Destino   | Entidad de Red                                                                                                       | Tipo de Entidad   | Descripción   |
|:-----------|:------------------|:---------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                | DRG               |               |
| 0.0.0.0/0  | CIDR_BLOCK        | [NAT Gateway](#nat-ocid1_natgateway_oc1_eu_amsterdam_1_aaaaaaaa6bgehrsbciikripfqyqi5ts2rup4ggjh5gpwqrt7rumlgrv7lrna) | NAT Gateway       |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaawhhcaueskwz4orxozegrslegnqfmv2aczxyz7ryov3ashm6prqdq"></a>
###### oci-ams-udr-hub-fw-sha (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaawhhcaueskwz4orxozegrslegnqfmv2aczxyz7ryov3ashm6prqdq)

| Destino    | Tipo de Destino   | Entidad de Red                                                                                                       | Tipo de Entidad   | Descripción   |
|:-----------|:------------------|:---------------------------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK        | [DRG](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa)                | DRG               |               |
| 0.0.0.0/0  | CIDR_BLOCK        | [NAT Gateway](#nat-ocid1_natgateway_oc1_eu_amsterdam_1_aaaaaaaa6bgehrsbciikripfqyqi5ts2rup4ggjh5gpwqrt7rumlgrv7lrna) | NAT Gateway       |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaajwkh3j6tz73gtaf4ams5tk7kwt5lo3nnszldmkox4mpowo24hdoa"></a>
###### oci-ams-udr-hub-dmz-sha (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaajwkh3j6tz73gtaf4ams5tk7kwt5lo3nnszldmkox4mpowo24hdoa)

No hay reglas de ruta definidas.

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaazwqyvapmtqphrjk7mrjw4flst3iox6ko7zu46vkdys34gsk2kmcq"></a>
###### oci-ams-udr-hub-vngw-nat-sha (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaazwqyvapmtqphrjk7mrjw4flst3iox6ko7zu46vkdys34gsk2kmcq)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                  | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | ocid1.privateip.oc1.eu-amsterdam-1.abqw2ljrxvtde2klt2edmi3jugm4l4da2u3cwxhaku24hwutixj6nlitulua | Desconocido       |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaqos27ui3kbmxlaocmbabqkkybp6fjntoexwoeqg6g2qsacwqxjqa"></a>
###### oci-ams-udr-hub-vngw-inet-sha (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaqos27ui3kbmxlaocmbabqkkybp6fjntoexwoeqg6g2qsacwqxjqa)

No hay reglas de ruta definidas.

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaamnmkfba4q5zukwqcu2amcrwmk23tfgqjmjd53kpfvxyvjod36tra"></a>
###### oci-ams-udr-hub-ingress-sha (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaamnmkfba4q5zukwqcu2amcrwmk23tfgqjmjd53kpfvxyvjod36tra)

| Destino   | Tipo de Destino   | Entidad de Red                                                                                  | Tipo de Entidad   | Descripción   |
|:----------|:------------------|:------------------------------------------------------------------------------------------------|:------------------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | ocid1.privateip.oc1.eu-amsterdam-1.abqw2ljrxvtde2klt2edmi3jugm4l4da2u3cwxhaku24hwutixj6nlitulua | Desconocido       |               |

<a id="rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaakrtu6wnh6r5jpgzyv2a2amkhicigaddvcutcae7weud5er2abdq"></a>
###### Default Route Table for oci-ams-vnet-hub-sha (ID: ocid1.routetable.oc1.eu-amsterdam-1.aaaaaaaaakrtu6wnh6r5jpgzyv2a2amkhicigaddvcutcae7weud5er2abdq)

No hay reglas de ruta definidas.

##### Security Lists

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaar3zkals63jl6n4s22b26sjrqpguivwnnpkcy6rtf4luqcctvoghq"></a>
###### oci-ams-sl-hub-int-sha-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaar3zkals63jl6n4s22b26sjrqpguivwnnpkcy6rtf4luqcctvoghq)

####### Reglas de Entrada

| Origen     | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:-----------|:-----------------|:------------|:----------|:--------------|
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 2500-3300 | Veeam Backup  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6160-6160 | Veeam Backup  |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 22-22     | SSH           |
| 10.0.0.0/8 | CIDR_BLOCK       | TCP         | 6162-6162 | Veeam Backup  |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaanio5mombhijhwdcqi7j6l64n7ogmb6pmbl3kzadbjhunxsxyndlq"></a>
###### oci-ams-sl-hub-fw-all-sha-1 (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaanio5mombhijhwdcqi7j6l64n7ogmb6pmbl3kzadbjhunxsxyndlq)

####### Reglas de Entrada

| Origen    | Tipo de Origen   | Protocolo   | Puertos   | Descripción                                                   |
|:----------|:-----------------|:------------|:----------|:--------------------------------------------------------------|
| 0.0.0.0/0 | CIDR_BLOCK       | Todos       |           | 26/5/2025 - changed to stateless according to SR 4-0000679354 |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción                                                   |
|:----------|:------------------|:------------|:----------|:--------------------------------------------------------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           | 26/5/2025 - changed to stateless according to SR 4-0000679354 |

<a id="sl-ocid1_securitylist_oc1_eu_amsterdam_1_aaaaaaaaoqndnwqtlzuh5oq2po6frubsccz2ycxnjqzshkha2reoiqcdccoa"></a>
###### Default Security List for oci-ams-vnet-hub-sha (ID: ocid1.securitylist.oc1.eu-amsterdam-1.aaaaaaaaoqndnwqtlzuh5oq2po6frubsccz2ycxnjqzshkha2reoiqcdccoa)

####### Reglas de Entrada

| Origen         | Tipo de Origen   | Protocolo   | Puertos   | Descripción   |
|:---------------|:-----------------|:------------|:----------|:--------------|
| 0.0.0.0/0      | CIDR_BLOCK       | TCP         | 22-22     |               |
| 0.0.0.0/0      | CIDR_BLOCK       | ICMP        |           |               |
| 10.201.32.0/26 | CIDR_BLOCK       | ICMP        |           |               |

####### Reglas de Salida

| Destino   | Tipo de Destino   | Protocolo   | Puertos   | Descripción   |
|:----------|:------------------|:------------|:----------|:--------------|
| 0.0.0.0/0 | CIDR_BLOCK        | Todos       |           |               |

##### DRG Attachments

| ID                                                                                                  | Nombre                    | DRG                                                                                                                      | Estado   |
|:----------------------------------------------------------------------------------------------------|:--------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaa3j7cuxnnypkd4kn4xcqbsj6be5u66lp63ubzvep2axi4vblc74ma | oci-ams-drgattach-hub-sha | [oci-ams-vngw-drg-sha-1](#drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa) | ATTACHED |

##### Internet Gateways

<a id="igw-ocid1_internetgateway_oc1_eu_amsterdam_1_aaaaaaaasyqxm3cn5pmrrnwl5tgvkyyules3poxmbwd26mgijmzyc6gjqnzq"></a>
| ID                                                                                                    | Nombre                    | Habilitado   | Estado    |
|:------------------------------------------------------------------------------------------------------|:--------------------------|:-------------|:----------|
| ocid1.internetgateway.oc1.eu-amsterdam-1.aaaaaaaasyqxm3cn5pmrrnwl5tgvkyyules3poxmbwd26mgijmzyc6gjqnzq | oci-ams-vngw-inet-hub-sha | Sí           | AVAILABLE |

##### NAT Gateways

<a id="nat-ocid1_natgateway_oc1_eu_amsterdam_1_aaaaaaaa6bgehrsbciikripfqyqi5ts2rup4ggjh5gpwqrt7rumlgrv7lrna"></a>
| ID                                                                                               | Nombre                   | IP Pública     | Habilitado   | Estado    |
|:-------------------------------------------------------------------------------------------------|:-------------------------|:---------------|:-------------|:----------|
| ocid1.natgateway.oc1.eu-amsterdam-1.aaaaaaaa6bgehrsbciikripfqyqi5ts2rup4ggjh5gpwqrt7rumlgrv7lrna | oci-ams-vngw-nat-hub-sha | 143.47.184.126 | No           | AVAILABLE |

##### Service Gateways

<a id="sgw-ocid1_servicegateway_oc1_eu_amsterdam_1_aaaaaaaamnje4ncwdjppnnu22uerxtwjmvn6p3elcirs55xso3vs5rsviwoq"></a>
| ID                                                                                                   | Nombre                   | Servicios                                   | Estado    |
|:-----------------------------------------------------------------------------------------------------|:-------------------------|:--------------------------------------------|:----------|
| ocid1.servicegateway.oc1.eu-amsterdam-1.aaaaaaaamnje4ncwdjppnnu22uerxtwjmvn6p3elcirs55xso3vs5rsviwoq | oci-ams-vngw-svc-hub-sha | All AMS Services In Oracle Services Network | AVAILABLE |

<a id="region-eu-amsterdam-1-drgs"></a>
### Dynamic Routing Gateways (DRGs)

<a id="drg-ocid1_drg_oc1_eu_amsterdam_1_aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa"></a>
| ID                                                                                        | Nombre                 | Compartment                                                                         | Estado    |
|:------------------------------------------------------------------------------------------|:-----------------------|:------------------------------------------------------------------------------------|:----------|
| ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | oci-ams-vngw-drg-sha-1 | ocid1.compartment.oc1..aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq | AVAILABLE |

#### DRG Attachments

<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaao2yhm42l37ggl4se23v4w2icgu42etgb5qmpot32iejhsbz762ma"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaaodvhzayjdxmjg4uqjvtwunacmm2wkpeqimvewoxzzvgbrcxixcga"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaamak4hr3nhmpui5rfdvcixgc3zaiywtcg3pcxvmj5wun6ih6uaaha"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaagevgvwlhhpiyfp5id4xe7exwmju3bex34idcjrx7wcumncl3xioq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaa7pinr3mnargqmu5stb44ev5j2rxms23shuic3ppbjbfcamuirqka"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaab3uqwjuya4zw44kpkv5yjwos4fwocixqdmdjzamwlxhncr4pqoca"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaab6yp2escotsd22bdnv2haipwpo7v6lzrvuvbrhmxme5iaarzsaua"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaajjqvazgfp5xqgopzucr4xisyigeakafcduo6bzs4zvkcco6bvqfq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaactymilykvbz74guqmngwkhgad7hk5bojdprwwr4u4gp44deogmuq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaayll72ij2s6644dyz7qcxrn6wd2xqny7jwdqkxl3ieaju54jg7hva"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaaraes67z6l3mqsqryphr5pkut5rzcixim5m4lyl3t73dyyn6ga6zq"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaavyv5dzia4oedsldwbdlemp7wjze7yettyo2bqt6ddzqhm2zbmmwa"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaafogr6npefrwj3ccodpwyloboo7fjj7dnd6ru56i5u2ysxkntbyba"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaavr3ysndhiyqaplludsun2q5zgmcu5br6m2k2ntruomczevqz3eba"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaa4v2jqsqorqpb4e7bbdjtsooc27r6liq354o3vgqcug6nt4yakoaa"></a>
<a id="dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaa3j7cuxnnypkd4kn4xcqbsj6be5u66lp63ubzvep2axi4vblc74ma"></a>
| ID                                                                                                  | Nombre                                      | DRG ID                                                                                    | Tipo   | Recurso                                                                                   | Nombre Recurso                                                                                                                      | Route Table                                                                                                                              | Compartment                                                               | Estado   |
|:----------------------------------------------------------------------------------------------------|:--------------------------------------------|:------------------------------------------------------------------------------------------|:-------|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|:---------|
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaao2yhm42l37ggl4se23v4w2icgu42etgb5qmpot32iejhsbz762ma | oci-ams-it-drgattach-vnet-functions-dev     | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqas6ii7orfb5ieq3yh7v5sz3odqpdz3xmga325l6riba7q | [oci-ams-it-vnet-functions-dev](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqas6ii7orfb5ieq3yh7v5sz3odqpdz3xmga325l6riba7q)     | [oci-ams-it-udr-functions-dev](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa76vqladcgy3gmi62unseqs52tmahzh5xgbvx235nl4ru4qa547la)     | Compartment: aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaaodvhzayjdxmjg4uqjvtwunacmm2wkpeqimvewoxzzvgbrcxixcga | oci-ams-it-drgattach-vnet-forms-dev         | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqagxwcp7t334bf6phogoczfdpyrpbhvaochvw2nb2osbxa | [oci-ams-it-vnet-forms-dev](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqagxwcp7t334bf6phogoczfdpyrpbhvaochvw2nb2osbxa)         | [oci-ams-it-udr-forms-dev](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaxlrhqzewqts6fl53vrp26fkgrmi7ykga4gjcbzdqkvzdimt6brlq)         | Compartment: aaaaaaaauv7yl755kyzuzg7pwzgyzserqxjgbj2yyczeagslyesedrm3ny5a | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaamak4hr3nhmpui5rfdvcixgc3zaiywtcg3pcxvmj5wun6ih6uaaha | oci-ams-it-drgattach-vnet-vdipro-pro        | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqapn3vuk62v3z24vqxirjmdnlu5udqwwqhxmdnjfefr45a | [oci-ams-it-vnet-vdipro-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqapn3vuk62v3z24vqxirjmdnlu5udqwwqhxmdnjfefr45a)        | [oci-ams-it-udr-vdipro-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaap45as3kdzoku4u77o5ychtqe7hgdsopiopiv2gk4wt6mwwebikvq)        | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaagevgvwlhhpiyfp5id4xe7exwmju3bex34idcjrx7wcumncl3xioq | oci-ams-it-drgattach-vnet-tools-pro         | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqabnaw37eb3fyqw7nrigkqb2tmahrzwak6d5pz6asltm5a | [oci-ams-it-vnet-tools-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqabnaw37eb3fyqw7nrigkqb2tmahrzwak6d5pz6asltm5a)         | [oci-ams-it-udr-tools-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaad26hkb6apwidjgsrrqejacjpzrx7hkvjwywjk22ny2eippk27ifq)         | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaa7pinr3mnargqmu5stb44ev5j2rxms23shuic3ppbjbfcamuirqka | oci-ams-it-drgattach-vnet-vdi-customers-pro | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqanulxctlc7mhujlrxufblf4vkcctqz4zerpqbmytd7o6q | [oci-ams-it-vnet-vdi-customers-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqanulxctlc7mhujlrxufblf4vkcctqz4zerpqbmytd7o6q) | [oci-ams-it-udr-vdi-customers-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaaruuqsqvnsvj2go3ldr5adksmrkrxvig4o6asblr3q3yvmvmgxmha) | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaab3uqwjuya4zw44kpkv5yjwos4fwocixqdmdjzamwlxhncr4pqoca | oci-ams-it-drgattach-vnet-functions-pro     | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaaps62ygw643sijetx6rwn5qr3w6gikqcexkxvyz7y4oq | [oci-ams-it-vnet-functions-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaaps62ygw643sijetx6rwn5qr3w6gikqcexkxvyz7y4oq)     | [oci-ams-it-udr-functions-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa3ae4v5dua7efywpliibd25rtcu4a5353jjgdlod7bxt3wfqzpfqq)     | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaab6yp2escotsd22bdnv2haipwpo7v6lzrvuvbrhmxme5iaarzsaua | oci-ams-ot-drgattach-vnet-mw-pro            | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaweyhygwptai46wmh2xcqynumk5vyhivkxctfllhbdupa | [oci-ams-ot-vnet-mw-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaweyhygwptai46wmh2xcqynumk5vyhivkxctfllhbdupa)            | [oci-ams-ot-udr-mw-back-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaavxe76czrqe65n4lrjao6jlfu6yn5a7r5iwasof4zh4oft5i2yjma)       | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaajjqvazgfp5xqgopzucr4xisyigeakafcduo6bzs4zvkcco6bvqfq | oci-ams-it-drgattach-vnet-mw-pro            | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqarmgitbkpdy5h5pwcyxd3gptxxhopq22bmqpp67rfmega | [oci-ams-it-vnet-mw-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqarmgitbkpdy5h5pwcyxd3gptxxhopq22bmqpp67rfmega)            | [oci-ams-it-udr-mw-back-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaap5kupa5qxks6ohuxthfspt4udljkgwux5mprlg6thzjugvjqu6fa)       | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaactymilykvbz74guqmngwkhgad7hk5bojdprwwr4u4gp44deogmuq | oci-ams-ot-drgattach-vnet-db-pro            | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaojplkm7p4ywh42abafmkq4xkti7qmzwh4ebo2avp53la | [oci-ams-ot-vnet-db-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaojplkm7p4ywh42abafmkq4xkti7qmzwh4ebo2avp53la)            | [oci-ams-ot-udr-db-bck-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaayi2qdpgpujx3z26m2welh2lr2glwp5whq6kyk7v6ig4triklkkmq)        | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaayll72ij2s6644dyz7qcxrn6wd2xqny7jwdqkxl3ieaju54jg7hva | oci-ams-it-drgattach-vnet-db-pro            | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaebgsjzpxg26bf6nevmi6prnl52mqx25dnxv6b4mpllpa | [oci-ams-it-vnet-db-pro](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaebgsjzpxg26bf6nevmi6prnl52mqx25dnxv6b4mpllpa)            | [oci-ams-it-udr-db-bck-pro](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaar54ilrrhqlxnhuacctbjvwqil7uhfblk2yof7plo3lxmuvoowu4q)        | Compartment: aaaaaaaalpmros33hpumgqsccsyyxqbgyfc2qa6s3axpuy5drwy3fj2yghua | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaaraes67z6l3mqsqryphr5pkut5rzcixim5m4lyl3t73dyyn6ga6zq | oci-ams-it-drgattach-vnet-tools-stg         | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaeccutpjlmlmk635jpba37qcmoomhcfl7cmvze43xvqsq | [oci-ams-it-vnet-tools-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaeccutpjlmlmk635jpba37qcmoomhcfl7cmvze43xvqsq)         | [oci-ams-it-udr-tools-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaarnmwnvw2ohiwh7yz4mfgb5zvpvttiptt6fppgmgfezbswailxanq)         | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaavyv5dzia4oedsldwbdlemp7wjze7yettyo2bqt6ddzqhm2zbmmwa | oci-ams-ot-drgattach-vnet-mw-stg            | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqayzueatthiz3v6ls2qfqge3pedyyusuve4ddytnwwbmfa | [oci-ams-ot-vnet-mw-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqayzueatthiz3v6ls2qfqge3pedyyusuve4ddytnwwbmfa)            | [oci-ams-ot-udr-mw-back-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa62eifqvuqt3uoeg7krnajmdctbpli45pffou6dxakf3orhchajta)       | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaafogr6npefrwj3ccodpwyloboo7fjj7dnd6ru56i5u2ysxkntbyba | oci-ams-it-drgattach-vnet-mw-stg            | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqavkpxggb7lunwrptanl6tndqjuj3netvdjgc5enhq7rfa | [oci-ams-it-vnet-mw-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqavkpxggb7lunwrptanl6tndqjuj3netvdjgc5enhq7rfa)            | [oci-ams-it-udr-mw-back-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaasxgloorj4bxsl3l4gjknlj6b2n7w7ysaamn45x2ndpmfuu4nyaka)       | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaavr3ysndhiyqaplludsun2q5zgmcu5br6m2k2ntruomczevqz3eba | oci-ams-ot-drgattach-vnet-db-stg            | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaumsllyvdgfkyo3rfgrx2nb2taecrqanopuy3x33omgga | [oci-ams-ot-vnet-db-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaumsllyvdgfkyo3rfgrx2nb2taecrqanopuy3x33omgga)            | [oci-ams-ot-udr-db-bck-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaapwuzrkbc5lr3dhsb4fucguhzaau4jgb6qxfpqtssuojkmtegqapa)        | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaa4v2jqsqorqpb4e7bbdjtsooc27r6liq354o3vgqcug6nt4yakoaa | oci-ams-it-drgattach-vnet-db-stg            | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqaczixf26gyqw4o7p2mnwhd2cx2k2e6uhgzcgy7kcg3kfq | [oci-ams-it-vnet-db-stg](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqaczixf26gyqw4o7p2mnwhd2cx2k2e6uhgzcgy7kcg3kfq)            | [oci-ams-it-udr-db-bck-stg](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaag2wumu2cpuawpjbupqh53ymo667se5fmlk472r33t7hfmui6lcpq)        | Compartment: aaaaaaaa4u5bagpdbrw7p4f4ykj554arlvxp5cdh2ykpqrimen2jgexim73a | ATTACHED |
| ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaa3j7cuxnnypkd4kn4xcqbsj6be5u66lp63ubzvep2axi4vblc74ma | oci-ams-drgattach-hub-sha                   | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | VCN    | ocid1.vcn.oc1.eu-amsterdam-1.amaaaaaa6k4uvdqabpiciz67q2ud5hpn2i3eqzv7pwgqcsoynovow26kzfvq | [oci-ams-vnet-hub-sha](#vcn-ocid1_vcn_oc1_eu_amsterdam_1_amaaaaaa6k4uvdqabpiciz67q2ud5hpn2i3eqzv7pwgqcsoynovow26kzfvq)              | [oci-ams-udr-hub-int-sha](#rt-ocid1_routetable_oc1_eu_amsterdam_1_aaaaaaaa3pbpbbpva6susjspc2ecuisdig3djh2gaj3u3wxdesiwvzcaxqla)          | Compartment: aaaaaaaajvmomujag352kp6apannlokwcc3wmekpq4mozvpzd2kopcjt7waq | ATTACHED |

#### DRG Route Tables

##### oci-ams-udr-rpc-ams-sha (ID: ocid1.drgroutetable.oc1.eu-amsterdam-1.aaaaaaaald6anbenboz55dgwcfynpqr7x2goxypknuy5eg6mq2i4ks3cnjyq)

Import Distribution: [oci-ams-importrd-rpc-ams-sha](#drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaazif5dnajnhjy4lxx7jwpepfagqwl53aehcyjw7rcwfuebbn5xdeq)

| Destino        | Tipo de Destino   | Next Hop DRG Attachment                                                                                                               | Origen   | Tipo de Ruta   |
|:---------------|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------|
| 10.201.32.0/19 | CIDR_BLOCK        | [oci-ams-drgattach-hub-sha](#dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaa3j7cuxnnypkd4kn4xcqbsj6be5u66lp63ubzvep2axi4vblc74ma) |          | STATIC         |

##### oci-ams-udr-ipsec-sha (ID: ocid1.drgroutetable.oc1.eu-amsterdam-1.aaaaaaaai6mm4anikfeczvasolov3lri4kjkhfco3ehy7yk4wbpawy4frvvq)

Import Distribution: [oci-ams-importrd-ipsec-sha](#drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaacf2qyunc7gwa5ud4b3ryjcf7pgxrrpor6ybx64rfuwoo6fddf2aq)

| Destino        | Tipo de Destino   | Next Hop DRG Attachment                                                                                                               | Origen   | Tipo de Ruta   |
|:---------------|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------|
| 10.201.32.0/19 | CIDR_BLOCK        | [oci-ams-drgattach-hub-sha](#dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaa3j7cuxnnypkd4kn4xcqbsj6be5u66lp63ubzvep2axi4vblc74ma) |          | STATIC         |
| 10.201.0.0/19  | CIDR_BLOCK        | ocid1.drgattachment.oc1.eu-amsterdam-1.aaaaaaaapwpqervvwc757wag7kibfryjafx7jvnymd4nq5yg3nnwd65vgkia (Attachment no encontrado)        |          | STATIC         |

##### oci-ams-udr-hub-sha (ID: ocid1.drgroutetable.oc1.eu-amsterdam-1.aaaaaaaanrn4optywhprlad4545qjvrfabwnsczq2lqzjfe4wbwar5sfh2la)

Import Distribution: [oci-ams-importrd-hub-sha](#drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaahkv4zkwrygqwyrbpsu4zzzztib3jinmwrog3a4lkyqxfhzag7gva)

No hay reglas de ruta estáticas definidas.

##### oci-ams-udr-spokes-sha (ID: ocid1.drgroutetable.oc1.eu-amsterdam-1.aaaaaaaa5tf532uaaumwjfjalzjlbqp2pyt3ixrctlhl2x42sdb2glhe7amq)

Import Distribution: No configurada

| Destino   | Tipo de Destino   | Next Hop DRG Attachment                                                                                                               | Origen   | Tipo de Ruta   |
|:----------|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------|
| 0.0.0.0/0 | CIDR_BLOCK        | [oci-ams-drgattach-hub-sha](#dra-ocid1_drgattachment_oc1_eu_amsterdam_1_aaaaaaaa3j7cuxnnypkd4kn4xcqbsj6be5u66lp63ubzvep2axi4vblc74ma) |          | STATIC         |

##### DONT USE - Autogenerated Drg Route Table for VCN attachments (ID: ocid1.drgroutetable.oc1.eu-amsterdam-1.aaaaaaaamrig4qvxekkakzwyxisz55lcpfcb4pkgrim72caskngb2ex6njha)

Import Distribution: [DONT USE -Autogenerated Import Route Distribution for ALL routes](#drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaavz4iufugayzbqrqhqdsdvodxno5irnloi6pvrn6au2nfan36p6ia)

No hay reglas de ruta estáticas definidas.

##### DONT USE - Autogenerated Drg Route Table for RPC, VC, and IPSec attachments (ID: ocid1.drgroutetable.oc1.eu-amsterdam-1.aaaaaaaaeofxggnqnbbtuavxgjz5naq6j2zke63kpoqj6eayh654bhol7chq)

Import Distribution: [DONT USE - Autogenerated Import Route Distribution for VCN Routes](#drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaapco35wxfycvgnjb5psv5ures6tg2hhoh3xmt5nvz5x6jjrouhmuq)

No hay reglas de ruta estáticas definidas.

#### DRG Route Distributions (Import/Export)

<a id="drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaazif5dnajnhjy4lxx7jwpepfagqwl53aehcyjw7rcwfuebbn5xdeq"></a>
##### oci-ams-importrd-rpc-ams-sha (ID: ocid1.drgroutedistribution.oc1.eu-amsterdam-1.aaaaaaaazif5dnajnhjy4lxx7jwpepfagqwl53aehcyjw7rcwfuebbn5xdeq)

Tipo de Distribución: IMPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|          10 | DESCONOCIDO     |                   |                     | ACCEPT   |

<a id="drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaacf2qyunc7gwa5ud4b3ryjcf7pgxrrpor6ybx64rfuwoo6fddf2aq"></a>
##### oci-ams-importrd-ipsec-sha (ID: ocid1.drgroutedistribution.oc1.eu-amsterdam-1.aaaaaaaacf2qyunc7gwa5ud4b3ryjcf7pgxrrpor6ybx64rfuwoo6fddf2aq)

Tipo de Distribución: IMPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|          10 | DESCONOCIDO     |                   |                     | ACCEPT   |

<a id="drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaahkv4zkwrygqwyrbpsu4zzzztib3jinmwrog3a4lkyqxfhzag7gva"></a>
##### oci-ams-importrd-hub-sha (ID: ocid1.drgroutedistribution.oc1.eu-amsterdam-1.aaaaaaaahkv4zkwrygqwyrbpsu4zzzztib3jinmwrog3a4lkyqxfhzag7gva)

Tipo de Distribución: IMPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|          20 | DESCONOCIDO     |                   |                     | ACCEPT   |
|          10 | DESCONOCIDO     |                   |                     | ACCEPT   |
|          30 | DESCONOCIDO     |                   |                     | ACCEPT   |

<a id="drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaadnfk6gbtjacpjqz2n4ahib7czkatcfg4qryahvvx5gnuj2y4dwsq"></a>
##### Default Export Route Distribution for DRG: oci-ams-vngw-drg-sha-1 (ID: ocid1.drgroutedistribution.oc1.eu-amsterdam-1.aaaaaaaadnfk6gbtjacpjqz2n4ahib7czkatcfg4qryahvvx5gnuj2y4dwsq)

Tipo de Distribución: EXPORT

|   Prioridad | Tipo de Match   | Attachment Type   | DRG Attachment ID   | Acción   |
|------------:|:----------------|:------------------|:--------------------|:---------|
|           1 | DESCONOCIDO     |                   |                     | ACCEPT   |

<a id="drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaavz4iufugayzbqrqhqdsdvodxno5irnloi6pvrn6au2nfan36p6ia"></a>
##### DONT USE -Autogenerated Import Route Distribution for ALL routes (ID: ocid1.drgroutedistribution.oc1.eu-amsterdam-1.aaaaaaaavz4iufugayzbqrqhqdsdvodxno5irnloi6pvrn6au2nfan36p6ia)

Tipo de Distribución: IMPORT

No hay statements de distribución definidos.

<a id="drd-ocid1_drgroutedistribution_oc1_eu_amsterdam_1_aaaaaaaapco35wxfycvgnjb5psv5ures6tg2hhoh3xmt5nvz5x6jjrouhmuq"></a>
##### DONT USE - Autogenerated Import Route Distribution for VCN Routes (ID: ocid1.drgroutedistribution.oc1.eu-amsterdam-1.aaaaaaaapco35wxfycvgnjb5psv5ures6tg2hhoh3xmt5nvz5x6jjrouhmuq)

Tipo de Distribución: IMPORT

No hay statements de distribución definidos.

#### Remote Peering Connections

| ID                                                                                                            | Nombre                          | DRG ID                                                                                    | Región Peer   | RPC Peer ID                                                                                                | Estado    | Estado Peering   |
|:--------------------------------------------------------------------------------------------------------------|:--------------------------------|:------------------------------------------------------------------------------------------|:--------------|:-----------------------------------------------------------------------------------------------------------|:----------|:-----------------|
| ocid1.remotepeeringconnection.oc1.eu-amsterdam-1.aaaaaaaaqsqwz4looswqkwzh7fkbadfszy6ig7cozc3ql7jnkrs6nfzp453q | oci-ams-drgattach-rpc-mad-sha-1 | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | eu-madrid-1   | ocid1.remotepeeringconnection.oc1.eu-madrid-1.aaaaaaaaicr5yjr34uihgdxsqavz4muipbnm66ujeaahygdmxehbmrklcnja | AVAILABLE | PEERED           |

<a id="region-eu-amsterdam-1-vpn"></a>
### Conexiones VPN IPSec

| ID                                                                                                    | Nombre              | DRG ID                                                                                    | CPE ID                                                                                    | IP CPE      | IP CPE Tipo   | Estado    |
|:------------------------------------------------------------------------------------------------------|:--------------------|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|:------------|:--------------|:----------|
| ocid1.ipsecconnection.oc1.eu-amsterdam-1.aaaaaaaaumy6xj6vas6h74txcugpsihnn7mm6kxlcfbx2fp72wy2sujusccq | oci-ams-ipsec-sha-1 | ocid1.drg.oc1.eu-amsterdam-1.aaaaaaaat6jpdo6mbgwj5cesj6gcwg5h7pfngstfwllcn6tcfdfisgvu3bfa | ocid1.cpe.oc1.eu-amsterdam-1.aaaaaaaalxkwsnnowc4wchbddyf3574w64ezlewwzvii7hxyuxgtyffuhj6q | 195.57.2.66 | IP_ADDRESS    | AVAILABLE |

#### Detalles de Túneles VPN

##### Túneles de oci-ams-ipsec-sha-1

No se encontraron túneles para esta conexión VPN.

<a id="region-eu-amsterdam-1-fc"></a>
### Conexiones FastConnect

No se encontraron conexiones FastConnect en esta región.

