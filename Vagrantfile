# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 512
    vb.cpus = 1
  end

  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.synced_folder "./", "/home/vagrant/app"

  config.vm.provision "shell", path: "bootstrap.sh"
end
