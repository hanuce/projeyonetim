import streamlit as st

#neden? hakkında sayfası
def show():
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