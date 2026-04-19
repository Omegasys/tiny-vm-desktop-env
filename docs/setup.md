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
Make sure your user is added to the libvirt group to allow running VMs:
sudo usermod -aG libvirt $USER
Log out and back in to apply the group changes.
On macOS
Install Homebrew if you don't have it:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install QEMU:
brew install qemu
Optionally, you can also install Docker if you'd like to containerize your setup.
On Windows
Install VirtualBox from the official website
.
Install Windows Subsystem for Linux (WSL) if using a Linux-based environment.
Alternatively, use Docker for Windows to containerize the setup.
Installing the Project
Clone the repository to your local machine:
git clone https://github.com/your-username/tiny-vm-desktop-env.git
cd tiny-vm-desktop-env
Install Python dependencies:
pip install -r requirements.txt
Run the setup script to initialize the environment:
python setup.py install
Running the Project

After installation, you can launch the desktop environment:

python run.py

This will start the Tiny VM Desktop Environment, which will manage the virtual machines and provide you with the graphical interface.

Troubleshooting
Error: "Virtualization is not enabled": Make sure virtualization is enabled in your BIOS/UEFI settings.
Error: "Cannot find QEMU/VirtualBox": Ensure that the virtualization software is installed and accessible via the command line.
Performance issues: This environment is designed for low-resource machines, but performance can still vary depending on your hardware. Consider using less resource-intensive virtual machines if you encounter issues.
