import re
import streamlit as st

def validate_email(func):
    def wrapper(user_data, *args, **kwargs):
        email = user_data.get("user_email", "")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            st.warning("Geçersiz e-posta formatı.")
            return False
        return func(user_data, *args, **kwargs)
    return wrapper

def validate_password(func):
    def wrapper(user_data, *args, **kwargs):
        password = user_data.get("user_password", "")
        if len(password) < 6:
            st.warning("Şifre en az 6 karakter uzunluğunda olmalı.")
            return False
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.,;!+\-*:%()=?_]).+$'
        if not re.match(pattern, password):
            st.warning("Şifre, büyük harf, küçük harf, rakam ve özel karakter içermeli.")
            return False
        return func(user_data, *args, **kwargs)
    return wrapper

def check_email_registered(user_manager):  # user_manager'ı parametre olarak al
    def decorator(func):
        def wrapper(user_data, *args, **kwargs):
            email = user_data.get("user_email", "")
            if user_manager.is_email_registered(email):
                st.warning("Bu e-posta adresi zaten kayıtlı.")
                return False
            return func(user_data, *args, **kwargs)
        return wrapper
    return decorator