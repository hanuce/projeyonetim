import streamlit as st
import sqlite3
from apps.webapps import web_app

def sign_in_page():
    # Oturum kontrolü
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    # Veritabanı bağlantısı
    conn = sqlite3.connect('databases/database.sqlite')
    cursor = conn.cursor()

    # Kullanıcı adı ve şifre alanları
    st.title("Giriş Yap")
    username = st.text_input("Kullanıcı Adı:")
    password = st.text_input("Şifre:", type="password")

    # Giriş yap butonu
    if st.button("Giriş Yap"):
        if authenticate_user(username, password, cursor):
            st.success("Başarıyla giriş yaptınız!")
            st.session_state["authenticated"] = True
            st.experimental_rerun()  # Oturum açıldıktan sonra sayfayı yeniden yükle
        else:
            st.error("Kullanıcı adı veya şifre yanlış!")

    # Şifremi unuttum ve Üye ol bağlantıları
    st.markdown("[Şifrenizi mi Unuttunuz?](#)", unsafe_allow_html=True)
    st.markdown("[Üye Ol](#)", unsafe_allow_html=True)

    # Yetkili kullanıcıyı yönlendirme
    if st.session_state["authenticated"]:
        web_app()

    # Veritabanı bağlantısını kapat
    conn.close()

# Kullanıcı doğrulama işlevi
def authenticate_user(username, password, cursor):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        return True
    return False

# sign_in_page() fonksiyonunu çağırmak
if __name__ == "__main__":
    sign_in_page()