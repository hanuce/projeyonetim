import streamlit as st

#ekibimiz sayfası
def show():
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