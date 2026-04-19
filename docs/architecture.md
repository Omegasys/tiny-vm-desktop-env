# System Architecture of Tiny VM Desktop Environment

This document outlines the high-level architecture of the "Tiny VM Desktop Environment" project. The system is designed to run on lightweight virtual machines and provide a minimal desktop experience. It is composed of the following main components:

## Overview

The Tiny VM Desktop Environment is built around the concept of virtual machines running in isolated environments, with a graphical user interface (GUI) to provide user interaction. The system is modular, with each module responsible for a specific feature or functionality.

## Key Components

### 1. **VM Manager**
   - The VM Manager handles the lifecycle of virtual machines. It is responsible for:
     - Creating new VMs
     - Starting, pausing, and stopping VMs
     - Managing virtual disk and networking
   - This component interacts with the underlying hypervisor (e.g., QEMU, VirtualBox).

### 2. **Graphical User Interface (GUI)**
   - The GUI is a lightweight desktop environment designed for low resource consumption. It is composed of:
     - **Window Manager**: Manages windows, their layout, and user interactions.
     - **Taskbar**: Provides access to running applications and system functions.
     - **File Explorer**: Lets users browse and manage files in the virtual environment.
     - **Terminal**: Provides shell access to the underlying VM.

### 3. **Session Manager**
   - The Session Manager manages user sessions and preferences. It tracks:
     - Active user sessions
     - User-specific settings and configurations
     - Input devices (keyboard, mouse) for the virtual machine

### 4. **Network Manager**
   - The Network Manager manages network interfaces and settings for the VMs, including:
     - Configuring networking mode (NAT, bridged, host-only)
     - Managing virtual network adapters

### 5. **File System & Storage**
   - Each VM has its own virtual file system, and the file manager interacts with the VM's storage to provide file access and organization.
   - Support for virtual disk images (e.g., QCOW2, VDI).

## Communication Flow

1. **User Interaction**: The user interacts with the GUI, which sends requests to the respective components (e.g., Window Manager, VM Manager, etc.).
2. **VM Creation**: The VM Manager spins up a new virtual machine based on the user's request.
3. **Resource Management**: The system keeps track of CPU, RAM, and storage usage for each VM, ensuring resource allocation is efficient.
4. **Running Applications**: Applications within the VM interact with the Window Manager and File Manager for UI display and file management.

## Conclusion

This architecture allows for a modular, scalable desktop environment that can run on minimal hardware, making it suitable for low-resource environments or embedded systems. Each component is designed to be lightweight but extensible, with the ability to add new features over time.
