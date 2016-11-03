import json
from jsonrpclib import Server
import sys
import os
from pprint import pprint

testswitches = ["leaf1a","leaf1b","leaf2a"]

switchusername = 'api'
switchpassword = 'password'

def CheckRun():
    for switch in testswitches:
      urlString = "https://%s:%s@%s/command-api" % (switchusername, switchpassword, switch)
      switchReq = Server( urlString )
      response = switchReq.runCmds( 1, ["enable", "show running-config"] )
      runningconfig = response[1]
      parsed = json.dumps(runningconfig, indent=4)
      print parsed 
      with open('/vagrant/scripts/gitrepo/'+ switch + '.txt', 'w') as outputfile:
	  json.dump(parsed, outputfile) 
CheckRun()

