#!/bin/sh

sleep 5

FastCli -p 15 -c "configure
hostname leaf1b
!
username api secret password
!
aaa authorization exec default local
!
vlan 5
!
interface vlan 5
ip address 10.0.5.3/24
vrrp 5 ip 10.0.5.1
no shut
!
interface Ethernet1
  no switchport
  ip address 10.0.0.100/24
!
interface Ethernet2
description connection-to-spine1
no switchport
ip address 10.0.21.2/24
!
interface Ethernet3
description connection-to-spine2
no switchport
ip address 10.0.22.2/24
!
interface Ethernet4
description connection-to-leaf1a
switchport
switchport mode trunk
!
interface Ethernet5
description connection-to-host2
switchport mode access
switchport access vlan 5
!
interface Ethernet6
description used for management
no switchport
ip address 192.168.15.12/24
!
int loopback0
ip address 2.2.2.2/32
!
ip routing
!
router bgp 65501
   router-id 2.2.2.2
   neighbor 10.0.5.2 remote-as 65501
   neighbor 10.0.5.2 send-community
   neighbor 10.0.5.2 maximum-routes 12000 
   neighbor 10.0.21.3 remote-as 65500
   neighbor 10.0.21.3 maximum-routes 12000 
   neighbor 10.0.22.3 remote-as 65500
   neighbor 10.0.22.3 maximum-routes 12000 
   redistribute connected
exit"
