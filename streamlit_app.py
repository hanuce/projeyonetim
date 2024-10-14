import streamlit as st
from streamlit_option_menu import option_menu
import sayfalar as sayfa
import subprocess


st.set_page_config(
    page_title="Proje Yönetim",
    page_icon=":flag-tr:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CSS dosyasını yüklemek
with open("styles/custom.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# index.py'ı çalıştır
subprocess.run(['streamlit', 'run', 'entrance/index.py'])

