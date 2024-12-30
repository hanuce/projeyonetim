import streamlit as st
#pys sayfası
def show():
    # İki sütunlu yapı oluşturuluyor.
    col1, col2 = st.columns([3,4], border=True)

    # Sol tarafta sözde resim (bir kutu veya metin) olacak.
    with col1:
        st.image("images/undraw_scrum_board_re_wk7v.svg", use_container_width=True)

    # Sağ tarafta başlıklar yer alacak.
    with col2:
            st.markdown(
                """
                # Proje Yönetim Sistemi: PYS
                "Proje Yönetimi" projelerin başarısı için en önemli değişkendir. Proje fikirlerinin doğru yönetimsel süreçle başarıya ulaşan bir "Proje" olması için PYS size destek olur.
                * Projelerinize güç katın, ekibinizle hedeflerinize ulaşın.
                * Takımınızla uyum içinde çalışın, her aşamada tam kontrol sağlayın.
                * PYS ile projelerinizi organize edin, verimliliğinizi artırın.
                * Her yerden, her zaman projelerinizi kolayca yönetin.
                * İletişimi güçlendirin, ekip ruhunu her zaman canlı tutun.
                * Karmaşık süreçleri kolaylaştırın, projelerinize odaklanın.
                * Başarıya giden yolda hep bir adım önde olun.
                * Başarıya giden yolda, her adımda yanınızdayız. Çevik yönetim, güçlü sonuçlar.
                """, 
                unsafe_allow_html=True
            )