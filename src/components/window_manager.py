# window_manager.py

class WindowManager:
    def __init__(self):
        self.open_windows = []
    
    def open_window(self, window_name):
        """Opens a new window."""
        self.open_windows.append(window_name)
        print(f"Window {window_name} opened.")
    
    def close_window(self, window_name):
        """Closes an existing window."""
        if window_name in self.open_windows:
            self.open_windows.remove(window_name)
            print(f"Window {window_name} closed.")
        else:
            print(f"Window {window_name} not found.")
    
    def list_windows(self):
        """Lists all currently open windows."""
        return self.open_windows
