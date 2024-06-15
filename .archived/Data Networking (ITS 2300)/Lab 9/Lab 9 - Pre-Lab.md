# Lab 9 - Pre-Lab

## Network Division

Random Network Generate = 192.168.0.0/22

| Network Name | Static Hosts | Growth | Projected Hosts | Network Number / Mask |
| ------------ | ------------ | ------ | --------------- | --------------------- |
| LAN1         | 75           | 25%    | 94              | 192.168.0.0/25        |
| LAN2         | 25           | 50%    | 38              | 192.168.1.0/26        |
| LAN3         | 150          | 10%    | 165             | 192.168.2.0/24        |
| LAN4         | 50           | 100%   | 100             | 192.168.3.0/25        |

## IP Chart

| Name                  | Interface       | Address/Mask       |
| --------------------- | --------------- | ------------------ |
| WAN Network           |                 | 132.235.205.0/25   |
| LAN1 Network          |                 | 192.168.0.0/25     |
| LAN2 Network          |                 | 192.168.1.0/26     |
| LAN3 Network          |                 | 192.168.2.0/24     |
| LAN4 Network          |                 | 192.168.3.0/25     |
|                       |                 |                    |
| **WAN**               |                 |                    |
| VyOS-1                | eth0            | 132.235.205.60/25  |
| (WAN Gateway)         | br192-PublicNet | 132.235.205.126/25 |
|                       |                 |                    |
| **LAN1 Network**      |                 | 192.168.0.0/25     |
| (Static Host Start)   |                 | 192.168.0.1        |
| (Static Host Stop)    |                 | 192.168.0.94       |
| DHCP Pool Start       |                 | 192.168.0.95       |
| VPCS1                 |                 | 192.168.0.95/25    |
| DHCP Pool Stop        |                 | 192.168.0.125      |
| VyOS-1 (LAN1 Gateway) | eth6            | 192.168.0.126      |
|                       |                 |                    |
| **LAN2 Network**      |                 | 192.168.1.0/26     |
| (Static Host Start)   |                 | 192.168.1.1        |
| VyOS-2 (LAN2 Client)  | eth0            | 192.168.1.1        |
| (Static Host Stop)    |                 | 192.168.1.38       |
| DHCP Pool Start       |                 | 192.168.1.39       |
| DHCP Pool Stop        |                 | 192.168.1.61       |
| VyOS-1 (LAN2 Gateway) | eth1            | 192.168.1.62       |
|                       |                 |                    |
| **LAN3 Network**      |                 | 192.168.2.0/24     |
| (Static Host Start)   |                 | 192.168.2.1        |
| (Static Host Stop)    |                 | 192.168.2.165      |
| DHCP Pool Start       |                 | 192.168.2.166      |
| Ubuntu-GUI-1          |                 | 192.168.2.166/24   |
| DHCP Pool Stop        |                 | 192.168.2.253      |
| VyOS-2 (LAN3 Gateway) | eth7            | 192.168.2.254      |
|                       |                 |                    |
| **LAN4 Network**      |                 | 192.168.3.0/25     |
| (Static Host Start)   |                 | 192.168.3.1        |
| (Static Host Stop)    |                 | 192.168.3.100      |
| DHCP Pool Start       |                 | 192.168.3.101      |
| DHCP Pool End         |                 | 192.168.3.125      |
| VyOS-2 (LAN4 Gateway) | eth6            | 192.168.3.126      |

## Network Diagram

![Diagram](/assets/Lab%209%20-%20Pre-Lab%20Diagram.drawio.png)

## Scripts

### VyOS-1

#### VyOS-1 Router NICs

config

set interfaces ethernet eth0 address 132.235.205.60/25
set interfaces ethernet eth0 description WAN

set nat source rule 100 outbound-interface eth0
set nat source rule 100 source address 192.168.0.126/25
set nat source rule 100 translation address masquerade

set interfaces ethernet eth6 address 192.168.0.126/25
set interfaces ethernet eth6 description LAN1

set nat source rule 200 outbound-interface eth0
set nat source rule 200 source address 192.168.1.62/26
set nat source rule 200 translation address masquerade

set interfaces ethernet eth1 address 192.168.1.62/26
set interfaces ethernet eth1 description LAN2

commit

#### VyOS-1 Default Route

config

set protocols static route 0.0.0.0/0 next-hop 132.235.205.126

commit

#### VyOS-1 Nameservers

config

set system name-server 132.235.9.75
set system name-server 132.235.200.41

commit

#### VyOS-1 LAN1 DHCP Pool

config

set service dhcp-server shared-network-name LAN1 subnet 192.168.0.0/25 range 0 start 192.168.0.95
set service dhcp-server shared-network-name LAN1 subnet 192.168.0.0/25 range 0 stop 192.168.0.125
set service dhcp-server shared-network-name LAN1 subnet 192.168.0.0/25 default-router 192.168.0.126
set service dhcp-server shared-network-name LAN1 subnet 192.168.0.0/25 lease 120
set service dhcp-server shared-network-name LAN1 subnet 192.168.0.0/25 name-server 132.235.9.75
set service dhcp-server shared-network-name LAN1 subnet 192.168.0.0/25 name-server 132.235.200.41

commit

#### VyOS-1 LAN2 DHCP Pool

config

set service dhcp-server shared-network-name LAN2 subnet 192.168.1.0/26 range 0 start 192.168.1.39
set service dhcp-server shared-network-name LAN2 subnet 192.168.1.0/26 range 0 stop 192.168.1.61
set service dhcp-server shared-network-name LAN2 subnet 192.168.1.0/26 default-router 192.168.1.62
set service dhcp-server shared-network-name LAN2 subnet 192.168.1.0/26 lease 120
set service dhcp-server shared-network-name LAN2 subnet 192.168.1.0/26 name-server 132.235.9.75
set service dhcp-server shared-network-name LAN2 subnet 192.168.1.0/26 name-server 132.235.200.41

commit

### VyOS-2

#### VyOS-2 Router NICs

config

set interfaces ethernet eth0 address 192.168.1.1/26
set interfaces ethernet eth0 description LAN2

set interfaces ethernet eth7 address 192.168.2.254/26
set interfaces ethernet eth7 description LAN3

commit

#### VyOS-2 Default Route

config

set protocols static route 0.0.0.0/0 next-hop 191.168.1.62

commit

#### VyOS-2 Nameservers

config

set system name-server 132.235.9.75
set system name-server 132.235.200.41

commit

#### VyOS-2 LAN3 DHCP Pool

config

set service dhcp-server shared-network-name LAN3 subnet 192.168.2.0/24 range 0 start 192.168.2.166
set service dhcp-server shared-network-name LAN3 subnet 192.168.2.0/24 range 0 stop 192.168.2.253
set service dhcp-server shared-network-name LAN3 subnet 192.168.2.0/24 default-router 192.168.2.254
set service dhcp-server shared-network-name LAN3 subnet 192.168.2.0/24 lease 120
set service dhcp-server shared-network-name LAN3 subnet 192.168.2.0/24 name-server 132.235.9.75
set service dhcp-server shared-network-name LAN3 subnet 192.168.2.0/24 name-server 132.235.200.41

commit
