## IP Subnetting

### Goals 
-   Client and Router Configuration Basics
-   Design and Implement New LAN Segment

### PreLab
-   Thursday Pre-Lab Checkpoint. This lab has a check point that students need to be at **BEFORE** the Thursday lab session.
  
![](./images/Pre-Lab-Deliverable.png)

-   Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:

    -   [ECT Tech Nugget - N2.1 - IPv4 Subnetting - Part 1](https://www.youtube.com/watch?v=uwa7w37LhF0&list=PLEA5GnkCPRTlvN_eyR99jOSsBCaV6khRS&index=9)

    -   [ECT Tech Nugget - N2.1 - IPv4 Subnetting - Part 2](https://www.youtube.com/watch?v=K-yAX1OHNSI&list=PLEA5GnkCPRTlvN_eyR99jOSsBCaV6khRS&index=10)

    -   [ECT Tech Nugget - N2.3 - IPv4 Subnetting - Binary Method](https://www.youtube.com/watch?v=A_JbKcmjyts&list=PLEA5GnkCPRTlvN_eyR99jOSsBCaV6khRS&index=11)

### Resources
-   Tools from Previous labs
-   Virtual Lab Notebook or a text editor
-   Favorite subnet calculator - http://www.its.ohio.edu/ipcalc

### Network Diagram

  ![](./images/network-daig-1.png)

### Task 1 - WAN Configuration

1. Subnet 10.40.0.0/16 into two networks for use in LAN1 and LAN2. Create an IP Grid using a table/chart (Excel or Google Sheets) with the info from the chart below. Put the conventions listed below into your lab notebook they are expected for all subnetting assignments.

  #### Lab Network Conventions (aka Local Best Practices)
  These conventions MUST be used for IP address assignment. These conventions will be in effect for all assignments for the entire semester.
  A. Default Gateway (Router) will use the last usable address in the IP Network.
  B. All other static assigned IPs (including other routers that are not the default gateway) start at the beginning of the range. 
  C. DHCP pools between the statically addressed clients and the Default Gateway.
  D. Unless stated otherwise use the following DNS Name servers: 132.235.9.75, 132.235.200.41
  **HINT:** Think about the "goto" subnet sizes talked about in lecture. Don't over complicate the process.

  **Note:** The **X** is a variable that's supplied to the student on Blackboard. This way each student has a unique number.<br><br>
IP Grid
| Name                          | IP/Mask                                                                                                                                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WAN Address                   | 132.235.205.X/25                                                                                                                                                                                               |
| WAN Gateway                   | 132.235.205.Y                                                                                                                                                                                                  |
| Internal Network              | 10.40.0.0/16                                                                                                                                                                                                   |
| **WAN**                       |
| VyOS-1 eth0 IP                | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| **LAN1**                      |
| VyOS-1 eth6 (LAN1 Gateway) IP |
| VPCS IP                       |
| **LAN2**                      |
| VyOS-1 eth7 (LAN2 Gateway) IP |
| Ubuntu-GUI-1 IP               |
<br>

3. Close all other projects and start a **new** GNS3 project called ``ITS-2300-LAB-Subnetting``. 

3.5 Create the network seen in the Network Diagram above. See Diagraming step at the end of this lab and create the appropriate Draw.IO drawing. 

4. Start VyOS. Once booted up use knowledge learned in earlier labs **AND** your personal WAN address, as shown on Blackboard, in the following template to configure the WAN interface on VyOS. For help use the ITS [Lab Notebook Cheat Sheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet).

   **Note:** X (your IP) and Y (gateway) must be replaced with personalized information only available on Blackboard! (should be in your IP GRID by now too!).

   **Note2:** If the name servers are already configured on VyOS you may receive an error or warning message.

    ```
    set interfaces ethernet eth0 address 132.235.205.X/25
    set interfaces ethernet eth0 description WAN
    set protocols static route 0.0.0.0/0 next-hop 132.235.205.Y
    set system name-server 132.235.9.75
    set system name-server 132.235.200.41
    ```

6. To show VyOS's route table:<br>
   
   In config mode: ``run show ip route``<br>
   In NON-config mode: ``show ip route``
<br>

7. After committing the configuration. Test the WAN side by pinging it's gateway and then test outside world connectivity by using ping and traceroute with a "known good" AKA reliable address (8.8.8.8 in this case).
<br>

8. Use the following commands add to the NAT configuration of VyOS-1. This updates the NAT service.

   **Note:** Don't forget to Commit!

    ```
    set nat source rule 100 outbound-interface eth0
    set nat source rule 100 source address 10.40.0.0/16
    set nat source rule 100 translation address masquerade
    ```

### Task 2 - LAN1 Network

9. Configure VyOS-1 eth6.
  
   **Note:** A,B and G must be replaced with information from the IP Grid.

    ```
    set interfaces ethernet eth6 address 10.40.A.B/G
    ```

10. Start the VPCS PC1 object and configure the static IP from your IP GRID. 
    
    **Note:** R and S must be replaced with information from the IP Grid. 

    ```
    ip 10.40.R.S <subnet mask> <gateway IP>
    ```
    <br>

11. Confirm that the VPCS is able to ping it's gateway IP and the outside world ("known good" IP).
<br>

```diff
@@ Students should **at least** be to this point by their Thursday lab session @@
```

![](./images/Lab-Checkpoint.png)

### Task 3 - LAN2 Network

12.  Using What you have learned in Task 2 configure VyOS-1 eth7 for LAN2.
    <br>

13. At an **Ubuntu-GUI-1** terminal/CLI configure it with an IP from the LAN2 network, see IP Grid. Use the following commands as a template.
    
    **Note:** A,B and S must be replaced with information from the IP Grid. 
    
    **Note2:** B.G is the gateway IP for LAN2

    ```
    sudo nmcli general hostname <PICK A HOSTNAME>
    sudo nmcli con mod "Wired connection 1" ipv4.addresses 10.40.A.B/G
    sudo nmcli con mod "Wired connection 1" ipv4.gateway 10.40.A.G
    sudo nmcli con mod "Wired connection 1" ipv4.dns 132.235.9.75
    sudo nmcli con mod "Wired connection 1" ipv4.method manual
    sudo nmcli connection down "Wired connection 1"
    sudo nmcli connection up "Wired connection 1"
    ```

15.  Confirm ping to it's gateway IP and the outside world ("known good").
<br>

16. Use the following command to show routing table in Ubuntu ```ip route``` and VyOS ```show ip route```.

### Task 4 - Documentation and Diagrams

17. Your completed IP Grid will be part of your lab report.
<br>

18. Using information from Draw.IO from lecture/lab/YouTube, develop a network diagram of this project in Draw.io to turn in as a PNG file. Place all IPv4 IPs on the diagram with appropriate interface name. **NEW:** Add colored background to denote networks and **add network numbers with mask** to the colored squares similar to the network diagram seen above.

### Student Deliverable
19. Complete appropriate lab assignment on Blackboard.