# Setup and Installation Guide

Follow the steps below to set up the Tiny VM Desktop Environment on your system.

## Prerequisites

Before installing, ensure that you have the following dependencies installed on your system:

- **Python 3.8+**
- **Virtualization software** (e.g., QEMU, VirtualBox, KVM)
- **pip** (for installing Python dependencies)

### On Ubuntu/Linux

```bash
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
