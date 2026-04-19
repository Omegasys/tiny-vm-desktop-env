# vm_manager.py
import subprocess
import os

class VMManager:
    def __init__(self, vm_name, memory, cpu, disk_size):
        self.vm_name = vm_name
        self.memory = memory
        self.cpu = cpu
        self.disk_size = disk_size
        self.vm_running = False

    def create_vm(self):
        """Creates a new virtual machine."""
        disk_path = f"/var/lib/vms/{self.vm_name}.qcow2"
        
        if not os.path.exists(disk_path):
            os.makedirs(os.path.dirname(disk_path), exist_ok=True)
            subprocess.run([
                "qemu-img", "create", "-f", "qcow2", disk_path, str(self.disk_size) + "G"
            ])
            print(f"Disk image created at {disk_path}")
        
        print(f"Creating virtual machine {self.vm_name} with {self.memory}GB RAM and {self.cpu} CPUs.")
        # Further VM creation logic will be here

    def start_vm(self):
        """Starts the VM."""
        if not self.vm_running:
            subprocess.run([
                "qemu-system-x86_64", "-m", str(self.memory) + "G", "-smp", str(self.cpu), 
                "-hda", f"/var/lib/vms/{self.vm_name}.qcow2", "-boot", "d", "-enable-kvm"
            ])
            self.vm_running = True
            print(f"VM {self.vm_name} started.")
        else:
            print(f"VM {self.vm_name} is already running.")

    def stop_vm(self):
        """Stops the VM."""
        if self.vm_running:
            subprocess.run(["killall", "qemu-system-x86_64"])  # Assumes one VM running
            self.vm_running = False
            print(f"VM {self.vm_name} stopped.")
        else:
            print(f"VM {self.vm_name} is not running.")
