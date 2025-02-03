#index.py
import streamlit as st
from streamlit_extras.button_selector import button_selector
from core import SessionManager, MenuManager
import apps  # apps/__init__.py'den show_apps fonksiyonunu içe aktardık
import os

# Çalışma dizinini ayarla
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Sayfa yapılandırması (script'in en başında)
st.set_page_config(
    page_title="Proje Yönetim",
    page_icon=":flag-tr:",
    layout="wide",
    initial_sidebar_state="auto",  # Sidebar başlangıçta kapalı
)

# SessionManager ve MenuManager başlatılıyor
session_manager = SessionManager()
menu_manager = MenuManager()

# Oturum kontrolü ve sayfa yönlendirmesi
def handle_session_and_routing():
    # Oturum durumunu başlat
    st.session_state.setdefault("session_id", None)
    st.session_state.setdefault("user_id", None)
    st.session_state.setdefault("last_activity", None)
    st.session_state.setdefault("sidebar_state", "collapsed")

    # Eğer oturum ID ve kullanıcı ID varsa, oturumu kontrol et
    if st.session_state.session_id and st.session_state.user_id:
        if session_manager.validate_session(st.session_state.session_id):
            # Oturum geçerliyse, last_activity'yi güncelle
            session_manager.update_last_activity(st.session_state.session_id)
            # Diğer aktif oturumları devre dışı bırak
            session_manager.deactivate_other_sessions(st.session_state.user_id, st.session_state.session_id)
            # Uygulama sayfasını göster
            app_page()
        else:
            # Oturum süresi dolduysa veya geçersizse oturumu temizle
            session_manager.logout()
            st.rerun()
    else:
        # Oturum yoksa, karşılama sayfasını göster
        main_page()

# Karşılama sayfası (giriş yapmayan kullanıcılar için)
def main_page():
    menu_items = menu_manager.get_menu_items(st.session_state.user_id)  # Kullanıcıya göre menüyü al
    with st.container():
        # Logo ve menü sütunları
        col_logo, menu_cols = st.columns([1, len(menu_items)])
        with col_logo:
            st.image("images/logo.svg", width=40)
        with menu_cols:
            selected_index = button_selector(
                list(menu_items.keys()),
                key="menu_selector",
                spec=6,
                index=0,
            )
            st.session_state.selected_index = selected_index
    # İçerik gösterimi (doğrudan çağırım)
    with st.container():
        selected_menu = list(menu_items.keys())[st.session_state.selected_index]
        menu_items[selected_menu]()

    # Sidebar'ı kontrol et
    st.session_state.sidebar_state = "collapsed"
    # Sidebar'ı gizle
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Uygulama sayfası (giriş yapan kullanıcılar için)
def app_page():
    apps.show_apps()

# Ana işlem
if __name__ == "__main__":
    handle_session_and_routing()

# Footer
st.markdown("---")  # Ayrım çizgisi
footer_content = """
© 2024. Görseller: <a href='https://undraw.co/illustrations'> undraw.co</a> | Özgün Hakları Saklıdır.
<a href='#'>Github</a> | <a href='#'>X.com</a>
"""
st.markdown(footer_content, unsafe_allow_html=True)  # Footer içeriği