import unittest
from unittest.mock import patch
from src.components.file_explorer import FileExplorer
import os

class TestFileExplorer(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of FileExplorer before each test."""
        self.file_explorer = FileExplorer(root_path="/tmp/test_vm")
        os.makedirs(self.file_explorer.root_path, exist_ok=True)  # Ensure the directory exists for testing

    def tearDown(self):
        """Clean up after tests."""
        for file in os.listdir(self.file_explorer.root_path):
            file_path = os.path.join(self.file_explorer.root_path, file)
            os.remove(file_path)
        os.rmdir(self.file_explorer.root_path)

    def test_list_files(self):
        """Test listing files in the directory."""
        with open(os.path.join(self.file_explorer.root_path, "file1.txt"), "w") as f:
            f.write("Hello, World!")
        
        files = self.file_explorer.list_files()
        self.assertIn("file1.txt", files)

    @patch("builtins.open", create=True)
    def test_open_file(self, mock_open):
        """Test opening a file."""
        self.file_explorer.open_file("file1.txt")
        mock_open.assert_called_with(os.path.join(self.file_explorer.root_path, "file1.txt"), "r")

if __name__ == "__main__":
    unittest.main()
