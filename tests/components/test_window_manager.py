import unittest
from src.components.window_manager import WindowManager

class TestWindowManager(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of WindowManager before each test."""
        self.window_manager = WindowManager()

    def test_open_window(self):
        """Test that opening a window adds it to the open windows list."""
        self.window_manager.open_window("Main Window")
        self.assertIn("Main Window", self.window_manager.open_windows)

    def test_close_window(self):
        """Test that closing a window removes it from the open windows list."""
        self.window_manager.open_window("Main Window")
        self.window_manager.close_window("Main Window")
        self.assertNotIn("Main Window", self.window_manager.open_windows)

    def test_list_windows(self):
        """Test listing all open windows."""
        self.window_manager.open_window("Main Window")
        self.window_manager.open_window("Settings Window")
        windows = self.window_manager.list_windows()
        self.assertEqual(windows, ["Main Window", "Settings Window"])

if __name__ == "__main__":
    unittest.main()
