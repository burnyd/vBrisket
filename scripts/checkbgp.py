import os
from jsonrpclib import Server
import sys

testswitches = ["leaf1a", "leaf1b", "spine1", "spine2"]
switchusername = 'api'
switchpassword = 'password'

def findallinterfaces(): #Function makes sure that each and every API is actually running on each switches and can pull with the current password.
    try:
        for switch in testswitches:
            urlString = "https://%s:%s@%s/command-api" % (switchusername, switchpassword, switch)
            switchReq = Server( urlString )
            response = switchReq.runCmds( 1, ["show ip interface"] )
            interfaceResponseName = response[0]["interfaces"]
    except:
        print "%s created an issue please check to make sure the API is running and not possibly blocking connectivity" % (switch)
        sys.exit()

def Checkbgp():
    for switch in testswitches:
      urlString = "https://%s:%s@%s/command-api" % (switchusername, switchpassword, switch)
      switchReq = Server( urlString )
      response = switchReq.runCmds( 1, ["show ip bgp summary"] )
      interfaceResponseName = response[0]['vrfs']['default']
      nodes = interfaceResponseName
      for node in nodes:
        peers = response[0]['vrfs']['default']['peers']
      for neighbors in peers:
         data = response[0]['vrfs']['default']['peers'][neighbors]["peerState"]
         if data == 'Established':
             print "%s %s" % (switch, data)
         else:
             #raise ValueError('BGP error')
             print "%s has an issue with a bgp peer" % (switch)
             raise ValueError('BGP error')
             #sys.exit()

findallinterfaces()
Checkbgp()
