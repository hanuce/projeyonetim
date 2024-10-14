import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Proje Yönetim",
    page_icon=":flag-tr:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CSS kodu
with open("styles/custom.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

   
ustmenu = option_menu(None, ["Projemiz Hakkında", "Ekibimiz", "Ücretlendirme", 'İletişim', 'Giriş Yap'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        orientation="horizontal")


