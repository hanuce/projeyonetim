#core/menu_manager.py
from entrance import page_about, page_contact, page_pricing, page_pys, page_sign, page_team
from core.user_manager import UserManager
import streamlit as st
import os


class MenuManager:
    def __init__(self):
        self.guest_menu = {
            "__PYS__": page_pys.show,
            "__Amaçlar__": page_about.show,
            "__Ekibimiz__": page_team.show,
            "__Ücretlendirme__": page_pricing.show,
            "__İletişim__": page_contact.show,
            "__Giriş Yap__": page_sign.show,
        }

        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # core/ dizininden bir üst dizine çık

        self.system_root_menu = {
            "Root 1": st.Page(page="apps/system/root/root_ui1.py", title="Root 1"),
            "Root 2": st.Page(page="apps/system/root/root_ui2.py", title="Root 2"),
        }
        
        self.system_admin_menu = {
            "Admin 1": st.Page(page="apps/system/admin/admin_ui1.py", title="Admin 1"),
            "Admin 2": st.Page(page="apps/system/admin/admin_ui2.py", title="Admin 2"),
        }
        
        self.school_institute_menu = {
            "School Institute 1": st.Page(page="apps/school/institute/institute_ui1.py", title="School Institute 1"),
            "School Institute 2": st.Page(page="apps/school/institute/institute_ui2.py", title="School Institute 2"),
        }
        
        self.school_manager_menu = {
            "School Manager 1": st.Page(page="apps/school/manager/manager_ui1.py", title="School Manager 1"),
            "School Manager 2": st.Page(page="apps/school/manager/manager_ui2.py", title="School Manager 2"),
        }
        
        self.school_teacher_menu = {
            "Öğretmen 1": st.Page(page="apps/school/teacher/teacher_ui1.py", title="Öğretmen 1"),
            "Öğretmen 2": st.Page(page="apps/school/teacher/teacher_ui2.py", title="Öğretmen 2"),
        }
        
        self.school_student_menu = {
            "Öğrenci 1": st.Page(page="apps/school/student/student_ui1.py", title="Öğrenci 1"),
            "Öğrenci 2": st.Page(page="apps/school/student/student_ui2.py", title="Öğrenci 2"),
        }

        self.role_mapping = {
            101: ("System Root", self.system_root_menu),
            102: ("System Admin", self.system_admin_menu),
            501: ("School Institute", self.school_institute_menu),
            503: ("School Manager", self.school_manager_menu),
            506: ("School Teacher", self.school_teacher_menu),
            507: ("School Student", self.school_student_menu),
        }

    def get_menu_items(self, user_id):
        """Get menu items based on user roles."""
        if user_id is None:
            return self.guest_menu
        
        user_manager = UserManager()
        main_role = user_manager.get_user_main_role(user_id)
        additional_roles = user_manager.get_additional_roles(user_id)
        
        menu_items = {}
        
        # Main role'u ekle
        if main_role:
            main_role_id = int(main_role)
            if main_role_id in self.role_mapping:
                category, pages = self.role_mapping[main_role_id]
                menu_items[f"⏩ {category} ⏪"] = list(pages.values())  # Kategori başlığına ikon ekle
        
        # Additional roles'u ekle
        if additional_roles:  # additional_roles boş değilse
            for role_id in additional_roles:
                role_id = int(role_id)
                if role_id in self.role_mapping:
                    category, pages = self.role_mapping[role_id]
                    if f"⏩ {category} ⏪" not in menu_items:  # Eğer kategori yoksa, oluştur
                        menu_items[f"⏩ {category} ⏪"] = []
                    menu_items[f"⏩ {category} ⏪"].extend(list(pages.values()))
         
        return menu_items

