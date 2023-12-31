# Lab 7 - Pre-Lab

## IP Grid

RandoNet Generated Network: 172.33.0.0/16

| Name                  | Interface             | Address/Mask          |
| --------------------- | --------------------- | --------------------- |
| **WAN Network**       |                       | 132.235.205.0/25      |
| **LAN1 Network**      |                       | 172.33.255.0/24       |
| **LAN2 Network**      |                       | 172.33.252.0/23       |
|                       |                       |                       |
| **WAN**               |                       | 132.235.205.0/25      |
| VyOS-1                | eth0                  | 132.235.205.60/25     |
| (WAN Gateway)         | br192-PublicNet       | 132.235.205.126/25    |
|                       |                       |                       |
| **LAN1 Network**      |                       | 172.33.**255**.0/24   |
| DHCP Pool Start       |                       | 172.33.**255**.50/24  |
| DHCP Pool Stop        |                       | 172.33.**255**.200/24 |
| VyOS-1 (LAN1 Gateway) | eth6                  | 172.33.**255**.254/24 |
| PC1 (VPCS)            | e0                    | 172.33.255.50/24      |
| Ubuntu-CLI-1          | e0                    | 172.33.255.51/24      |
|                       |                       |                       |
| **LAN2 Network**      |                       | 172.33.**252**.0/23   |
| DHCP Pool Start       |                       | 172.33.**252**.55/23  |
| DHCP Pool Stop        |                       | 172.33.**253**.100/23 |
| VyOS-2 (LAN2 Gateway) | eth7                  | 172.33.**253**.254/23 |
| PC2 (VPCS)            | e0                    | 172.33.252.55/23      |
| Win-Desktop-1         | Ethernet Instance 0 3 | 172.33.252.57/23      |

## Network Diagram

![Diagram](/Data%20Networking%20(ITS%202300)/Lab%207/Lab%207%20-%20Pre-Lab%20Diagram.png)

## VyOS Recipe

### WAN + LAN Gateway

    config
    set interfaces ethernet eth0 address 132.235.205.60/25
    set interfaces ethernet eth0 description WAN
    set protocols static route 0.0.0.0/0 next-hop 132.235.205.126
    set system name-server 132.235.9.75
    set system name-server 132.235.200.41

    set interfaces ethernet eth6 address 172.33.255.254/24
    set interfaces ethernet eth7 address 172.33.253.254/23
   
    commit

### Configure DHCP (LAN1 Network)

    config
    set service dhcp-server shared-network-name LAN1_POOL subnet 172.33.255.0/24 range 0 start 172.33.255.50
    set service dhcp-server shared-network-name LAN1_POOL subnet 172.33.255.0/24 range 0 stop 172.33.255.200
    set service dhcp-server shared-network-name LAN1_POOL subnet 172.33.255.0/24 default-router 172.33.255.254
    set service dhcp-server shared-network-name LAN1_POOL subnet 172.33.255.0/24 lease 120
    set service dhcp-server shared-network-name LAN1_POOL subnet 172.33.255.0/24 name-server 132.235.9.75
    set service dhcp-server shared-network-name LAN1_POOL subnet 172.33.255.0/24 name-server 132.235.200.41
    commit

### Configure DHCP (LAN2 Network)

    config
    set service dhcp-server shared-network-name LAN2_POOL subnet 172.33.252.0/23 range 0 start 172.33.252.55
    set service dhcp-server shared-network-name LAN2_POOL subnet 172.33.252.0/23 range 0 stop 172.33.253.100
    set service dhcp-server shared-network-name LAN2_POOL subnet 172.33.252.0/23 default-router 172.33.253.254
    set service dhcp-server shared-network-name LAN2_POOL subnet 172.33.252.0/23 lease 120
    set service dhcp-server shared-network-name LAN2_POOL subnet 172.33.252.0/23 name-server 132.235.9.75
    set service dhcp-server shared-network-name LAN2_POOL subnet 172.33.252.0/23 name-server 132.235.200.41
    commit

### Configure NAT

    config
    set nat source rule 100 outbound-interface eth0
    set nat source rule 100 source address 172.33.252.0/22
    set nat source rule 100 translation address masquerade
    commit

### NAT Forwarding

    config
    set nat destination rule 10 description 'Port Forward: Public HTTP (8080) to Ubuntu-CLI-1 HTTP (80)'
    set nat destination rule 10 destination port '8080'
    set nat destination rule 10 inbound-interface 'eth0'
    set nat destination rule 10 protocol 'tcp'
    set nat destination rule 10 translation address ==CLIENT_IP==
    set nat destination rule 10 translation port 80
    commit
