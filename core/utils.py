import re

def validate_email(func):
    def wrapper(user_data, *args, **kwargs):
        email = user_data.get("user_email", "")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Geçersiz e-posta formatı.")
        return func(user_data, *args, **kwargs)
    return wrapper

def validate_password(func):
    def wrapper(user_data, *args, **kwargs):
        password = user_data.get("user_password", "")
        if len(password) < 6:
            raise ValueError("Şifre en az 6 karakter uzunluğunda olmalı.")
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.,;!+\-*:%()=?_]).+$'
        if not re.match(pattern, password):
            raise ValueError("Şifre, büyük harf, küçük harf, rakam ve özel karakter içermeli.")
        return func(user_data, *args, **kwargs)
    return wrapper

def check_email_registered(func):
    def wrapper(user_data, user_manager, *args, **kwargs):
        email = user_data.get("user_email", "")
        if user_manager.is_email_registered(email):
            raise ValueError("Bu e-posta adresi zaten kayıtlı.")
        return func(user_data, user_manager, *args, **kwargs)
    return wrapper
