# Lab 10 - Pre-Lab

## Network Division

Random Network Generated = 192.168.104.0/23

| Network Name | Hosts | Growth | Projected Hosts | Min Mask | Network Number / Mask |
| ------------ | ----- | ------ | --------------- | -------- | --------------------- |
| LAN1         | 65    | 25%    | 82              | 25       | 192.168.105.0/25      |
| LAN2         | 2     | 0%     | 2               | 29       | 192.168.105.160/29    |
| LAN3         | 200   | 10%    | 220             | 24       | 192.168.104.0/24      |
| LAN4         | 25    | 10%    | 28              | 27       | 192.168.105.128/27    |

## IP Chart

| Name                  | Interface | Address/Mask       |
| --------------------- | --------- | ------------------ |
| WAN Network           |           | 132.235.205.0/25   |
| LAN1 Network          |           | 192.168.105.0/25   |
| LAN2 Network          |           | 192.168.105.160/30 |
| LAN3 Network          |           | 192.168.104.0/24   |
| LAN4 Network          |           | 192.168.105.128/27 |
|                       |           |                    |
| **WAN**               |           |                    |
| VyOS-1                | eth0      | 132.235.205.60/25  |
| (WAN Gateway)         |           |                    |
|                       |           |                    |
| **LAN1 Network**      |           | 192.168.105.0/25   |
| (Static Host Start)   |           | 192.168.105.1      |
| (Static Host Stop)    |           | 192.168.105.65     |
| DHCP Pool Start       |           | 192.168.105.66     |
| DHCP Pool Stop        |           | 192.168.105.82     |
| VyOS-1 (LAN1 Gateway) | eth6      | 192.168.105.126    |
|                       |           |                    |
| **LAN2 Network**      |           | 192.168.105.160/29 |
| (Static Host Start)   |           | 192.168.105.161    |
| VyOS-2 (LAN2 Client)  | eth0      | 192.168.105.161    |
| (Static Host Stop)    |           | 192.168.105.162    |
| VyOS-1 (LAN2 Gateway) | eth1      | 192.168.105.166    |
|                       |           |                    |
| **LAN3 Network**      |           | 192.168.104.0/24   |
| (Static Host Start)   |           | 192.168.104.1      |
| (Static Host Stop)    |           | 192.168.104.200    |
| DHCP Pool Start       |           | 192.168.104.201    |
| DHCP Pool Stop        |           | 192.168.104.220    |
| VyOS-2 (LAN3 Gateway) | eth7      | 192.168.104.254    |
|                       |           |                    |
| **LAN4 Network**      |           | 192.168.105.128/27 |
| (Static Host Start)   |           | 192.168.105.129    |
| (Static Host Stop)    |           | 192.168.105.154    |
| DHCP Pool Start       |           | 192.168.105.155    |
| DHCP Pool Stop        |           | 192.168.105.157    |
| VyOS-2 (LAN4 Gateway) | eth6      | 192.168.105.158    |

## Network Diagram

![Diagram](/Data%20Networking%20(ITS%202300)/Lab%2010/Lab%2010%20-%20Pre-Lab%20Diagram.drawio.png)

## Scripts

### VyOS-1

config

set system host-name VyOS-1

commit

exit

exit

### VyOS-1 Router NICs

set interfaces ethernet eth0 address 132.235.205.60/25

set interfaces ethernet eth0 description WAN

set interfaces ethernet eth6 address 192.168.105.126/25

set interfaces ethernet eth6 description LAN1

set interfaces ethernet eth1 address 192.168.105.166/29

set interfaces ethernet eth1 description LAN2

### VyOS-1 Default Route

set protocols static route 0.0.0.0/0 next-hop 132.235.205.126

### VyOS-1 Nameservers

set system name-server 132.235.9.75

set system name-server 132.235.200.41

### VyOS-1 LAN1 DHCP Pool

set service dhcp-server shared-network-name LAN1 subnet 192.168.105.0/25 range 0 start 192.168.105.66

set service dhcp-server shared-network-name LAN1 subnet 192.168.105.0/25 range 0 stop 192.168.105.82

set service dhcp-server shared-network-name LAN1 subnet 192.168.105.0/25 default-router 192.168.105.126

set service dhcp-server shared-network-name LAN1 subnet 192.168.105.0/25 lease 120

set service dhcp-server shared-network-name LAN1 subnet 192.168.105.0/25 name-server 132.235.9.75

set service dhcp-server shared-network-name LAN1 subnet 192.168.105.0/25 name-server 132.235.200.41

### VyOS-1 NAT

set nat source rule 100 outbound-interface eth0

set nat source rule 100 source address 192.168.104.0/23

set nat source rule 100 translation address masquerade

### VyOS-1 Routing to LAN3

set protocols static route 192.168.104.0/24 next-hop 192.168.105.161

### VyOS-1 Routing to LAN4

set protocols static route 192.168.105.128/27 next-hop 192.168.105.161

## VyOS-2

config

set system host-name VyOS-2

commit

exit

exit

### VyOS-2 Router NICs

set interfaces ethernet eth0 address 192.168.105.161/29

set interfaces ethernet eth0 description LAN2

set interfaces ethernet eth7 address 192.168.104.254/24

set interfaces ethernet eth7 description LAN3

set interfaces ethernet eth6 address 192.168.105.158/27

set interfaces ethernet eth6 description LAN4

### VyOS-2 Default Route

set protocols static route 0.0.0.0/0 next-hop 192.168.105.166

### VyOS-2 Nameservers

set system name-server 132.235.9.75

set system name-server 132.235.200.41

### VyOS-2 LAN3 DHCP Pool

set service dhcp-server shared-network-name LAN3 subnet 192.168.104.0/24 range 0 start 192.168.104.201

set service dhcp-server shared-network-name LAN3 subnet 192.168.104.0/24 range 0 stop 192.168.104.220

set service dhcp-server shared-network-name LAN3 subnet 192.168.104.0/24 default-router 192.168.104.254

set service dhcp-server shared-network-name LAN3 subnet 192.168.104.0/24 lease 120

set service dhcp-server shared-network-name LAN3 subnet 192.168.104.0/24 name-server 132.235.9.75

set service dhcp-server shared-network-name LAN3 subnet 192.168.104.0/24 name-server 132.235.200.41

### VyOS-2 LAN4 DHCP Pool

set service dhcp-server shared-network-name LAN4 subnet 192.168.105.128/27 range 0 start 192.168.105.155

set service dhcp-server shared-network-name LAN4 subnet 192.168.105.128/27 range 0 stop 192.168.105.157

set service dhcp-server shared-network-name LAN4 subnet 192.168.105.128/27 default-router 192.168.105.158

set service dhcp-server shared-network-name LAN4 subnet 192.168.105.128/27 lease 120

set service dhcp-server shared-network-name LAN4 subnet 192.168.105.128/27 name-server 132.235.9.75

set service dhcp-server shared-network-name LAN4 subnet 192.168.105.128/27 name-server 132.235.200.41
