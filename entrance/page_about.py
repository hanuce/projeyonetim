import streamlit as st

# Neden? hakkında sayfası
def show():
    # İki sütunlu yapı oluşturuluyor.
    col1_1, col1_2, = st.columns([3,5], border=True)

    with col1_1:
        st.image("images/undraw_powerful_re_frhr.svg", use_container_width=True)
    with col1_2:
        st.markdown("""
            ### Yetenek Yönetimi
            PYS sayesinde, kendi ilgi alanlarına ve yetkinliklerine uygun proje gruplarına katılabilir veya projelerinize katkı sağlayacak doğru ekip yetenekteki kişileri bulabilirsiniz.
            Amaçlar: 
            - **Ekip Oluşumunu Optimize Etmek:** Katılımcıların ilgi alanlarına ve yetkinliklerine göre doğru proje gruplarına yönlendirilmesini sağlayarak, her bireyin güçlü yönlerinden en iyi şekilde yararlanmak.
            - **Bireysel ve Ekip Verimliliğini Arttırmak:** Ekip üyelerinin yeteneklerine uygun görevler vererek, kişisel ve ekip performansını artırmak.
            - **Projelerde Başarıyı Sağlamak:** Her proje için doğru yeteneklerin bir araya getirilmesiyle, projelerin başarısını artırmak ve zorluklara hızlı çözümler üretmek.
            """)
    # İki sütunlu yapı oluşturuluyor.
    col2_1, col2_2, = st.columns([5,3], border=True)

    # Her bir sütun için içerik ekleniyor.
    with col2_1:
        st.markdown("""
            ### Proje Yönetimi
            Proje yönetiminin temeli, belirlenen hedeflere ulaşmak için tüm adımların takip edilmesi ve gerekli düzeltmelerin zamanında yapılmasıdır. İş yükünün dengeli bir şekilde dağılması ve her ekip üyesinin görevine odaklanması kritik öneme sahiptir. 
            Amaçlar:
            - **Proje Aşamalarının Düzenli Takibi:** Projenin her aşamasını dikkatlice planlamak, görevleri mantıklı bir şekilde bölüştürmek ve her adımda ilerlemeyi izleyerek hedeflere ulaşmak.
            - **Zaman ve Kaynak Yönetimini İyileştirmek:** Proje sürecinde zaman ve kaynakları verimli bir şekilde kullanarak, belirlenen zaman diliminde projeyi tamamlamak.
            - **Ekip İletişimini Güçlendirmek:** Proje yönetimi sırasında, ekip üyeleri arasında etkin iletişimi teşvik ederek, her bireyin görevine odaklanmasını sağlamak ve işbirliği içerisinde başarıya ulaşmak.
            """)
    with col2_2:
        st.image("images/undraw_data_points_re_vkpq.svg", use_container_width=True)

            