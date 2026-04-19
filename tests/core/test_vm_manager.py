import unittest
from src.core.vm_manager import VMManager
from unittest.mock import patch

class TestVMManager(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of VMManager before each test."""
        self.vm_manager = VMManager(vm_name="TestVM", memory=2, cpu=1, disk_size=10)

    @patch("subprocess.run")
    def test_create_vm(self, mock_subprocess):
        """Test the VM creation process."""
        self.vm_manager.create_vm()
        mock_subprocess.assert_called_once_with([
            "qemu-img", "create", "-f", "qcow2", "/var/lib/vms/TestVM.qcow2", "10G"
        ])
    
    @patch("subprocess.run")
    def test_start_vm(self, mock_subprocess):
        """Test the VM start process."""
        self.vm_manager.start_vm()
        mock_subprocess.assert_called_once_with([
            "qemu-system-x86_64", "-m", "2G", "-smp", "1", "-hda", "/var/lib/vms/TestVM.qcow2", 
            "-boot", "d", "-enable-kvm"
        ])
    
    @patch("subprocess.run")
    def test_stop_vm(self, mock_subprocess):
        """Test the VM stop process."""
        self.vm_manager.start_vm()  # Ensure VM is started
        self.vm_manager.stop_vm()
        mock_subprocess.assert_called_once_with(["killall", "qemu-system-x86_64"])

if __name__ == "__main__":
    unittest.main()
