# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 512
    vb.cpus = 1
  end

  # Port for Flask dev server.
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # Port for Postgres.
  config.vm.network "forwarded_port", guest: 5432, host: 5432

  config.vm.synced_folder "./app/", "/home/vagrant/app/"

  # Provision packages to the VM.
  config.vm.provision "shell", path: "bootstrap.sh"

  # Provision Docker images to the VM.
  config.vm.provision "docker", images: ["postgres"]

  # Start up Docker images.
  config.vm.provision "docker" do |d|
    # Set the credentials to usgw/usgw and forward the default Postgres port.
    d.run "postgres", args: "-e POSTGRES_USER=usgw -e POSTGRES_PASSWORD=usgw -p 5432:5432"
  end

  # Initialize Postgres to the app's schema.
  config.vm.provision "shell",
    inline: "
      export PGPASSWORD=usgw
      docker cp /home/vagrant/app/schema.sql postgres:/docker-entrypoint-initdb.d/
    "
end
