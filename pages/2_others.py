import streamlit as st

st.session_state

def clean_photos():
    st.session_state.photos.clear()
    st.session_state.photo = None

st.button('clean', on_click=clean_photos)