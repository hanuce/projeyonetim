import streamlit as st

st.title("App 1")
st.write("Bu, App 1'in içeriğidir.")
st.write(st.session_state.user_email)
st.write(st.session_state.user_password)
