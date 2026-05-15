import streamlit as st
import os
import pandas as pd

from pipeline.video_reader import extract_frames

st.title("PriceVision AI")

video = st.file_uploader(
    "Upload robot video",
    type=["mp4", "avi", "mov"]
)

if video is not None:

    os.makedirs("data/videos", exist_ok=True)

    video_path = os.path.join("data/videos", video.name)

    with open(video_path, "wb") as f:
        f.write(video.read())

    st.success(f"Видео сохранено: {video.name}")

    st.video(video_path)

    if st.button("Извлечь кадры"):
        with st.spinner("Извлекаем кадры из видео..."):
            frames = extract_frames(video_path, step_seconds=2)

        st.success(f"Извлечено кадров: {len(frames)}")

        df = pd.DataFrame(frames)
        st.dataframe(df)

        if len(frames) > 0:
            st.image(frames[0]["frame_path"], caption="Первый извлечённый кадр")