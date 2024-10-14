import streamlit as st
from streamlit_option_menu import option_menu
import sayfalar as sayfa


st.set_page_config(
    page_title="Proje Yönetim",
    page_icon=":flag-tr:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CSS dosyasını yüklemek
with open("styles/custom.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

logo_url = "https://via.placeholder.com/80"  # Sözde logo resmi
logo_option = f'<img src="{logo_url}" style="height: 50px;">'  # Logo yüksekliği ayarlandı


selected = option_menu(
    menu_title=None,  # Menü başlığı
    options=["PYS","Neden?", "Ekibimiz", "Ücretlendirme", "İletişim","Giriş Yap"],  # Menü öğeleri
    icons=["grid-3x3-gap-fill","info-circle", "people", "wallet2", "envelope", "box-arrow-in-right"],  # İkonlar (isteğe bağlı)
    menu_icon=None,  # Menü ikonu
    default_index=0,  # Varsayılan seçili öğe
    orientation="horizontal", # Yatay menü
)

# Seçili öğeye göre içerik gösterimi
with st.container():
    if selected == "PYS":
        sayfa.show_pys()  # PYS (Anasayfa) sayfasını göster
    elif selected == "Neden?":
        sayfa.show_neden() # Neden sayfasını göster
    elif selected == "Ekibimiz":
        sayfa.show_ekip() # Ekibimiz  sayfasını göster
    elif selected == "Ücretlendirme":
        sayfa.show_ucret() # Ücretlendirme  sayfasını göster
    elif selected == "İletişim":
        sayfa.show_iletisim() # İetlişim  sayfasını göster



st.markdown("---")  # Ayrım çizgisi
footer_content = """
© 2024. Görseller: <a href='https://undraw.co/illustrations'> undraw.co</a> | Özgün Hakları Saklıdır.
<a href='#'>Github</a> | <a href='#'>X.com</a>
"""
st.markdown(footer_content, unsafe_allow_html=True)  # Footer içeriği