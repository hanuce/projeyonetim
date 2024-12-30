import streamlit as st
from streamlit_extras.button_selector import button_selector
import entrance  # entrance klasöründen fonksiyonları çekeceğiz

st.set_page_config(
    page_title="Proje Yönetim",
    page_icon=":flag-tr:",
    layout="wide",
    initial_sidebar_state="auto",
)

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

# Menü öğeleri ve ilgili fonksiyonlar
menu_items = {
    "__PYS__": entrance.pys.show,
    "__Amaçlar__": entrance.about.show,
    "__Ekibimiz__": entrance.team.show,
    "__Ücretlendirme__": entrance.pricing.show,
    "__İletişim__": entrance.contact.show,
    "__Giriş Yap__": entrance.sign.show,
}


# Kullanıcı girişi yapmayanlar için karşılama sayfası
def main_page():
    st.session_state.selected_item = list(menu_items.keys())[0]

    with st.container(border=True):

        # Logo ve menü sütunları
        col_logo, menu_cols = st.columns([1, len(menu_items)])

        with col_logo:
            st.image("images/logo.svg", width=40,)

        with menu_cols:
            selected_index = button_selector(
                list(menu_items.keys()),
                key="menu_selector",
                spec=6
            )
            st.session_state.selected_index = selected_index

    # İçerik gösterimi (doğrudan çağırım)
    with st.container():
        selected_menu = list(menu_items.keys())[st.session_state.selected_index]
        menu_items[selected_menu]()

# Kullanıcı login olduysa app_page fonksiyonu değilse main_page fonksiyonu çalıştır.
def app_page():
    import apps.app as app
    app.show_apps()

if st.session_state.is_logged_in:
    app_page()
else:
    main_page()

# Footer
st.markdown("---")  # Ayrım çizgisi
footer_content = """
© 2024. Görseller: <a href='https://undraw.co/illustrations'> undraw.co</a> | Özgün Hakları Saklıdır.
<a href='#'>Github</a> | <a href='#'>X.com</a>
"""
st.markdown(footer_content, unsafe_allow_html=True)  # Footer içeriği