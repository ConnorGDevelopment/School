# My Cheatsheet

## VyOS

### Script Head

> config

### Script Tail

> commit
> exit

### Configure WAN + LAN Gateway

> set interfaces ethernet eth0 address 132.235.205.60/25
> set interfaces ethernet eth0 description WAN
> set protocols static route 0.0.0.0/0 next-hop 132.235.205.126
> set system name-server 132.235.9.75
> set system name-server 132.235.200.41
>
> set interfaces ethernet ==PORT== address ==LAN_GATEWAY_ADDR==

### Configure DHCP

> set service dhcp-server shared-network-name ==POOL_NAME== subnet ==NETWORK_NUMBER/MASK== range 0 start ==POOL_START==
> set service dhcp-server shared-network-name ==POOL_NAME== subnet ==NETWORK_NUMBER/MASK== range 0 stop ==POOL_STOP==
> set service dhcp-server shared-network-name ==POOL_NAME== subnet ==NETWORK_NUMBER/MASK== default-router ==GATEWAY==
> set service dhcp-server shared-network-name ==POOL_NAME== subnet ==NETWORK_NUMBER/MASK== lease 120
> set service dhcp-server shared-network-name ==POOL_NAME== subnet ==NETWORK_NUMBER/MASK== name-server 132.235.9.75
> set service dhcp-server shared-network-name ==POOL_NAME== subnet ==NETWORK_NUMBER/MASK== name-server 132.235.200.41

### Configure NAT

> set nat source rule 100 outbound-interface eth0
> set nat source rule 100 source address ==LAN_NETWORK_NUMBER/MASK==
> set nat source rule 100 translation address masquerade
