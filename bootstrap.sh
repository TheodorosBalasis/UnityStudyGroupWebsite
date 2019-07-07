#!/usr/bin/env bash

apt-get -y update
apt-get -y upgrade

# Tooling for VM management.

apt-get -y install htop
apt-get -y install vim

# Tooling for app development.

apt-get -y install make
apt-get -y install python-pip

pip install virtualenv

# Add Python environment variable to bashrc
# so that `python` points to Python 3.

VAGRANT_BASHRC=/home/vagrant/.bashrc

if [ ! -f $VAGRANT_BASHRC ]
then
    touch $VAGRANT_BASHRC
fi

echo '' >> $VAGRANT_BASHRC
echo 'export python=python3' >> $VAGRANT_BASHRC