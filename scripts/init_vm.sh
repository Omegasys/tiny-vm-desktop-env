#!/bin/bash

# init_vm.sh
# Script to initialize a new VM

# Variables (adjust these values as needed)
VM_NAME=$1
DISK_SIZE=10G
MEMORY=2G
CPU=1

# Ensure a VM name is provided
if [ -z "$VM_NAME" ]; then
  echo "Error: VM name must be provided."
  exit 1
fi

# Create directories for the VM
VM_PATH="/var/lib/vms/$VM_NAME"
mkdir -p "$VM_PATH"

# Create the virtual disk
qemu-img create -f qcow2 "$VM_PATH/$VM_NAME.qcow2" $DISK_SIZE
if [ $? -ne 0 ]; then
  echo "Error: Failed to create disk image."
  exit 1
fi

# Set default VM configuration file (optional)
echo "VM_NAME=$VM_NAME" > "$VM_PATH/config.txt"
echo "MEMORY=$MEMORY" >> "$VM_PATH/config.txt"
echo "CPU=$CPU" >> "$VM_PATH/config.txt"
echo "DISK_SIZE=$DISK_SIZE" >> "$VM_PATH/config.txt"

echo "VM $VM_NAME initialized successfully at $VM_PATH."
