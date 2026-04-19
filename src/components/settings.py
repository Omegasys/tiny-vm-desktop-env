# settings.py

class Settings:
    def __init__(self):
        self.config = {
            "theme": "light",
            "vm_startup": True
        }
    
    def get_setting(self, key):
        """Retrieves a configuration setting."""
        return self.config.get(key, None)
    
    def set_setting(self, key, value):
        """Sets a configuration setting."""
        self.config[key] = value
        print(f"Setting {key} updated to {value}")
    
    def reset_settings(self):
        """Resets all settings to defaults."""
        self.config = {
            "theme": "light",
            "vm_startup": True
        }
        print("Settings have been reset to default.")
