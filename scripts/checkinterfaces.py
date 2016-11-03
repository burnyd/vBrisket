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

def CheckConnected():
    for switch in testswitches:
      urlString = "https://%s:%s@%s/command-api" % (switchusername, switchpassword, switch)
      switchReq = Server( urlString )
      response = switchReq.runCmds( 1, ["show ip interface"] )
      interfaceResponseName = response[0]["interfaces"]
      nodes = interfaceResponseName
      for node in nodes:
        interfaces = response[0]["interfaces"]
      for interface in interfaces:
         data = response[0]["interfaces"][interface]["interfaceStatus"]
      if data == 'disabled':
            raise ValueError('Interface is disconnected')
      else:
            print "%s %s" % (switch, data)

findallinterfaces()
CheckConnected()
