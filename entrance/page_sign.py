import streamlit as st
import sqlite3
import re

# Giriş yap sayfası
def show():
        # Ortalamak için 3 sütun oluşturuyoruz, orta sütun aktif kullanılıyor.
    col1, col2, col3 = st.columns([1, 2, 1])
    # SQLite veritabanına bağlanma
    conn = sqlite3.connect('databases/database.db')
    cursor = conn.cursor()
    
    with col2:
        # Giriş ve Üye Ol sütunu tabs ile oluşturuyoruz
        tabs = st.tabs(["Giriş Yap", "Üye Ol", "Kurum Kaydı"])

        # Giriş Yap sekmesi
        with tabs[0]:
            # Kullanıcı adı ve şifre giriş alanları
            user_email = st.text_input("Kullanıcı E-Posta:", key="username")
            user_password = st.text_input("Şifre:", type="password", key="password")
            if st.button("Giriş Yap"):
                st.success("Giriş başarılı!")
                user_email = "1@meb.k12.tr"
                st.session_state.user_email = user_email
                st.session_state.is_logged_in = True
                st.rerun()
            st.info("Şifrenizi unuttuysanız sıfırlamak için lütfen kayıtlı olduğunuz BİLSEM'e başvurun.")
            

        # Üye Ol sekmesi
        with tabs[1]:
            st.info("Kayıt işleminden sonra bilgileriniz seçtiğiniz BİLSEM'e onaya gönderilecektir. Bu sebeple doğru BİLSEM'i seçmeniz önemlidir. "
            "Onaylanmak ve sistemi kullanmak için kurumunuza başvurunuz. "
            "Eğer yanlış BİLSEM üzerinden kayıt oluşturduysanız düzelttirmek için yine kurumunuza başvurunuz. "
            "Tüm alanlar zorunludur.")
            # Veritabanından bilsemleri getiriyoruz.
            cursor.execute("SELECT institute_name FROM institutes")
            institutes_details = [row[0] for row in cursor.fetchall()]
            institutes_details = sorted(institutes_details)
            user_institute = st.selectbox("Kayıtlı olduğunuz BİLSEM'i seçiniz. (Aramak için yazmaya başlayınız.)", institutes_details)

            col_type, col_gender = st.columns([1,1])
            with col_type:
                user_type = st.radio("", ["Öğrenci", "Öğretmen"], index=0, horizontal=True)
            with col_gender:
                gender = st.radio("", ["Kadın", "Erkek"], index=0, horizontal=True)

            col_branch_or_level, col_user_institute_id = st.columns([1,1])

            with col_branch_or_level:

                # Veritabanından öğrenciler ve öğretmenler için seçenekleri getiriyoruz.
                if user_type == "Öğrenci":
                    cursor.execute(f"SELECT user_role_detail FROM user_roles WHERE user_type = ?",(2,))
                    user_details = [row[0] for row in cursor.fetchall()]
                    user_role_detail = st.selectbox("Sınıf", user_details)
                else:
                    cursor.execute(f"SELECT user_role_detail FROM user_roles WHERE user_type = ?",(3,))
                    user_details = [row[0] for row in cursor.fetchall()]
                    user_role_detail = st.selectbox("Branş (Aramak için yazmaya başlayınız.)", user_details)

            with col_user_institute_id:
                user_institute_id = st.text_input("BİLSEM NO", 0, disabled=(user_type == "Öğretmen"))
                if user_type == "Öğretmen": user_institute_id = "8100"
                
                
            col_user_name, col_user_last_name = st.columns([1,1])

            with col_user_name:
                user_name = st.text_input("İsim", placeholder="İsim")

            with col_user_last_name:
                user_last_name = st.text_input("Soyisim", placeholder="Soyisim")
            
            # Yazılan eposta adresi görünüm olarak bir epostaya benziyor mu? RegEx.
            def is_valid_email(user_email):
                # E-posta için regex deseni
                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                return re.match(pattern, user_email) is not None

            user_email = st.text_input("E-Posta", placeholder="user@example.com")

            # Yazılan şifre 6 karakter, özel karakter ve Upper_Lower Case karşılıyor mu? RegEx.
            def is_valid_password(user_password):
                # Şifrenin en az 6 karakter olup olmadığını kontrol et
                if len(user_password) < 6:
                    return False
                # Büyük harf, küçük harf, rakam ve özel karakter kontrolü
                pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.,;!+\-*:%()=?_]).+$'
                return re.match(pattern, user_password) is not None

            user_password = st.text_input("Şifre", type="password", placeholder="En az 6 karakter, büyük-küçük harf, rakam ve özel karakter içermeli")

            # Üye Ol butonu
            if st.button("Üye Ol"):
                routing = 1
                if not user_institute: st.warning("Geçersiz Kurum. Lütfen listeden seçiniz.")
                elif not user_role_detail: st.warning("Geçersiz Branş veya Sınıf bilgisi. Lütfen listeden seçiniz.")
                elif not user_institute_id.isnumeric() or user_institute_id == "0": st.warning("Geçersiz BİLSEM No girdiniz.")
                elif not user_name: st.warning("İsim giriniz.")
                elif not user_last_name: st.warning("Soyisim giriniz")
                elif not is_valid_email(user_email):
                    st.warning("Geçersiz e-posta formatı. Lütfen geçerli bir e-posta adresi girin.")
                elif not is_valid_password: st.warning("Şifre kurallara uymuyor: En az 6 Karakter, büyük-küçük harf, özel karakter ve rakam içermeli.")
                elif not user_password: st.warning("Şifre Giriniz")
                elif not is_valid_password(user_password): st.warning("Kurallara uygun şifre giriniz. En az 6 karakter, En az 1'er tane büyük-küçük harf, rakam ve özel karakter (.,;!+\-*:%()=?_) içermelidir.")
                else:
                    cursor.execute("SELECT user_email FROM user_basics WHERE user_email = ?", (user_email,))
                    email_exists = cursor.fetchone()
                    if email_exists:
                        st.warning(f"Bu e-posta adresi zaten kayıtlı: {user_email}")
                    else:
                        conn.close()
                        #sign_control.login(user_name = user_name, )
                        st.success("Kayıt başarılı! Sistemi kullanmaya başlamak için lütfen kayıtlı olduğunuz BİLSEM'den başvurunuzu onaylatın.")
        # Kurum kaydı sekmesi
        with tabs[2]:
            st.info("Tüm kurumlar sisteme kayıtlıdır.")
            st.info("Kullanıcı adınız okula ait meb.k12.tr e-posta (kurumkodu@meb.k12.tr) adresinizdir.")
            st.info("Şifrenizi almak için veya şifre sıfırlamak için meb.k12.tr e-postanızdan admin@pys.com'a e-posta yollayınız.")
            st.info("Yeni kurum kaydı için de aynı adrese meb.k12.tr e-postanızdan durumu açıklayan bir mail atınız.")