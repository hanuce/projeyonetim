import streamlit as st

# iletişim sayfası
def show():
    # İki sütunlu yapı oluşturuluyor.
    col1, col2 = st.columns([5,3])

    # Sol sütun: Google Maps Embed
    with col1:
        st.markdown(
            """
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3009.9432331104745!2d29.03078577575533!3d41.02649787134798!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14cab77d5cbf18c7%3A0x3ddd6a52176b0245!2sAhmet%20Y%C3%BCksel%20%C3%96zemre%20Bilim%20ve%20Sanat%20Merkezi!5e0!3m2!1str!2str!4v1728899578921!5m2!1str!2str" 
                width="100%" 
                height="450" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy">
            </iframe>
            """,
            unsafe_allow_html=True
        )

    # Sağ sütun: İletişim Bilgileri
    with col2:
        st.markdown("## İletişim Bilgilerimiz")
        st.write("📍 **Adres:**")
        st.write("Selamı Ali Mah. Cumhuriyet Cad. No:60/1")
        st.write("Üsküdar, İstanbul, Türkiye")
        st.write("")
        st.write("✉️ **E-posta:**")
        st.write("info@----.com")
        st.write("")
        st.write("🕒 **Çalışma Saatleri:**")
        st.write("Hafta içi: ?? - ??")