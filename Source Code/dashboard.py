import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Analysis Dashboard")

if "uploaded_audio" not in st.session_state:
    st.warning("Please upload an audio file on the Upload page first.")
else:
    st.write(f"Analyzing explanation of: **{st.session_state.get('concept', 'N/A')}**")

    audio_samples = np.sin(np.linspace(0, 50, 1000)) * np.random.uniform(0.5, 1, 1000)
    fig, ax = plt.subplots(figsize=(10, 2.5))
    ax.plot(audio_samples, color="#4A4AFF", linewidth=0.8)
    ax.set_title("Audio Waveform")
    ax.set_facecolor("#f9f9fb")
    st.pyplot(fig)

    similarity_score = 82
    audio_score = 75

    st.write("Similarity Score")
    st.progress(similarity_score / 100)
    st.write(f"{similarity_score}%")

    st.write("Audio Score")
    st.progress(audio_score / 100)
    st.write(f"{audio_score}%")