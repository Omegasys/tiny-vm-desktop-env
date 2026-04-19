# terminal.py

class Terminal:
    def __init__(self):
        self.history = []
    
    def execute_command(self, command):
        """Executes a shell command."""
        print(f"Executing: {command}")
        self.history.append(command)
    
    def show_history(self):
        """Displays command history."""
        print("Command History:")
        for cmd in self.history:
            print(cmd)
