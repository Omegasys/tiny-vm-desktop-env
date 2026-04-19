import unittest
from src.components.terminal import Terminal

class TestTerminal(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of Terminal before each test."""
        self.terminal = Terminal()

    def test_execute_command(self):
        """Test executing a shell command."""
        self.terminal.execute_command("echo 'Hello, World!'")
        self.assertIn("echo 'Hello, World!'", self.terminal.history)

    def test_show_history(self):
        """Test showing command history."""
        self.terminal.execute_command("echo 'Hello'")
        self.terminal.execute_command("echo 'World'")
        history = self.terminal.show_history()
        self.assertEqual(history, ["echo 'Hello'", "echo 'World'"])

if __name__ == "__main__":
    unittest.main()
