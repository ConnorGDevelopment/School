# Lab 3 - Assignment

## "Task 3 - Common VyOS Debugging Commands - Copy/Paste the results of the ""show interfaces"" command after interfaces were successfully configured."

    itsclass@VyOS-1:~$ show interfaces
    Codes: S - State, L - Link, u - Up, D - Down, A - Admin Down
    Interface        IP Address                        S/L  Description
    ---------        ----------                        ---  -----------
    eth0             132.235.205.27/25                 u/u  WAN
    eth1             -                                 u/D  
    eth2             -                                 u/D  
    eth3             -                                 u/D  
    eth4             -                                 u/D  
    eth5             -                                 u/D  
    eth6             -                                 u/D  
    eth7             -                                 u/D  
    lo               127.0.0.1/8                       u/u  
                    ::1/128   

## Task 3 - Common VyOS Debugging Commands - Copy/Paste the results of the "show ip route" command after interfaces were successfully configured.

    itsclass@VyOS-1:~$ show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
        O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
        T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
        F - PBR, f - OpenFabric,
        > - selected route, * - FIB route, q - queued, r - rejected, b - backup

    S>* 0.0.0.0/0 [210/0] via 132.235.205.126, eth0, weight 1, 00:04:38
    C>* 132.235.205.0/25 is directly connected, eth0, 00:04:39

## Task 3 - Common VyOS Debugging Commands - Copy/Paste the results of the "ping 8.8.8.8" command after it was successful.

    itsclass@VyOS-1:~$ ping 8.8.8.8
    PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
    64 bytes from 8.8.8.8: icmp_seq=1 ttl=52 time=15.8 ms
    64 bytes from 8.8.8.8: icmp_seq=2 ttl=52 time=16.1 ms
    64 bytes from 8.8.8.8: icmp_seq=3 ttl=52 time=15.8 ms
    64 bytes from 8.8.8.8: icmp_seq=4 ttl=52 time=16.5 ms
    64 bytes from 8.8.8.8: icmp_seq=5 ttl=52 time=16.8 ms
    64 bytes from 8.8.8.8: icmp_seq=6 ttl=52 time=16.0 ms
    ^C
    --- 8.8.8.8 ping statistics ---
    6 packets transmitted, 6 received, 0% packet loss, time 12ms
    rtt min/avg/max/mdev = 15.814/16.160/16.788/0.362 ms

## Task 4 - VyOS as a Simple Router - Copy/Paste the results of the "ping headwallram.com" command after it was successful.

itsclass@VyOS-1# ping headwallram.com
PING headwallram.com (70.60.131.252) 56(84) bytes of data.
64 bytes from bcse-static.bcsengineering.com (70.60.131.252): icmp_seq=1 ttl=48 time=29.3 ms
64 bytes from bcse-static.bcsengineering.com (70.60.131.252): icmp_seq=2 ttl=48 time=26.4 ms
64 bytes from bcse-static.bcsengineering.com (70.60.131.252): icmp_seq=3 ttl=48 time=27.1 ms
^C
--- headwallram.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 5ms
rtt min/avg/max/mdev = 26.386/27.591/29.265/1.221 ms
[edit]

## Task 5 - VPCS - Copy/Paste the results of the "show ip" from the VPCS after the VPCS has an IP.

    PC1> show ip

    NAME        : PC1[1]
    IP/MASK     : 172.16.85.1/24
    GATEWAY     : 172.16.85.254
    DNS         : 132.235.9.75  
    DHCP SERVER : 172.16.85.254
    DHCP LEASE  : 86368, 86400/43200/75600
    DOMAIN NAME : vyos.net
    MAC         : 00:50:79:66:68:00
    LPORT       : 10026
    RHOST:PORT  : 127.0.0.1:10027
    MTU         : 1500

## Task 6 - ARP - Copy/Paste the results of the "show arp" from the Ubuntu-GUI after it has an IP.

    PC1> show arp           

    0c:37:d5:cf:00:00  172.16.85.2 expires in 118 seconds 
    
## Task 7 - Documentation and Diagrams - Copy the completed IP Table (IP-Grid) from your spreadsheet into this text field.

| Computer Name | Adapter Name  | MAC Address       | IPv4 Address   | Subnet Mask | Default Gateway | IPv6 Address                 |
| ------------- | ------------- | ----------------- | -------------- | ----------- | --------------- | ---------------------------- |
| VyOS-1        | eth0          |                   | 132.235.205.0  | /25         | 132.235.205.126 | fe80::01:24:57/64            |
| VyOS-1        | eth1          |                   | 172.16.85.0    | /24         | 132.235.205.126 | fe80::01:10:22/64            |
| Ubuntu-GUI-1  | Intel 82540EM |                   | 172.16.85.2    | /24         | 132.235.9.75    | fe80::6c74:e721:b94a:ea35/64 |
| PC1           | eth0          | 00:50:79:66:68:00 | 172.16.85.1/24 | /24         | 132.235.9.75    | fe80::250:79ff:fe66:6800/64  |
