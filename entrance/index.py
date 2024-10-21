import streamlit as st
import entrance.page_pys as pys
import entrance.page_about as about
import entrance.page_team as team
import entrance.page_pricing as pricing
import entrance.page_contact as contact
import entrance.page_sign as sign


def show_page(page):
    if page == "PYS": pys.show()
    elif page == "Neden?": about.show()
    elif page == "Ekibimiz": team.show()
    elif page == "Ücretlendirme": pricing.show()
    elif page == "İletişim": contact.show()
    elif page == "Giriş Yap": sign.show()