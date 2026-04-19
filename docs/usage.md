```markdown
# Usage Guide for Tiny VM Desktop Environment

This guide provides detailed instructions on how to use the Tiny VM Desktop Environment once it is set up and running.

## Starting the Desktop Environment

Once you have the environment set up, you can launch the desktop by running:

```bash
python run.py

This will start the VM manager, load the GUI, and begin managing virtual machines. You will see a window with the taskbar, a file explorer, and a terminal for interaction.

Managing Virtual Machines
Creating a New VM

To create a new virtual machine:

Click on the VM Manager button in the taskbar.
Select "New VM" and configure the VM's settings (e.g., memory, CPU, disk size).
Click "Create" to spin up the VM.
Starting/Stopping a VM

To start or stop a virtual machine:

Open the VM Manager.
Select the VM you want to manage.
Use the Start or Stop buttons to control the VM.
Viewing the VM's Console

Once the VM is running, click on it to open a console window. You can interact with the VM as if it were a physical machine.

Using the File Explorer
Browsing Files

Click the File Explorer icon from the taskbar to open the file manager. This will allow you to browse the VM's file system.

Use the sidebar to navigate between directories.
Double-click files to open them.
Managing Files

You can copy, move, delete, and rename files within the VM's file system through the file explorer interface.

Terminal Usage

The Terminal application is available for advanced users to interact directly with the VM's shell. You can run commands, install software, or configure the system via this terminal.

Adjusting System Settings
Changing Appearance

To change the desktop theme (e.g., light or dark mode):

Click on the Settings icon in the taskbar.
Navigate to the Appearance section.
Choose your preferred theme.
Network Configuration

You can manage the VM's network settings via the Network Manager. This allows you to configure NAT, bridged, or host-only networking modes for the VM.

Shutting Down

To shut down the environment:

Close all running VMs.
Click on the Shutdown option from the taskbar.
Confirm the shutdown to stop the environment.
