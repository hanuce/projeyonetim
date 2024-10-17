import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3

#pys sayfası
def show_pys():
    # İki sütunlu yapı oluşturuluyor.
    col1, col2 = st.columns([3,4])

    # Sol tarafta sözde resim (bir kutu veya metin) olacak.
    with col1:
        st.image("images/undraw_scrum_board_re_wk7v.svg")

    # Sağ tarafta başlıklar yer alacak.
    with col2:
            st.markdown(
                """
                # Proje Yönetim Sistemi: PYS
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

#neden? hakkında sayfası
def show_neden():
    # Üç sütunlu yapı oluşturuluyor.
    col1, col2, col3 = st.columns(3)

    # Her bir sütun için içerik ekleniyor.
    with col1:
        st.markdown(
            """
            # Neden PYS ?
            "Proje Yönetimi" projelerin başarısı için en önemli değişkendir. Proje fikirlerinin doğru yönetimsel süreçle başarıya ulaşan bir "Proje" olması için PYS size destek olur.
            """
        )
        st.image(
            "images/undraw_success_factors_re_ce93.svg",
            use_column_width=True
        )
        

    with col2:
        st.markdown(
            """
            # Projene Yetnek Bul veya Yeteneğini Paylaş!
            Proje gruplarına katılmak, fikirlerini proje haline getirmek, projen için tam da ihtiyacın olan ekip arkadaşını bulmak için en iyi araç.
            """
        )
        st.image(
            "images/undraw_powerful_re_frhr.svg",
            use_column_width=True
        )

    with col3:
        st.markdown(
            """
            # Projeni Etkili Yönet
            Proje sürecinde iş ve adımları böl, planla, takip et, zamanını yönet ve başarıya ulaş.Uygulamalı Bilimler, Doğa Bilimleri, Sosyal Bilimler için uygun...
            """
        )
        st.image(
            "images/undraw_data_points_re_vkpq.svg",
            use_column_width=True
        )

#ekibimiz sayfası
def show_ekip():
    # İki sütunlu yapı oluşturuluyor.
    col1, col2 = st.columns([2,5])

    # Sol tarafta sözde resim (bir kutu veya metin) olacak.
    with col1:
        st.image("images/undraw_team_page_re_cffb.svg")

    # Sağ tarafta başlıklar yer alacak.
    with col2:
            st.markdown(
                """
                ## Üsküdar Ahmet Yüksel Özemre Bilim ve Sanat Merkezi
                ### Danışman
                * H.N.Cetinkaya
                ### Proje Öğrencileri
                * A.C.Karsli
                * _B.Kuskonmaz_ (former)
                * _I.Soysal_ (former)
                * _I.T.Karadag_ (former)
                * _S.Arslan_ (former)
                """, 
                unsafe_allow_html=True
            )

#ücretlendirme sayfası
def show_ucret():
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

# iletişim sayfası
def show_iletisim():
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

# Giriş yap sayfası
def show_girisyap():
        # Ortalamak için 3 sütun oluşturuyoruz, orta sütun aktif kullanılıyor.
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Giriş ve Üye Ol sütunu tabs ile oluşturuyoruz
        tabs = st.tabs(["Giriş Yap", "Üye Ol"])

        # Giriş Yap sekmesi
        with tabs[0]:
            # Kullanıcı adı ve şifre giriş alanları
            st.text_input("Kullanıcı E-Posta:", key="username")
            st.text_input("Şifre:", type="password", key="password")
            if st.button("Giriş Yap"):
                st.success("Giriş başarılı!")
            st.info("Şifrenizi unuttuysanız sıfırlamak için lütfen kayıtlı olduğunuz BİLSEM'e başvurun.")
            

        # Üye Ol sekmesi
        with tabs[1]:
            st.info("Kayıt işleminden sonra bilgileriniz kurumunuza sistem üzerinden onaylanmak üzere düşecektir. "
            "Onaylanmak ve sistemi kullanmak için kurumunuza başvurunuz.")
            bilsem = st.selectbox("Kayıtlı olduğunuz BİLSEM'i seçiniz. (Aramak için yazmaya başlayınız.)", ["BİLSEM A", "BİLSEM B", "BİLSEM C"])
            col_type, col_gender = st.columns([1,1])
            with col_type:
                user_type = st.radio("", ["Öğrenci", "Öğretmen"], index=0)
            with col_gender:
                gender = st.radio("", ["Kadın", "Erkek"], index=0)

            col_branch_or_level, col_bilsem_no = st.columns([1,1])
            with col_branch_or_level:
                if user_type == "Öğrenci":
                    class_grade = st.selectbox("Sınıf", ["9. Sınıf", "10. Sınıf", "11. Sınıf", "12. Sınıf"])
                else:
                    branch = st.selectbox("Branş (Aramak için yazmaya başlayınız.)", ["Matematik", "Fizik", "Biyoloji", "Türk Dili ve Edebiyatı"])
            with col_bilsem_no:
                bilsem_no = st.text_input("BİLSEM NO", disabled=(user_type == "Öğretmen"))
            
            col_name, col_last_name = st.columns([1,1])
            with col_name:
                name = st.text_input("İsim")
            with col_last_name:
                last_name = st.text_input("Soyisim")
            
            email = st.text_input("E-posta")
            password = st.text_input("Şifre", type="password")

            # Üye Ol butonu
            if st.button("Üye Ol"):
                st.success("Kayıt başarılı! Sistemi kullanmaya başlamak için lütfen kayıtlı olduğunuz BİLSEM'den başvurunuzu onaylatın.")
