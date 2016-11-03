import os
hostname = ['leaf1a','leaf1b','spine1','spine2']

print "\n\n\n\n ******** Running test to ping all network devices first on their management network *******\n\n\n\n "

for i in hostname: 
	response = os.system("ping -c 1 " + str(i))
	print "Ping testing %s" % (hostname)
	if response == 0:
  		print "%s , 'is up!" % (hostname)
	else:
  		print "%s, 'is down!" % (hostname)
