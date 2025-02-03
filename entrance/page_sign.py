#page_signin.py
import streamlit as st
from core.user_manager import UserManager
from core.session_manager import SessionManager
from core.static_manager import StaticManager
import time

# Kullanıcı, oturum ve statik yöneticisi örnekleri
user_manager = UserManager()
session_manager = SessionManager()
static_manager = StaticManager()

# Streamlit UI
def show():
    col1, col2, col3 = st.columns([3, 14, 3])
    with col1:
        st.empty()
    with col2:
        with st.container(border=True):
            tabs = st.tabs(["Giriş Yap", "Üye Ol", "Kurum Kaydı"])

            # Giriş Yap Sekmesi
            with tabs[0]:
                user_email = st.text_input("Kullanıcı E-Posta:", placeholder="E-Posta Adresinizi Giriniz")
                user_password = st.text_input("Şifre:", type="password", placeholder="Şifrenizi Giriniz")
                if st.button("Giriş Yap"):
                    if user_manager.verify_password(user_email, user_password):
                        st.success("Giriş başarılı!")
                        user_id = user_manager.get_user_by_email(user_email)["user_id"]
                        session_id = session_manager.create_session(user_id)
                        st.session_state.user_id = user_id
                        st.session_state.session_id = session_id
                        st.rerun()
                    else:
                        st.error("E-posta veya şifre yanlış. Lütfen tekrar deneyin.")

            # Üye Ol Sekmesi
            with tabs[1]:
                st.info("*Tüm alanlar zorunludur.")
                institutes = static_manager.get_institutes()
                institute_options = {title: id for id, title in institutes}  # {title: id}
                user_institute = st.selectbox(
                    "Kayıt olacağınız BİLSEM'i seçiniz. *",
                    options=list(institute_options.keys()),  # Show titles
                    placeholder="Aramak için yazmaya başlayınız",
                    index=None
                )

                col_type, col_gender, col_branch_level = st.columns([1, 1, 1])
                with col_type:
                    user_type = st.radio("Rolünüz *", ["Öğrenci", "Öğretmen / Yönetici / Danışman"], index=0, horizontal=True)

                with col_gender:
                    user_gender = st.radio("Cinsiyet *", ["Kadın", "Erkek"], index=0, horizontal=True)

                with col_branch_level:
                    if user_type == "Öğrenci":
                        student_levels = static_manager.get_student_levels()
                        level_options = {detail: id for id, detail in student_levels}  # {detail: id}
                        user_detail = st.selectbox(
                            "Sınıf *",
                            options=list(level_options.keys()),  # Show details
                            placeholder="Seçiniz",
                            index=None
                        )
                        user_detail_id = level_options.get(user_detail) if user_detail else None
                    else:
                        teacher_branches = static_manager.get_teacher_branches()
                        branch_options = {detail: id for id, detail in teacher_branches}  # {detail: id}
                        user_detail = st.selectbox(
                            "Branş *",
                            options=list(branch_options.keys()),  # Show details
                            placeholder="Aramak için yazmaya başlayınız",
                            index=None
                        )
                        user_detail_id = branch_options.get(user_detail) if user_detail else None

                col_user_name, col_user_last_name = st.columns([1, 1])
                with col_user_name:
                    user_name = st.text_input("İsim *", placeholder="İsim", max_chars=35)
                with col_user_last_name:
                    user_last_name = st.text_input("Soyisim *", placeholder="Soyisim", max_chars=35)

                user_email = st.text_input("E-Posta *", placeholder="e-posta@adres.com", max_chars=46)
                user_password = st.text_input("Şifre *", type="password", placeholder="Şifre", max_chars=16)
                st.info("Şifre en az 6 karakter uzunluğunda, 1 büyük harf, 1 küçük harf, 1 rakam ve 1 özel karakter içermeli")

                if st.button("Üye Ol"):
                    if not all([user_name, user_last_name, user_email, user_password, user_institute, user_detail]):
                        st.error("Lütfen tüm alanları doldurun.")
                    else:
                        user_data = {
                            "user_name": user_name,
                            "user_last_name": user_last_name,
                            "user_email": user_email,
                            "user_password": user_password,
                            "user_institute_id": institute_options[user_institute],  # Use institute ID
                            "user_main_role": 507 if user_type == "Öğrenci" else 506,  # 507 for student, 506 for teacher
                            "user_detail_id": user_detail_id,  # Use level_id or branch_id
                            "gender": 0 if user_gender == "Kadın" else 1, # 0 for male, 1 for female
                        }
                        if user_manager.register_user(user_data):
                            st.success("Kullanıcı kaydedildi! Giriş yapılıyor...")
                            user_id = user_manager.get_user_by_email(user_email)["user_id"]
                            session_id = session_manager.create_session(user_id)
                            st.session_state.user_id = user_id
                            st.session_state.session_id = session_id
                            time.sleep(0.5)
                            st.rerun()
                        else:
                            st.error("Kayıt sırasında bir hata oluştu. Lütfen tekrar deneyin.")

            # Kurum Kaydı Sekmesi
            with tabs[2]:
                st.info("Tüm kurumlar sisteme kayıtlıdır.")
                st.info("Kullanıcı adınız okula ait meb.k12.tr e-posta (kurumkodu@meb.k12.tr) adresinizdir.")
                st.info("Şifrenizi almak için veya şifre sıfırlamak için meb.k12.tr e-postanızdan admin@pys.com'a e-posta yollayınız.")
                st.info("Yeni kurum kaydı için admin@pys.com'a meb.k12.tr uzantılı e-postanızdan durumu açıklayan bir mail atınız.")
    with col3:
        st.empty()