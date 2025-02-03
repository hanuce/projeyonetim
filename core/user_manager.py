#user_manager.py
import sqlite3
import hashlib
import datetime

class UserManager:
    def __init__(self, db_path="databases/users.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def get_user_by_email(self, email):
        """Retrieve user data by email."""
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row  # To access columns by name
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_email = ?", (email,))
            return cursor.fetchone()

    def _generate_user_id(self, user_institute_id, user_main_role_id, user_detail_id):
        """
        Generate a unique integer user_id based on the given parameters.
        Format: user_institute_id + user_main_role_id + user_detail_id + (count + 1)
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT COUNT(*) FROM users 
                WHERE user_institute_id = ? AND user_main_role = ? AND user_detail_id = ?
                """,
                (user_institute_id, user_main_role_id, user_detail_id),
            )
            count = cursor.fetchone()[0]
            
            # user_main_role_id'yi 4 basamaklı yap (önüne sıfır ekle)
            formatted_user_detail_id = f"{int(user_detail_id):04d}"
            
            # Combine the parts to form a unique integer user_id
            user_id = int(f"{user_institute_id}{user_main_role_id}{formatted_user_detail_id}{count + 1:04d}")
            return user_id

    def register_user(self, user_data):
        """Register a new user with the provided data."""
        hashed_password = self._hash_password(user_data["user_password"])
        user_data["user_password"] = hashed_password
        user_data["user_created_at"] = datetime.datetime.utcnow().isoformat()
        # Generate user_id
        user_id = self._generate_user_id(
            user_data["user_institute_id"],
            user_data["user_main_role"],
            user_data["user_detail_id"],
        )
        with self._connect() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    INSERT INTO users (
                        user_id, user_name, user_lastname, user_email, user_password,
                        user_main_role, user_detail_id, user_status, user_gender, user_institute_id,
                        user_bio, user_approved_by, user_created_at
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        user_id,
                        user_data["user_name"],
                        user_data["user_last_name"],
                        user_data["user_email"],
                        user_data["user_password"],
                        user_data["user_main_role"],
                        user_data["user_detail_id"],
                        1,  # 0: deleted, 1:pending, 2:active
                        user_data["gender"],
                        user_data["user_institute_id"],
                        "",  # Bio can be updated later
                        0,  # approver_id by will be set later
                        user_data["user_created_at"],
                    ),
                )
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False

    def _hash_password(self, password):
        """Hash a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, email, password):
        """Verify the password for a given email."""
        user = self.get_user_by_email(email)
        if user:
            hashed_password = self._hash_password(password)
            return user["user_password"] == hashed_password
        return False

    def get_institutes(self):
        """Retrieve a list of all institutes."""
        with sqlite3.connect("databases/statics.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT institute_title FROM institutes")
            return [row[0] for row in cursor.fetchall()]

    def get_user_roles(self, role_level):
        """Retrieve roles based on level (e.g., teacher or student)."""
        with sqlite3.connect("databases/statics.db") as conn:
            cursor = conn.cursor()
            if role_level == 2:
                cursor.execute("SELECT level_detail FROM student_levels")
            elif role_level == 3:
                cursor.execute("SELECT branch_detail FROM `teacher branches`")
            return [row[0] for row in cursor.fetchall()]

    def get_user_main_role(self, user_id):
        """Retrieve the main role of a user."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT user_main_role FROM users WHERE user_id = ?", (user_id,))
            result = cursor.fetchone()
            return result[0] if result else None

    def get_additional_roles(self, user_id):
        """Retrieve additional roles of a user."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT additional_role_id FROM additional_roles WHERE user_id = ?", (user_id,))
            results = cursor.fetchall()
            return [row[0] for row in results]