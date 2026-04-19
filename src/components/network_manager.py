# network_manager.py

class NetworkManager:
    def __init__(self):
        self.network_config = {
            "mode": "NAT",
            "interface": "eth0"
        }
    
    def configure_network(self, mode, interface):
        """Configures network settings for the VM."""
        self.network_config["mode"] = mode
        self.network_config["interface"] = interface
        print(f"Network configured: {mode} mode on {interface}")
    
    def show_config(self):
        """Shows the current network configuration."""
        print(f"Network Mode: {self.network_config['mode']}")
        print(f"Network Interface: {self.network_config['interface']}")
