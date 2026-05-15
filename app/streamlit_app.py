import streamlit as st

st.title("PriceVision AI")

video = st.file_uploader("Upload video")

if video:
    st.success("Видео загружено")