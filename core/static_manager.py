#static_manager.py
import sqlite3

class StaticManager:
    def __init__(self, db_path="databases/statics.db"):
        self.db_path = db_path

    def _connect(self):
        """Connect to the SQLite database."""
        return sqlite3.connect(self.db_path)

    def get_institutes(self):
        """Retrieve a list of all available institutes with their IDs and titles."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT institute_id, institute_title FROM institutes")
            return cursor.fetchall()  # Returns a list of tuples: [(id, title), ...]

    def get_student_levels(self):
        """Retrieve a list of all student levels with their IDs and details."""
        query = "SELECT level_id, level_detail FROM student_levels"
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()  # Returns a list of tuples: [(id, detail), ...]

    def get_teacher_branches(self):
        """Retrieve a list of all teacher branches with their IDs and details."""
        query = "SELECT branch_id, branch_detail FROM teacher_branches ORDER BY branch_id"
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()  # Returns a list of tuples: [(id, detail), ...]