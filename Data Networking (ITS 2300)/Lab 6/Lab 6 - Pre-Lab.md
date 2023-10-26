# Lab 6 - Pre-Lab

## IP Grid

Random Network Generated: 172.128.124.0/22

| Name                  | Interface | Address/Mask       |
| --------------------- | --------- | ------------------ |
| WAN Address           |           | 132.235.205.60/25  |
| WAN Gateway           |           | 132.235.205.126/25 |
| LAN1 Network          |           | 172.128.124.0/25   |
| WAN                   |           |                    |
| VyOS-1                | eth0      | 132.235.205.60     |
| (WAN Gateway)         |           | 132.235.205.126    |
| LAN1 Network          |           |                    |
| VyOS-1 (LAN1 Gateway) | eth7      | 172.128.124.126    |
| DHCP Pool Start       |           | 172.128.124.10     |
| DHCP Pool End         |           | 172.128.124.110    |

## Graph

![Graph](/Data%20Networking%20(ITS%202300)/Lab%206/Lab%206%20-%20Diagram.png)

## Recipe WAN

    config

    set interfaces ethernet eth0 address 132.235.205.60/25
    set interfaces ethernet eth0 description WAN
    set protocols static route 0.0.0.0/0 next-hop 132.235.205.126
    set system name-server 132.235.9.75
    set system name-server 132.235.200.41

    set nat source rule 100 outbound-interface eth0
    set nat source rule 100 source address 172.128.124.0/22
    set nat source rule 100 translation address masquerade

    set interfaces ethernet eth7 address 172.128.124.126/25

    commit
    exit

## Recipe DHCP

    config

    set service dhcp-server shared-network-name MY_POOL subnet 172.128.124.0/25 range 0 start 172.128.124.10
    set service dhcp-server shared-network-name MY_POOL subnet 172.128.124.0/25 range 0 stop 172.128.124.110
    set service dhcp-server shared-network-name MY_POOL subnet 172.128.124.0/25 default-router 172.128.124.126
    set service dhcp-server shared-network-name MY_POOL subnet 172.128.124.0/25 lease 120
    set service dhcp-server shared-network-name MY_POOL subnet 172.128.124.0/25 name-server 132.235.9.75
    set service dhcp-server shared-network-name MY_POOL subnet 172.128.124.0/25 name-server 132.235.200.41

    commit
    exit

## Outputs PC1 (VPCS)

PC1> show ip

NAME        : PC1[1]
IP/MASK     : 172.128.124.10/25
GATEWAY     : 172.128.124.126
DNS         : 132.235.9.75  132.235.200.41
DHCP SERVER : 172.128.124.126
DHCP LEASE  : 67, 120/60/105
MAC         : 00:50:79:66:68:00
LPORT       : 10024
RHOST:PORT  : 127.0.0.1:10025
MTU         : 1500

## Outputs Win-Desktop-1

PS C:\Users\itsclass> ipconfig /renew

Windows IP Configuration

Ethernet adapter Ethernet Instance 0 3:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::76d7:acf8:2c37:8ffb%18
   IPv4 Address. . . . . . . . . . . : 172.128.124.11
   Subnet Mask . . . . . . . . . . . : 255.255.255.128
   Default Gateway . . . . . . . . . : 172.128.124.126

Tunnel adapter Teredo Tunneling Pseudo-Interface:

   Connection-specific DNS Suffix  . :
   IPv6 Address. . . . . . . . . . . : 2001:0:34a2:52f8:3c41:1a65:537f:83f4
   Link-local IPv6 Address . . . . . : fe80::3c41:1a65:537f:83f4%11
   Default Gateway . . . . . . . . . : ::
