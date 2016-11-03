# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
config.vm.box = "vEOS-lab-4.15"
config.ssh.insert_key = false

  config.vm.define "leaf1a" do |leaf1a|
    leaf1a.vm.provision "shell", path: "scripts/leaf1abootstrap.sh"
    leaf1a.vm.network "private_network",  virtualbox__intnet: 'MGT-10.0.0.0', auto_config: false
    leaf1a.vm.network "private_network",  virtualbox__intnet: 'leaf1a-spine1-', auto_config: false
    leaf1a.vm.network "private_network",  virtualbox__intnet: 'leaf1a-spine2-', auto_config: false
    leaf1a.vm.network "private_network",  virtualbox__intnet: 'leaf1a-leaf1b-', auto_config: false
    leaf1a.vm.network "private_network",  virtualbox__intnet: 'leaf1a-host1', auto_config: false
    leaf1a.vm.network "private_network",  virtualbox__intnet: 'MGT', auto_config: false

  leaf1a.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--nicpromisc2", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc3", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc4", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc5", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc6", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc7", "allow-vms"]
    end

#Configure a forwarded port to access eAPI on vEOS
 #https://username:password@localhost:8443/command-api
   leaf1a.vm.network "forwarded_port", guest: 443, host: 8443
    end
 
 config.vm.define "leaf1b" do |leaf1b|
    leaf1b.vm.provision "shell", path: "scripts/leaf1bbootstrap.sh"
    leaf1b.vm.network "private_network",  virtualbox__intnet: 'MGT-10.0.0.0', auto_config: false
    leaf1b.vm.network "private_network",  virtualbox__intnet: 'leaf1b-spine1-', auto_config: false
    leaf1b.vm.network "private_network",  virtualbox__intnet: 'leaf1b-spine2-', auto_config: false
    leaf1b.vm.network "private_network",  virtualbox__intnet: 'leaf1a-leaf1b-', auto_config: false
    leaf1b.vm.network "private_network",  virtualbox__intnet: 'leaf1b-host1', auto_config: false
    leaf1b.vm.network "private_network",  virtualbox__intnet: 'MGT', auto_config: false

  leaf1b.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--nicpromisc2", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc3", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc4", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc5", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc6", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc7", "allow-vms"]
    end

#Configure a forwarded port to access eAPI on vEOS
 #https://username:password@localhost:8443/command-api
   leaf1b.vm.network "forwarded_port", guest: 443, host: 8444
    end
 
 config.vm.define "leaf2a" do |leaf2a|
    leaf2a.vm.provision "shell", path: "scripts/leaf2abootstrap.sh"
    leaf2a.vm.network "private_network",  virtualbox__intnet: 'MGT-10.0.0.0', auto_config: false
    leaf2a.vm.network "private_network",  virtualbox__intnet: 'leaf2a-spine1-', auto_config: false
    leaf2a.vm.network "private_network",  virtualbox__intnet: 'leaf2a-spine2-', auto_config: false
    leaf2a.vm.network "private_network",  virtualbox__intnet: 'leaf2a-leaf1b-', auto_config: false
    leaf2a.vm.network "private_network",  virtualbox__intnet: 'leaf2a-host2', auto_config: false
    leaf2a.vm.network "private_network",  virtualbox__intnet: 'MGT', auto_config: false

  leaf2a.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--nicpromisc2", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc3", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc4", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc5", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc6", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc7", "allow-vms"]
end

#Configure a forwarded port to access eAPI on vEOS
 #https://username:password@localhost:8443/command-api
   leaf2a.vm.network "forwarded_port", guest: 443, host: 8445
    end

  config.vm.define "leaf2b" do |leaf2b|
    leaf2b.vm.provision "shell", path: "scripts/leaf2bbootstrap.sh"
    leaf2b.vm.network "private_network",  virtualbox__intnet: 'MGT-10.0.0.0', auto_config: false
    leaf2b.vm.network "private_network",  virtualbox__intnet: 'leaf2b-spine1-', auto_config: false
    leaf2b.vm.network "private_network",  virtualbox__intnet: 'leaf2b-spine2-', auto_config: false
    leaf2b.vm.network "private_network",  virtualbox__intnet: 'leaf2b-leaf1b-', auto_config: false
    leaf2b.vm.network "private_network",  virtualbox__intnet: 'leaf2b-host2', auto_config: false
    leaf2b.vm.network "private_network",  virtualbox__intnet: 'MGT', auto_config: false

  leaf2b.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--nicpromisc2", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc3", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc4", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc5", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc6", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc7", "allow-vms"]
end

#Configure a forwarded port to access eAPI on vEOS
 #https://username:password@localhost:8443/command-api
   leaf2b.vm.network "forwarded_port", guest: 443, host: 8446
    end

  config.vm.define "spine1" do |spine1|
    spine1.vm.provision "shell", path: "scripts/spine1bootstrap.sh"
    spine1.vm.network "private_network",  virtualbox__intnet: 'MGT-10.0.0.0', auto_config: false
    spine1.vm.network "private_network",  virtualbox__intnet: 'leaf1a-spine1-', auto_config: false
    spine1.vm.network "private_network",  virtualbox__intnet: 'leaf1b-spine1-', auto_config: false
    spine1.vm.network "private_network",  virtualbox__intnet: 'leaf2a-spine1-', auto_config: false
    spine1.vm.network "private_network",  virtualbox__intnet: 'leaf2b-spine1-', auto_config: false
    spine1.vm.network "private_network",  virtualbox__intnet: 'MGT', auto_config: false

  spine1.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--nicpromisc2", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc3", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc4", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc5", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc6", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc7", "allow-vms"]
     

    end
 #Configure a forwarded port to access eAPI on vEOS
 #https://username:password@localhost:8445/command-api
      spine1.vm.network "forwarded_port", guest: 443, host: 8447
    end

  config.vm.define "spine2" do |spine2|
    spine2.vm.provision "shell", path: "scripts/spine2bootstrap.sh"
    spine2.vm.network "private_network",  virtualbox__intnet: 'MGT-10.0.0.0', auto_config: false
    spine2.vm.network "private_network",  virtualbox__intnet: 'leaf1a-spine2-', auto_config: false
    spine2.vm.network "private_network",  virtualbox__intnet: 'leaf1b-spine2-', auto_config: false
    spine2.vm.network "private_network",  virtualbox__intnet: 'leaf2a-spine2-', auto_config: false
    spine2.vm.network "private_network",  virtualbox__intnet: 'leaf2b-spine2-', auto_config: false
    spine2.vm.network "private_network",  virtualbox__intnet: 'MGT', auto_config: false

  spine2.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--nicpromisc2", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc3", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc4", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc5", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc6", "allow-vms"]
      v.customize ["modifyvm", :id, "--nicpromisc7", "allow-vms"]
    end

 #Configure a forwarded port to access eAPI on vEOS
 #https://username:password@localhost:8446/command-api
      spine2.vm.network "forwarded_port", guest: 443, host: 8448
    end

  config.vm.define "mgt1" do |mgt1|
    mgt1.vm.box = "ubuntu/trusty64"
    mgt1.vm.hostname = "mgt1"
    mgt1.vm.provision "shell", path: "scripts/mgt1bootstrap.sh"
    #Needed to statically put in an interface due to issues with the ubuntu/trusty64 image it will not work under the vbox nic settings.
    mgt1.vm.provision "shell", inline: "sudo ifconfig eth1 192.168.15.150 netmask 255.255.255.0"
    mgt1.vm.network "private_network", ip: "192.168.15.150", virtualbox__intnet: "MGT", auto_config: false
    mgt1.vm.network "forwarded_port", guest: 443, host: 9443
    mgt1.vm.network "forwarded_port", guest: 80, host: 9480
    mgt1.vm.network "forwarded_port", guest: 8080, host: 9488
    mgt1.vm.network "forwarded_port", guest: 5601, host: 9456
   
   end

  config.vm.define "host1" do |host1|
    host1.vm.box = "ubuntu/trusty64"
    host1.vm.hostname = "host1"
    host1.vm.network "private_network",  virtualbox__intnet: 'leaf1a-host1', auto_config: false
    host1.vm.network "private_network",  virtualbox__intnet: 'leaf1b-host1', auto_config: false
    #Needed to statically put in an interface due to issues with the ubuntu/trusty64 image it will not work under the vbox nic settings.
    host1.vm.provision "shell", inline: "sudo ifconfig eth1 10.0.5.100 netmask 255.255.255.0"
    host1.vm.provision "shell", inline: "sudo route add -net 10.0.0.0/8 gw 10.0.5.1 dev eth1"
   end

  config.vm.define "host2" do |host2|
    host2.vm.box = "ubuntu/trusty64"
    host2.vm.hostname = "host2"
    host2.vm.network "private_network",  virtualbox__intnet: 'leaf2a-host2', auto_config: false
    host2.vm.network "private_network",  virtualbox__intnet: 'leaf2b-host2', auto_config: false
   end

end
