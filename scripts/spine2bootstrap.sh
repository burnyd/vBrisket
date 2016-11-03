#!/bin/sh

sleep 5

FastCli -p 15 -c "configure
hostname spine2
!
username api secret password
!
aaa authorization exec default local
!
interface Ethernet1
  no switchport
  ip address 10.0.0.102/24
!
interface Ethernet2
description connection-to-leaf1a
no switchport
ip address 10.0.12.3/24
!
interface Ethernet3
description connection-to-leaf1b
no switchport
ip address 10.0.22.3/24
!
interface Ethernet4
description connection-to-leaf2a
no switchport
ip address 10.0.212.3/24
!
interface Ethernet5
description connection-to-leaf2b
no switchport
ip address 10.0.222.3/24
!
interface Ethernet6
description used for management
no switchport
ip address 192.168.15.17/24
!
int lo0 
ip address 4.4.4.4/32
!
ip routing
!
router bgp 65500
   router-id 4.4.4.4
   neighbor 10.0.12.2 remote-as 65501
   neighbor 10.0.12.2 maximum-routes 12000 
   neighbor 10.0.22.2 remote-as 65501
   neighbor 10.0.22.2 maximum-routes 12000 
exit"
