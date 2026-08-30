import streamlit as st

st.title("📤 Upload Your Audio")

concept = st.selectbox(
    "Select a concept to explain",
    ["Machine Learning", "Cloud Computing", "Neural Networks"]
)

uploaded_audio = st.file_uploader(
    "Upload an audio file (WAV, MP3, M4A)",
    type=["wav", "mp3", "m4a"]
)

if uploaded_audio is not None:
    st.session_state["uploaded_audio"] = uploaded_audio
    st.session_state["concept"] = concept
    st.success(f"File uploaded: {uploaded_audio.name}")
    st.audio(uploaded_audio)
else:
    st.info("Please upload an audio file to begin analysis.")