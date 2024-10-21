import streamlit as st
from streamlit_option_menu import option_menu
from entrance.index import show_page
import apps.web_app as app_module

st.set_page_config(
    page_title="Proje Yönetim",
    page_icon=":flag-tr:",
    layout="wide",
    initial_sidebar_state="auto",
)

# CSS dosyasını yüklemek
with open("styles/custom.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

if 'is_logged_in' not in st.session_state: st.session_state.is_logged_in = False

# Kullanıcı girşi yapmayanlar sitenin karşılama sayfalarını gösterme
def main_page():

    logo_url = "https://via.placeholder.com/80"  # Sözde logo resmi
    logo_option = f'<img src="{logo_url}" style="height: 50px;">'  # Logo yüksekliği ayarlandı

    # option-menu kütüphanesi ile yatay menü yapımı ve menüler
    selected = option_menu(
        menu_title=None,  # Menü başlığı
        options=["PYS","Neden?", "Ekibimiz", "Ücretlendirme", "İletişim","Giriş Yap"],  # Menü öğeleri
        icons=["grid-3x3-gap-fill","info-circle", "people", "wallet2", "envelope", "box-arrow-in-right"],  # İkonlar (isteğe bağlı)
        menu_icon=None,  # Menü ikonu
        default_index=0,  # Varsayılan seçili öğe
        orientation="horizontal", # Yatay menü
    )

    # Seçili menüye göre içerik gösterimi
    with st.container():
        show_page(selected)

def app_page():
    app_module.show_apps()

    
# Kullanıcı login olduysa app_page fonksiyonu değilse main_page fonskiyonunu çalıştır.
if st.session_state.is_logged_in:
    app_page()
else:
    main_page()

st.markdown("---")  # Ayrım çizgisi
footer_content = """
© 2024. Görseller: <a href='https://undraw.co/illustrations'> undraw.co</a> | Özgün Hakları Saklıdır.
<a href='#'>Github</a> | <a href='#'>X.com</a>
"""
st.markdown(footer_content, unsafe_allow_html=True)  # Footer içeriği