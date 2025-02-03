import sqlite3
from datetime import datetime, timedelta
import pytz
import streamlit as st

class SessionManager:
    def __init__(self, db_path="databases/sessions.db"):
        self.db_path = db_path

    def _get_current_time(self):
        """Get the current time in GMT+3."""
        return datetime.now(pytz.timezone("Etc/GMT-3")).strftime("%Y-%m-%d %H:%M:%S")

    def generate_session_id(self, user_id):
        """Generate a unique session ID based on user ID and timestamp."""
        timestamp = datetime.now(pytz.timezone("Etc/GMT-3")).strftime("%Y%m%d%H%M%S%f")
        session_id = f"{timestamp}{user_id}"
        return session_id

    def create_session(self, user_id):
        """Create a new session for the given user ID."""
        session_id = self.generate_session_id(user_id)
        created_at = self._get_current_time()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO sessions (session_id, user_id, session_created_at, session_last_activity, is_active)
                VALUES (?, ?, ?, ?, ?)
                """,
                (session_id, user_id, created_at, created_at, 1),  # 1: active, 0: not active
            )
            conn.commit()
        st.session_state["session_id"] = session_id
        st.session_state["user_id"] = user_id
        st.session_state["last_activity"] = created_at
        return session_id

    def validate_session(self, session_id):
        """Validate if the current session is active."""
        if not session_id:
            return False
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT session_last_activity, is_active FROM sessions WHERE session_id = ?", (session_id,)
            )
            result = cursor.fetchone()
        if result:
            last_activity_str = result[0]
            is_active = result[1]
            # Convert last_activity_str to offset-aware datetime
            last_activity = datetime.strptime(last_activity_str, '%Y-%m-%d %H:%M:%S')
            last_activity = pytz.timezone("Etc/GMT-3").localize(last_activity)  # Make it offset-aware
            # Get current time as offset-aware datetime
            current_time = datetime.now(pytz.timezone("Etc/GMT-3"))
            # Check if session is active and last activity is within 10 minutes
            if is_active and (current_time - last_activity) < timedelta(minutes=10):
                return True
            else:
                # Oturum süresi dolmuşsa, oturumu pasif hale getir
                self.deactivate_session(session_id)
        return False

    def deactivate_session(self, session_id):
        """Deactivate the session."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE sessions SET is_active = 0 WHERE session_id = ?", (session_id,)
            )
            conn.commit()

    def update_last_activity(self, session_id):
        """Update the last activity time for the current session."""
        if not session_id:
            return
        last_activity = self._get_current_time()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE sessions SET session_last_activity = ? WHERE session_id = ?", (last_activity, session_id)
            )
            conn.commit()
        st.session_state["last_activity"] = last_activity

    def deactivate_other_sessions(self, user_id, current_session_id):
        """Deactivate other active sessions for the same user."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE sessions SET is_active = 0 WHERE user_id = ? AND session_id != ?", (user_id, current_session_id)
            )
            conn.commit()

    def end_session(self):
        """End the current session."""
        if "session_id" not in st.session_state or not st.session_state["session_id"]:
            return
        session_id = st.session_state["session_id"]
        self.deactivate_session(session_id)
        st.session_state["session_id"] = None
        st.session_state["user_id"] = None
        st.session_state["last_activity"] = None

    def logout(self):
        """Logout the user by ending the session and clearing the session state."""
        self.end_session()
        if "sidebar_state" in st.session_state:
            del st.session_state["sidebar_state"]
        st.rerun()