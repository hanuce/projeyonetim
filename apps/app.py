import streamlit as st



def show_apps():

    App1 = st.Page("apps/pages/app1.py", title="App1")
    App2 = st.Page("apps/pages/app2.py", title="App2")
    App3 = st.Page("apps/pages/app3.py", title="App3")
    App4 = st.Page("apps/pages/app4.py", title="App4")
    App5 = st.Page("apps/pages/app5.py", title="App5")


    # Sidebar ile sayfaları tanıt
    pg = st.navigation(
        {
            "Öğrenci Menüsü": [App1,App2],
            "Öğretmen Menüsü": [App3,],
            "Kurum Menüsü": [App4, App5],
        }
    )
    pg.run()
    
