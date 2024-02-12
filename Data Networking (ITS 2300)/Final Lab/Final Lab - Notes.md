# Final Lab - Notes

## VyOS-1 Config Scripts

set system host-name vyos-1
set interfaces ethernet eth0 address 132.235.205.60/25
set interfaces ethernet eth0 description WAN

set interfaces ethernet eth1 address 192.168.81.2/30
set interfaces ethernet eth1 description Interconnect_Network

set interfaces ethernet eth3 address 192.168.80.254/24
set interfaces ethernet eth3 description LAN2

set interfaces ethernet eth5 address 192.168.81.254/25
set interfaces ethernet eth5 description LAN3

set interfaces ethernet eth6 address 192.168.81.62/27
set interfaces ethernet eth6 description LAN1

set service dhcp-server shared-network-name LAN2_POOL subnet 192.168.80.0/24 range 0 start 192.168.80.3
set service dhcp-server shared-network-name LAN2_POOL subnet 192.168.80.0/24 range 0 stop 192.168.80.250
set service dhcp-server shared-network-name LAN2_POOL subnet 192.168.80.0/24 default-router 192.168.80.254
set service dhcp-server shared-network-name LAN2_POOL subnet 192.168.80.0/24 lease 120
set service dhcp-server shared-network-name LAN2_POOL subnet 192.168.80.0/24 name-server 132.235.9.75
set service dhcp-server shared-network-name LAN2_POOL subnet 192.168.80.0/24 name-server 132.235.200.41

## VyOS-2 Config Scripts

set system host-name vyos-2
set interfaces ethernet eth0 address 192.168.81.1/30
set interfaces ethernet eth0 description WAN

set interfaces ethernet eth6 address 192.168.81.126/26
set interfaces ethernet eth6 description LAN4

## IP Grid

| Name                     | Interface | Address/Mask       |
| ------------------------ | --------- | ------------------ |
| RandoNet Network         |           | 192.168.80.0/23    |
| WAN Network              |           | 132.235.205.0/25   |
| Interconnect Network     |           | 192.168.81.0/30    |
| LAN1 Network             |           | 192.168.81.32/27   |
| LAN2 Network             |           | 192.168.80.0/24    |
| LAN3 Network             |           | 192.168.81.128/25  |
| LAN4 Network             |           | 192.168.81.64/26   |
|                          |
| **WAN**                  |
| VyOS-1                   | eth0      | 132.235.205.60/25  |
| (WAN Gateway)            |           | 132.235.205.126/25 |
|                          |           |
| **Interconnect Network** |           |                    |
| VyOS-1 (Gateway)         | eth1      | 192.168.81.2/30    |
| VyOS-2 (Client )         | eth0      | 192.168.81.1/30    |
| **LAN1 Network**         |           |                    |
| DHCP Pool Start          |           |                    |
| DHCP Pool Stop           |           |                    |
| VyOS-1 (LAN1 Gateway)    | eth6      | 192.168.81.62/27   |
|                          |           |                    |
| **LAN2 Network**         |           |                    |
| DHCP Pool Start          |           | 192.168.80.3/24    |
| DHCP Pool Stop           |           | 192.168.80.250/24  |
| VyOS-1 (LAN2 Gateway)    | eth3      | 192.168.80.254/24  |
|                          |           |                    |
| **LAN3 Network**         |           |                    |
| DHCP Pool Start          |           |                    |
| DHCP Pool Stop           |           |                    |
| VyOS-1 (LAN3 Gateway)    | eth5      | 192.168.81.254/25  |
|                          |           |                    |
| **LAN4 Network**         |           |                    |
| DHCP Pool Start          |           |                    |
| DHCP Pool Stop           |           |                    |
| VyOS-2 (LAN4 Gateway)    | eth6      | 192.168.81.126/30  |

## VyOS-1 NAT

set nat source rule 100 outbound-interface eth0
set nat source rule 100 source address 192.168.80.0/23
set nat source rule 100 translation address masquerade

## VyOS-2 NAT

set nat source rule 100 outbound-interface eth0
set nat source rule 100 source address 192.168.81.62/26
set nat source rule 100 translation address masquerade

## VyOS-1 LAN1 DHCP

set service dhcp-server shared-network-name LAN1_POOL subnet 192.168.81.32/27 range 0 start 192.168.81.33
set service dhcp-server shared-network-name LAN1_POOL subnet 192.168.81.32/27 range 0 stop 192.168.81.61
set service dhcp-server shared-network-name LAN1_POOL subnet 192.168.81.32/27 default-router 192.168.81.61
set service dhcp-server shared-network-name LAN1_POOL subnet 192.168.81.32/27 lease 120
set service dhcp-server shared-network-name LAN1_POOL subnet 192.168.81.32/27 name-server 132.235.9.75
set service dhcp-server shared-network-name LAN1_POOL subnet 192.168.81.32/27 name-server 132.235.200.41

## VyOS-1 LAN3 DHCP

set service dhcp-server shared-network-name LAN3_POOL subnet 192.168.81.128/25 range 0 start 192.168.81.129
set service dhcp-server shared-network-name LAN3_POOL subnet 192.168.81.128/25 range 0 stop 192.168.81.253
set service dhcp-server shared-network-name LAN3_POOL subnet 192.168.81.128/25 default-router 192.168.81.254
set service dhcp-server shared-network-name LAN3_POOL subnet 192.168.81.128/25 lease 120
set service dhcp-server shared-network-name LAN3_POOL subnet 192.168.81.128/25 name-server 132.235.9.75
set service dhcp-server shared-network-name LAN3_POOL subnet 192.168.81.128/25 name-server 132.235.200.41

## VyOS-2 LAN4 DHCP

set service dhcp-server shared-network-name LAN4_POOL subnet 192.168.81.64/26 range 0 start 192.168.81.65
set service dhcp-server shared-network-name LAN4_POOL subnet 192.168.81.64/26 range 0 stop 192.168.81.125
set service dhcp-server shared-network-name LAN4_POOL subnet 192.168.81.64/26 default-router 192.168.81.126
set service dhcp-server shared-network-name LAN4_POOL subnet 192.168.81.64/26 lease 120
set service dhcp-server shared-network-name LAN4_POOL subnet 192.168.81.64/26 name-server 132.235.9.75
set service dhcp-server shared-network-name LAN4_POOL subnet 192.168.81.64/26 name-server 132.235.200.41

## VyOS-1 Routing

set protocols static route 0.0.0.0/0 next-hop 132.235.205.126
set protocols static route 192.168.81.64/26 next-hop 192.168.81.126

## VyOS-2 Routing

set protocols static route 0.0.0.0/0 next-hop 192.168.81.2
set protocols static route 192.168.81.32/27 next-hop 192.168.81.2
set protocols static route 192.168.80.0/24 next-hop 192.168.81.2
set protocols static route 192.168.81.128/25 next-hop 192.168.81.2

## Ping

PC2> ping 132.235.205.126

84 bytes from 132.235.205.126 icmp_seq=1 ttl=63 time=2.292 ms
84 bytes from 132.235.205.126 icmp_seq=2 ttl=63 time=2.228 ms
84 bytes from 132.235.205.126 icmp_seq=3 ttl=63 time=2.020 ms
84 bytes from 132.235.205.126 icmp_seq=4 ttl=63 time=1.584 ms
84 bytes from 132.235.205.126 icmp_seq=5 ttl=63 time=1.920 ms
^C
