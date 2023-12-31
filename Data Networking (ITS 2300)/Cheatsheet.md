# ECT/ITS Lab Notebook Cheatsheet

## ECT/ITS IP Networking Convention

The last usable IP in a network is the gateway.

## Wireshark

Display Filter

```bash
ip.addr==X.X.X.X
```

### Common Network Diagnostic Commands

- `ipconfig /all` - [Windows] or `nmcli` [Ubuntu] Used to display basic network card configuration information
- `ping` - Used to check if a host is reachable across a network or to display the round-trip time for information traveling to or from the host
- `traceroute` [Ubuntu] or `tracert` [Windows] - Used to display the IP addresses and/or host names of all the routers between your host and another host, including round trip times to each of the intermediate routers. Nearly always use the -d [Windows] or -n option [Ubuntu] to disable DNS resolution.
- `netstat` [Windows] or `ss` - [Ubuntu] Used to display the Network status information for your particular host operating system. This can include existing network connections as well as routing information (i.e. how to reach other hosts if more than one network interface exists on the host)
- `dig` - Used to convert host names to IPv4 addresses or vice-versa. Web version: <http://digwebinterface.com>
- `nslookup` - Also used to convert hostnames to IPv4 addresses. A deprecated version of this command still exists in most major operating systems

## VyOS Config

### VyOS 1.3.1 User Guide - <https://docs.vyos.io/en/equuleus> - it is really good and not too long.

Switch into configuration mode.

```bash
config
```

Show Current Configuration

```bash
show
```

Push the configuration to the interfaces

```bash
commit
```

Set Hostname

```bash
set system host-name VyOS-1
```

Configure Interfaces

```bash
set interfaces ethernet eth0 address 132.235.160.X/28
set interfaces ethernet eth0 description WAN
```

Default Route - This only needs to be done **once per router.**

```bash
set protocols static route 0.0.0.0/0 next-hop 132.235.160.14
```

Static Route Update

```bash
set protocols static route 100.70.111.64/26 next-hop 100.70.111.241
```

DNS Servers

````bash
set system name-server 132.235.9.75
set system name-server 132.235.200.41
````

DHCP Server

````bash
set service dhcp-server shared-network-name SUB1_POOL subnet 192.168.12.0/24 range 0 start 192.168.12.1
set service dhcp-server shared-network-name SUB1_POOL subnet 192.168.12.0/24 range 0 stop 192.168.12.50
set service dhcp-server shared-network-name SUB1_POOL subnet 192.168.12.0/24 default-router 192.168.12.254
set service dhcp-server shared-network-name SUB1_POOL subnet 192.168.12.0/24 name-server 132.235.9.75
set service dhcp-server shared-network-name SUB1_POOL subnet 192.168.12.0/24 name-server 132.235.200.41
set service dhcp-server shared-network-name SUB1_POOL subnet 192.168.12.0/24 lease 120
````

Show DHCP Leases

````bash
show dhcp server leases
````

Network Address Translation

````bash
set nat source rule 100 source address 172.X.Y.Z/S
set nat source rule 100 outbound-interface eth0
set nat source rule 100 translation address masquerade
````

VyOS VLAN Interfaces

````bash
set interfaces ethernet eth0 vif 310 address 132.235.160.1/28
set interfaces ethernet eth0 vif 100X address 192.168.11.254/24
````

VyOS VPN Sample Commands

```bash
set interfaces openvpn vtun1 local-address <VyOS-1 vtun1 IP> subnet-mask <VyOS-1 vtun1 mask>
set interfaces openvpn vtun1 local-host 10.101.100.X
set interfaces openvpn vtun1 local-port 1195
set interfaces openvpn vtun1 mode site-to-site
set interfaces openvpn vtun1 remote-address <VyOS-2 vtun1 IP>
set interfaces openvpn vtun1 remote-host 132.235.160.X
set interfaces openvpn vtun1 remote-port 1195
set interfaces openvpn vtun1 shared-secret-key-file /config/auth/openvpn-1.key
set interfaces openvpn vtun1 protocol udp
set interfaces openvpn vtun1 persistent-tunnel
```

IPv6 Config Interface

```bash
set interfaces ethernet eth1 address 2610:a8:4831:3XY::1/64
```

IPv6 Static Routing

```bash
set protocols static route6 ::/0 next-hop 2610:a8:4831:3XY::1
```

Show IPv6 Route table

```bash
show ipv6 route
```

Config Name Server

```bash
set system name-server 2610:a8:4831:310::1
```

Configure IPv6 RA

````bash
set service router-advert interface ethY prefix 2610:a8:483f:XXXX::/64
set service router-advert interface ethY name-server 2001:4860:4860::8888
````

Advanced Config Commands

```bash
show system | commands
```

Ubuntu-CLI

````bash
sudo nmcli general hostname <PICK A HOSTNAME>
sudo nmcli con mod "Wired connection 1" ipv4.addresses X.X.X.X/Y
sudo nmcli con mod "Wired connection 1" ipv4.gateway X.X.X.G
sudo nmcli con mod "Wired connection 1" ipv4.dns D.D.D.D,S.S.S.S
sudo nmcli con mod "Wired connection 1" ipv4.method manual
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection up "Wired connection 1"

````

#### IPv4 Quick Subnetting Table

| Slash   | Dotted Decimal    | Total IPs
|---      |--                 |--
| /22     | 255.255.252.0     | 1024
| /23     | 255.255.254.0     | 512
|**/24**  | **255.255.255.0** | **256**
| /25     | 255.255.255.128   | 128
| /26     | 255.255.255.192   | 64
| /27     | 255.255.255.224   | 32
| /28     | 255.255.255.240   | 16
| /29     | 255.255.255.248   | 8
| /30     | 255.255.255.252   | 4
| /31     | 255.255.255.254   | 2
| /32     | 255.255.255.255   | 1
