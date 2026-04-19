# utils.py

import os
import shutil

def is_valid_path(path):
    """Checks if a given path is valid."""
    return os.path.exists(path)

def create_directory(path):
    """Creates a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created at {path}")
    else:
        print(f"Directory already exists at {path}")

def copy_file(source, destination):
    """Copies a file from source to destination."""
    if os.path.exists(source):
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}")
    else:
        print(f"Source file {source} does not exist.")
