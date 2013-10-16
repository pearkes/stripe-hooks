# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Not too much needed here, just Ubuntu 12.04 and a wee bit of provisioning
  config.vm.box = "precise64"

  # For Virtualbox
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  # Override for vmware
  config.vm.provider "vmware_fusion" do |v, override|
    override.vm.box_url = "http://files.vagrantup.com/precise64_vmware_fusion.box"
  end

  # Provision basic Python stuff
  config.vm.provision :shell, :path => "scripts/provision.sh"

  # NFS requires sudo, remove to disable
  config.vm.network :private_network, ip: "172.12.12.100"
  config.vm.synced_folder ".", "/vagrant", :nfs => true
end
