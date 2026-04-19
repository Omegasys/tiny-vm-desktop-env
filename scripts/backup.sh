#!/bin/bash

# backup.sh
# Backup script for VM data

# Variables
VM_NAME=$1
BACKUP_DIR="/backups/vm_backups"

# Ensure VM name is provided
if [ -z "$VM_NAME" ]; then
  echo "Error: VM name must be provided."
  exit 1
fi

# Check if VM exists
VM_PATH="/var/lib/vms/$VM_NAME"
if [ ! -d "$VM_PATH" ]; then
  echo "Error: VM $VM_NAME not found."
  exit 1
fi

# Create backup directory if not exists
mkdir -p "$BACKUP_DIR"

# Backup disk image and configuration
tar -czf "$BACKUP_DIR/$VM_NAME-backup.tar.gz" -C "$VM_PATH" .
if [ $? -eq 0 ]; then
  echo "Backup of VM $VM_NAME completed successfully."
else
  echo "Error: Backup failed."
  exit 1
fi
