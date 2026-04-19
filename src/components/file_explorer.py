# file_explorer.py

import os

class FileExplorer:
    def __init__(self, root_path):
        self.root_path = root_path
    
    def list_files(self):
        """Lists all files and directories in the root path."""
        if os.path.exists(self.root_path):
            return os.listdir(self.root_path)
        else:
            print(f"The path {self.root_path} does not exist.")
            return []
    
    def open_file(self, file_name):
        """Opens a file (just prints its content for now)."""
        file_path = os.path.join(self.root_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                print(file.read())
        else:
            print(f"File {file_name} not found in {self.root_path}.")
