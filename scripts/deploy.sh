#!/bin/bash

# deploy.sh
# Deployment script to set up the VM environment

echo "Starting deployment..."

# Update system and install dependencies
sudo apt-get update
sudo apt-get upgrade -y

# Install required packages for VM (QEMU, Python, etc.)
sudo apt-get install -y qemu qemu-kvm libvirt-bin python3-pip

# Install Python dependencies (assuming requirements.txt is available)
pip3 install -r requirements.txt

# Set up the VM by calling the init_vm.sh script
./scripts/init_vm.sh "MyDeployedVM"

# Deploy configurations (copy custom configs if needed)
cp -r config/ /etc/my_vm_config/

echo "Deployment complete!"
