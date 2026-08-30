import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from report import display_results, generate_pdf_report

st.title("📄 Results & Report")

if "uploaded_audio" not in st.session_state:
    st.warning("Please upload an audio file on the Upload page first.")
else:
    sample_results = {
        "transcript": "Machine learning is a method where systems learn patterns from data instead of following fixed rules.",
        "similarity_score": 82,
        "audio_score": 75,
        "feedback": "Clear explanation of the core concept, with minor hesitation patterns."
    }

    display_results(sample_results)
    
    pdf_buffer = generate_pdf_report(sample_results)
    st.download_button(
        label="📥 Download PDF Report",
        data=pdf_buffer,
        file_name="vbcua_report.pdf",
        mime="application/pdf"
    )
