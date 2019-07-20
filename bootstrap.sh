#!/usr/bin/env bash

apt-get -y update
apt-get -y upgrade

# Tooling for VM management.

apt-get -y install htop
apt-get -y install vim

# Tooling for app development.

apt-get -y install make
apt-get -y install python3-pip

pip3 install virtualenv