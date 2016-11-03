# vBrisket
slides and demos for vBrisket network automation talk 


![Alt text](environment.png?raw=true "Optional Title")

This is a presentation that was given at vBrisket on November 4th regarding network automation.

If anyone is interested in running this vagrant file please follow the link to creating a vagrant box with EOS.

1.)https://eos.arista.com/using-veos-with-vagrant-and-virtualbox/

2.) Call the vagrant box vEOS-lab-4.15 regardless of what version it is.  Or if you want modify the Vagrant file.

3.) In the directory in which vagrant is installed type the following vagrant up leaf1a leaf1b spine1 spine2 mgt1

4.) vagrant ssh mgt1 

5.) Each device has a management ip on the 192.168.15.x network. 
