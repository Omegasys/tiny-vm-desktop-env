import unittest
from src.utils import utils

class TestUtils(unittest.TestCase):

    def test_is_valid_path(self):
        """Test the path validation function."""
        valid_path = "/tmp"
        invalid_path = "/invalid/path"
        self.assertTrue(utils.is_valid_path(valid_path))
        self.assertFalse(utils.is_valid_path(invalid_path))

    def test_create_directory(self):
        """Test the create directory function."""
        test_dir = "/tmp/test_directory"
        utils.create_directory(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        # Clean up
        os.rmdir(test_dir)

    def test_copy_file(self):
        """Test the copy file function."""
        source = "/tmp/source.txt"
        destination = "/tmp/destination.txt"
        with open(source, "w") as f:
            f.write("Test content")
        utils.copy_file(source, destination)
        self.assertTrue(os.path.exists(destination))
        # Clean up
        os.remove(source)
        os.remove(destination)

if __name__ == "__main__":
    unittest.main()
