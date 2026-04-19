# session.py

class SessionManager:
    def __init__(self):
        self.current_session = None

    def create_session(self, user_name):
        """Create a new session for a user."""
        self.current_session = {
            "user": user_name,
            "session_id": self.generate_session_id(),
            "settings": {}
        }
        print(f"Session created for user: {user_name}")
    
    def load_session(self):
        """Load the current user session."""
        if self.current_session:
            print(f"Session loaded for user: {self.current_session['user']}")
        else:
            print("No active session found.")
    
    def save_session(self):
        """Save the current session."""
        if self.current_session:
            print(f"Session for {self.current_session['user']} saved.")
        else:
            print("No active session to save.")
    
    def generate_session_id(self):
        """Generate a unique session ID."""
        import uuid
        return str(uuid.uuid4())
