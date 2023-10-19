## VyOS Router Setup

### Goals 

-   Learn how to configure network interface cards on VyOS and GNS3 Virtual Personal Computer (VPC)

-   Learn how to use some basic networking configuration and testing tools

-   Learn how to use a packet capture tool for network testing within GNS3

### Pre-Lab

-   Watch the the Following [ECT Tech Nuggets] videos on YouTube:
    -   [ECT Tech Nugget - N1.1 - GNS3]
    -   [ECT Tech Nugget - N1.2 - GNS3]
    -   [ECT Tech Nugget - N1.3 - GNS3]
    -   [ECT Tech Nugget - N4.0 - VyOS and GNS3  - Part 1]
    -   [ECT Tech Nugget  - N4.1 - VyOS and GNS3 - Part 2]

### Toolkit Additions
-   GNS3
-   VyOS
-   Draw.IO

### Task 1 - GNS3 Project Setup

1. Use the knowledge learned in [ECT Tech Nugget - N1.1 - GNS3] and [ECT Tech Nugget - N1.2 - GNS3] to get GNS3 started and running on your gHost.
<br>    

2. Open GNS3 and start a new project, name it: ``ITS-2300-Lab-VyOS-and-ARP``
<br>

3. Place the "Cloud" object (**not** the "NAT" object) and a VyOS router object into the GNS3 project workspace.
<br>

4. Link VyOS-1 e0 to Cloud1 br192-PublicNet as shown in diagram below.

   ![](./images/image1.png)

6. Start the GNS3 project and **WAIT** up to 2 minutes for VyOS router to boot and show the CLI login. Get help if things seem to be going awry.

### Task 2 - Configuring VyOS

6. Use knowledge learned from class and from [ECT Tech Nugget - N4.0 - VyOS and GNS3  - Part 1] and [ECT Tech Nugget  - N4.1 - VyOS and GNS3 - Part 2]. In the administration console of the virtual router, login into VyOS using itsclass credentials.
<br>

7. Set the router's hostname with the following command. Having a CLI prompt with a proper name makes it easier to tell which object you are connected to. This will result in MUCH faster troubleshooting. Instructors will **OFTEN** ask you to update your object hostname **BEFORE** helping trouble shoot as they won't know which object is which otherwise.
    ```
    config
    set system host-name VyOS-1
    commit
    exit
    exit
    ```
8. Login again, check the prompt and see that the hostname has been updated. The following commands setup the eth0 NIC/interface to automatically get an address from the br192-PublicNet network.
    ```
    config
    set interfaces ethernet eth0 address dhcp
    set interfaces ethernet eth0 description WAN
    commit
    ```

9. The above commands leave the system in configuration mode. Run ``exit`` to return to operations (run) mode. It is acceptable the message shown below:
    ```
    itsclass@VyOS-1# exit
    Warning: configuration changes have not been saved.
    exit
    itsclass@VyOS-1:~$
    ```

### Task 3 - Common VyOS Debugging Commands

10. Find the IP address and other NIC settings.
    ```
    show interfaces
    ```
    The address that begins with 132.235.205.X should appear on the eth0 line. If it does not the operator should check that the correct interface was used with VyOS eth0in GNS3, and that the line is connected to the correct upstream device.
<br>

11. Find the gateway for the default route, 0.0.0.0/0, from data produced by the following command.
    ```
    show ip route
    ```

12. The first trouble shooting step is to ping your local the gateway. The gateway IP was discovered in the previous task. Enter ping on the command line without pressing enter, copy the gateway address from the output and paste it the command line to form a new ping command like the ones used above. 
**Note:** The ping tool will run until it is interrupted by the user with the ``<Ctrl-C>`` key combination. 
<br>

13. The address ``8.8.8.8`` is maintained by Google. This means that it is considered "reliable" and is often used as a stable representation of access to the broader Internet.
    ```
    ping 8.8.8.8
    ```

14. Ping also workings with a DNS name (aka hostname) similar a URL in a web browser, but this requires the domain name service (DNS) to be configured and working. 
    ```
    ping google.com
    ```

15. In VyOS there are multiple command modes, this allows for a separation between the intention of the configuration and the what the router is currently configured. Some commands return different but related content. Return to the configuration mode and observe the difference in the show interfaces command.
    ```
    configure
    show interfaces
    ```

16. Other commands like the ping diagnostic tool only works in the operation mode. These commands are available when in configuration mode by prepending the run command to the intended operation mode command.
    ```
    run ping 8.8.8.8
    ```

### Task 4 - VyOS as a Simple Router

17. The following labs will elaborate on the following commands. For now, apply the following recipe in **configuration mode**.
**Note:** Copy/Paste is your friend!
    ```
    set interfaces ethernet eth1 address 172.16.85.254/24
    set service dhcp-server shared-network-name LAN subnet 172.16.85.0/24 default-router 172.16.85.254
    set service dhcp-server shared-network-name LAN subnet 172.16.85.0/24 name-server 132.235.9.75
    set service dhcp-server shared-network-name LAN subnet 172.16.85.0/24 domain-name vyos.net
    set service dhcp-server shared-network-name LAN subnet 172.16.85.0/24 lease 86400
    set service dhcp-server shared-network-name LAN subnet 172.16.85.0/24 range 0 start 172.16.85.1
    set service dhcp-server shared-network-name LAN subnet 172.16.85.0/24 range 0 stop 172.16.85.250
    set nat source rule 100 outbound-interface eth0
    set nat source rule 100 source address 172.16.85.0/24
    set nat source rule 100 translation address masquerade
    commit
    ```

18. Place an "Ethernet switch" object and an "Ubuntu-GUI" object into the work area of GNS3 and connect them as shown in diagram.

    ![](./images/image2.png)

19. Start the Ubuntu-GUI by right clicking on the Icon and selecting start. WAIT up to 2 minutes for the GUI object to boot and show the desktop!
<br>

20. Test your connection to headwallram.com from the Ubuntu-GUI machine, at the Terminal/Command Line/CLI use the command:
    ```
    ping headwallram.com
    ```
<br>

21. Use Diagnostic commands from previous labs to determine the IP address that is acquired by the Ubuntu-GUI.

### Task 5 - VPCS

22. Place a "VPCS" object into the work area of GNS3 and connect it as shown in diagram. Start the VPCS object.

    ![](./images/image3.png)

24. The VPCS object comes with GNS3 and for reasons only know to the GNS3 developers does NOT open it's console automatically when the object is started. Why? ```¯\_(ツ)_/¯```
To open the console right-click on the VPCS object and select console from the menu.
<br>

25. The VPCS is a VERY limited OS. Its only purpose is to be a network host testing object. To configure the VPCS in this lab use the command: ``dhcp``. There are ways to manually configure an IP in the VPCS that we will learn about in other labs.
<br>

26. When finished with the DHCP/DORA process it displays it's IP configuration. To gather other information from the VPCS use: ```show ip```

### Task 6 - ARP
ARP is the protocol used at "layer 2" aka "ethernet layer aka "switch layer" that devices use to transmit **FRAMES** on a **LOCAL** level. (Remember Ethernet Frames are Layer 2 and IP packets are Layer 3).
<br>

27. On VPCS run command ```show arp``` it will likely show a blank ARP table (i.e. ```arp table is empty```).
<br>

28. On VPCS ping the Ubuntu-GUI IP. **Quickly** as in within 20 seconds after the ping stops on the VPCS run the command: ```show arp```. This should show the ARP table

### Task 7 - Documentation and Diagrams

29. Create a table/chart (Excel or Google Sheets) like the chart below. Fill out as much as you can find out. This will be part of your lab report. Note the addition of the "MAC Address" column.

| Computer Name &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Adapter Name | MAC Address | IPv4 Address | Subnet Mask | Default Gateway | IPv6 Address (if available) |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------- | ------------ | ----------- | --------------- | --------------------------- |
| Gateway                                                                                                                          |              |             |              |             |                 |                             |
| &nbsp;                                                                                                                           |              |             |              |             |                 |                             |
| &nbsp;                                                                                                                           |              |             |              |             |                 |                             |
| &nbsp;                                                                                                                           |              |             |              |             |                 |                             |
| &nbsp;                                                                                                                           |              |             |              |             |                 |                             |
<br>

30. Using information from Draw.IO from lecture/lab/YouTube, develop a network diagram using stencils from the Scratchpad of this project to turn in as a PNG file.

### Student Deliverable
1. Complete appropriate lab assignment on Blackboard.

[ECT Tech Nuggets]:https://www.youtube.com/@ecttechnuggets9126/featured
[ECT Tech Nugget - N1.1 - GNS3]:https://youtu.be/w5qsM3LhpQI
[ECT Tech Nugget - N1.2 - GNS3]:https://youtu.be/X_LX4MCR1do
[ECT Tech Nugget - N1.3 - GNS3]:https://youtu.be/5ZZjxAYcy5Q
[ECT Tech Nugget - N4.0 - VyOS and GNS3  - Part 1]:https://youtu.be/POqlACy94ys
[ECT Tech Nugget  - N4.1 - VyOS and GNS3 - Part 2]:https://youtu.be/xtt3UO4gW7A