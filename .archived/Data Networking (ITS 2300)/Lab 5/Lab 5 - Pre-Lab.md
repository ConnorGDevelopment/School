# Lab 5 - Pre-Lab

## My Info

| Number | First  | Last    | gHost IP     | WAN IP         | Mask | Gateway         |
| ------ | ------ | ------- | ------------ | -------------- | ---- | --------------- |
| 60     | Connor | Guarino | 10.101.40.60 | 132.235.205.60 | /25  | 132.235.205.126 |

## Conventions

- Default Gateway (Router) will use last usable address in the IP Network.
- All other static assigned IPs (including other routers that are not the default gateway) start at the beginning of the range.
- DHCP pools between the statically addressed clients and the Default Gateway.
- Unless stated otherwise use the following DNS Name servers:  
  - 132.235.9.75
  - 132.235.200.41

## IP Grid

| Name                          | IP/Mask           |
| ----------------------------- | ----------------- |
| WAN Address                   | 132.235.205.60/25 |
| WAN Gateway                   | 132.235.205.126   |
| Internal Network              | 10.40.0.0/16      |
| WAN                           | 132.235.205.0/25  |
| VyOS-1 eth0 IP                | 132.235.205.60/25 |
| LAN1                          | 10.40.0.0/17      |
| VyOS-1 eth6 (LAN1 Gateway) IP | 10.40.127.254/17  |
| VPCS IP                       | 10.40.0.1/17      |
| LAN2                          | 10.40.128.0/17    |
| VyOS-1 eth7 (LAN2 Gateway) IP | 10.40.255.254/17  |
| Ubuntu-GUI-1 IP               | 10.40.128.1/17    |
