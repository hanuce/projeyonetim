from .db_manager import DatabaseManager
from .query_manager import QueryManager
from .user_manager import UserManager
from .session_manager import SessionManager
from .project_manager import ProjectManager
from .menu_manager import get_menu_items
from .validation import validate_email, validate_password, check_email_registered

class ServiceManager:
    def __init__(self, query_manager):
        self.query_manager = query_manager

    def get_institutes(self):
        query = "SELECT institute_name FROM institutes"
        return [row[0] for row in self.query_manager.fetch_all(query)]

    def get_user_roles(self, user_type):
        query = "SELECT user_role_detail FROM user_roles WHERE user_type = :user_type"
        return [row[0] for row in self.query_manager.fetch_all(query, {"user_type": user_type})]

    def is_email_registered(self, email):
        query = "SELECT user_email FROM user_basics WHERE user_email = :email"
        return self.query_manager.fetch_one(query, {"email": email}) is not None

    def register_user(self, user_data):
        query = """
        INSERT INTO user_basics (user_name, user_last_name, user_email, user_password, user_institute, user_role_detail)
        VALUES (:user_name, :user_last_name, :user_email, :user_password, :user_institute, :user_role_detail)
        """
        self.query_manager.execute_query(query, user_data)