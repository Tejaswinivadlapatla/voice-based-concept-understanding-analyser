import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io


def display_results(results):
    st.subheader("Transcript")
    st.write(results.get("transcript", "No transcript available"))

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Similarity Score", f"{results.get('similarity_score', 0)}%")
    with col2:
        st.metric("Audio Score", f"{results.get('audio_score', 0)}%")

    st.subheader("Feedback")
    st.info(results.get("feedback", "No feedback available"))


def generate_pdf_report(results):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("VBCUA Evaluation Report", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Transcript", styles["Heading2"]))
    story.append(Paragraph(results.get("transcript", "N/A"), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Scores", styles["Heading2"]))
    story.append(Paragraph(f"Similarity Score: {results.get('similarity_score', 0)}%", styles["Normal"]))
    story.append(Paragraph(f"Audio Score: {results.get('audio_score', 0)}%", styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Feedback", styles["Heading2"]))
    story.append(Paragraph(results.get("feedback", "N/A"), styles["Normal"]))

    doc.build(story)
    buffer.seek(0)
    return buffer