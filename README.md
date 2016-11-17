# vBrisket
slides and demos for vBrisket network automation talk 


![Alt text](environment.png?raw=true "Optional Title")

This is a presentation that was given at vBrisket on November 4th regarding network automation.

If anyone is interested in running this vagrant file please follow the link to creating a vagrant box with EOS.

The only prerquisites are that vagrant and virtualbox are installed. 

1.) clone this repository so from linux or mac git clone https://github.com/burnyd/vBrisket.git

2.)Download the .box file from arista.com ie vEOS-lab-4.16.6M-virtualbox.box move it into the vBrisket directory that was cloned.

3.) run the following command inside the vBrisket directory vagrant box add vEOS-lab-4.16.6M vEOS-lab-4.16.6M-virtualbox.box

4.) In the directory in which vagrant is installed type the following vagrant up leaf1a leaf1b spine1 spine2 mgt1

5.) vagrant ssh mgt1 

6.) Each device has a management ip on the 192.168.15.x network. So once connected to mgt1 you can ssh into leaf1a for example.  ssh leaf1a everything is also in DNS.  Without connecting directly into mgt1 you can run the following commands.  vagrant ssh leaf1a.  It will drop you into bash.  To get into the cli run the cli process FastCli.
