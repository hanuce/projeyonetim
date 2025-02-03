#app.py
import streamlit as st
from core.user_manager import UserManager
from core.menu_manager import MenuManager
from core.session_manager import SessionManager

# Ana uygulama
def show_apps():
    # SessionManager başlat
    session_manager = SessionManager()

    # Sidebar'ın açık gelmesini sağla
    st.session_state.sidebar_state = "expanded"
    
    # Oturum geçerli mi?
    if not session_manager.validate_session(st.session_state.get("session_id")):
        session_manager.logout()  # Oturum geçersizse logout yap
        return

    # Kullanıcı girişi yapmış mı?
    if not st.session_state.get("user_id"):
        st.rerun()  # Kullanıcı girişi yoksa sayfayı yeniden yükle
        return
    
    # Çıkış butonu
    if st.sidebar.button("Çıkış Yap"):
        session_manager.logout()  # Çıkış yap butonuna basıldığında logout yap
        return
    
    # Sidebar'da logo göster
    with st.sidebar:
        st.logo("images/logo_horizontal.svg", size="large")  # Logo boyutunu küçült

    # Menüyü oluştur ve göster
    menu_manager = MenuManager()
    menu_items = menu_manager.get_menu_items(st.session_state.user_id)
    
    # Sayfaları grupla ve st.navigation'a uygun hale getir
    page_dict = {category: pages for category, pages in menu_items.items()}
    
    # Navigasyon menüsünü oluştur ve çalıştır
    with st.sidebar:
        pg = st.navigation(page_dict)
    pg.run()

# Uygulamayı başlat
if __name__ == "__main__":
    show_apps()