import streamlit as st

#ücretlendirme sayfası
def show():
    # İki sütunlu yapı oluşturuluyor.
    col1, col2 = st.columns([3,5])

    # Sol tarafta sözde resim (bir kutu veya metin) olacak.
    with col1:
        st.image("images/undraw_bitcoin_p2p_re_1xqa.svg")

    # Sağ tarafta başlıklar yer alacak.
    with col2:
            st.markdown(
                """
                # Tamamen Ücretsiz ve Sınırsız Erişim!
                * Proje Yönetim Sistemi'ni (PYS) kullanmak için herhangi bir ücret ödemenize gerek yok.
                * Bilim ve Sanat Merkezlerinde aktif öğrenci olmanız yeterlidir.
                * Tüm özelliklere sınırsız erişim imkanı sunarak, ekiplerinizle kolayca iş birliği yapabilirsiniz.
                * Ücretsiz planımızda kullanıcı sınırı yok, tüm takım arkadaşlarınızı davet edin.
                * Gizli ücretler veya abonelikler olmadan, projenize odaklanın.
                * Proje takibi, görev yönetimi ve ekip iletişimi; hepsi ücretsiz.
                """, 
                unsafe_allow_html=True
            )