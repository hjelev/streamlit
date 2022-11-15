import streamlit as st
from PIL import Image
import glob



st.set_page_config(page_title="Home", page_icon="📈")
st.header(f"You have taken {len(st.session_state.photos)} photos")
if st.session_state.photo != None:
    for photo in st.session_state.photos:
        st.image(photo)
        st.write(photo)
        btn = st.download_button(
                label="Download image",
                data=photo,
                file_name="camera-photo.jpeg",
                mime="image/jpeg"
            )