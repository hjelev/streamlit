import streamlit as st
st.set_page_config(page_title="Plotting Demo", page_icon="📈")

if 'photos' not in st.session_state:
    st.session_state['photos'] = []

if 'photo' not in st.session_state:
    st.session_state['photo'] = ''

photos = []

photo = st.camera_input("Take a Photo")
    
if photo:
    st.session_state.photo = photo
    photos = st.session_state.photos
    photos.append(photo)
    st.session_state.photos = photos
    photo = None


# if st.session_state.photo != None:
#     st.write(st.session_state.photo)
#     st.image(st.session_state.photo)
