#--------------------------------------------------------------------------

# Voice Based Concept Understanding Analyser  


# Developed by:-

# 1. Vadlpatla Tejaswini
# 2. Jaya Mounika
# 3. Shanthi 
# 4. Nandhitha


#This project is developed as a part of SkillDizire Internship 2026  Generative Ai 
#--------------------------------------------------------------------------


import streamlit as st
import sqlite3
import tempfile
import os
import re
import io
import html
import whisper

from google import genai
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Voice Based Concept Understanding Analyser",
    page_icon="🎙️",
    layout="wide"
)

# ==========================================
# GEMINI API
# ==========================================
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# ==========================================
# LOAD WHISPER MODEL (LOADS ONLY ONCE)
# ==========================================
@st.cache_resource
def load_model():
    return whisper.load_model("base")

whisper_model = load_model()

# ==========================================
# DATABASE
# ==========================================
conn = sqlite3.connect(
    "results.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results(
id INTEGER PRIMARY KEY AUTOINCREMENT,
transcript TEXT,
feedback TEXT,
similarity TEXT,
score TEXT,
grade TEXT
)
""")

conn.commit()

# ==========================================
# SESSION STATE
# ==========================================
if "audio" not in st.session_state:
    st.session_state.audio = None

if "audio_name" not in st.session_state:
    st.session_state.audio_name = ""

if "reference_answer" not in st.session_state:
    st.session_state.reference_answer = ""

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "result" not in st.session_state:
    st.session_state.result = None

# ==========================================
# PDF FUNCTION
# ==========================================
def generate_pdf(result):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>VOICE BASED CONCEPT UNDERSTANDING ANALYSER</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Score:</b> {result['score']}/100",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Similarity:</b> {result['similarity']}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Grade:</b> {result['grade']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph("<br/><b>Transcript</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            html.escape(result["transcript"]),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph("<br/><b>AI Feedback</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            html.escape(result["feedback"]),
            styles["BodyText"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return buffer.getvalue()

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e293b);
}

section[data-testid="stSidebar"]{
background:#111827;
}

h1{
color:#ff1493 !important;
text-align:center;
font-weight:bold;
}

h2{
color:#ff4da6 !important;
}

h3{
color:#ff69b4 !important;
}

p,label,li{
color:white !important;
font-size:18px;
}

.stButton>button{
width:100%;
background:#ff1493;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
}

.stButton>button:hover{
background:#ff69b4;
}

div[data-testid="metric-container"]{
background:rgba(255,192,203,.15);
border-radius:12px;
padding:10px;
}

</style>
""", unsafe_allow_html=True)
# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.title("🎙 Navigation")

page = st.sidebar.radio(
    "Choose Page",
    [
        "🏠 Home",
        "🎤 Upload Audio",
        "🧠 AI Analysis",
        "📊 Dashboard",
        "📄 Report",
        
    ]
)

# ==========================================
# HOME PAGE
# ==========================================
if page == "🏠 Home":

    st.title("🎙 Voice Based Concept Understanding Analyser")

    st.markdown("""
## 🌸 Welcome

Welcome to the **Voice Based Concept Understanding Analyser**.

This application uses **Artificial Intelligence** to evaluate a student's conceptual understanding by analyzing voice recordings.

---

## ✨ Features

- 🎤 Upload Student Audio
- 📝 Speech-to-Text using Whisper AI
- 🤖 AI-based Answer Evaluation
- 📈 Similarity Analysis
- 📊 Automatic Score Generation
- 🏆 Grade Prediction
- 📄 Download PDF Report
- 📚 Student Analysis History

---

## 🚀 How to Use

1️⃣ Upload the student's audio.

2️⃣ Enter the expected answer.

3️⃣ Click **AI Analysis**.

4️⃣ View transcript, score, similarity, and grade.

5️⃣ Download the AI-generated PDF report.

---

### ❤️ Technologies Used

- Python
- Streamlit
- Whisper AI
- Google Gemini AI
- SQLite
- ReportLab
""")

# ==========================================
# UPLOAD AUDIO PAGE
# ==========================================
elif page == "🎤 Upload Audio":

    st.title("🎤 Upload Student Audio")

    uploaded_audio = st.file_uploader(
        "Choose Audio File",
        type=["mp3", "wav", "m4a"]
    )

    expected_answer = st.text_area(
        "Enter Expected Answer",
        value=st.session_state.reference_answer,
        height=220,
        placeholder="Enter the correct answer expected from the student..."
    )

    if uploaded_audio is not None:
        st.audio(uploaded_audio)

        st.success(f"✅ Uploaded: {uploaded_audio.name}")

    if st.button("💾 Save Input"):

        if uploaded_audio is None:
            st.warning("Please upload an audio file.")
            st.stop()

        if expected_answer.strip() == "":
            st.warning("Please enter the expected answer.")
            st.stop()

        st.session_state.audio = uploaded_audio.getvalue()
        st.session_state.audio_name = uploaded_audio.name
        st.session_state.reference_answer = expected_answer

        st.success("✅ Audio and Expected Answer saved successfully.")

# ==========================================
# PLACEHOLDER PAGES
# ==========================================
# ==========================================
# AI ANALYSIS (Speech-to-Text)
# ==========================================
# ==========================
# AI ANALYSIS
# ==========================
elif page == "🧠 AI Analysis":

    st.title("🧠 AI Analysis")

    if st.session_state.audio is None:
        st.warning("⚠️ Please upload an audio file first.")
        st.stop()

    if st.session_state.reference_answer.strip() == "":
        st.warning("⚠️ Please enter the expected answer first.")
        st.stop()

    if st.button("▶ Start AI Analysis"):

        extension = os.path.splitext(st.session_state.audio_name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as tmp:
            tmp.write(st.session_state.audio)
            audio_path = tmp.name

        try:

            # -------------------------------
            # Whisper Speech to Text
            # -------------------------------
            with st.spinner("🎤 Converting Speech to Text..."):
                result = whisper_model.transcribe(audio_path, fp16=False)

            transcript = result["text"]

            st.session_state.transcript = transcript

            st.success("✅ Transcription Completed")

            st.subheader("📄 Transcript")
            st.write(transcript)

            # -------------------------------
            # Gemini Prompt
            # -------------------------------
            prompt = f"""
You are an expert teacher.

Compare the student's answer with the expected answer.

Return ONLY in this format:

Similarity: <number>%
Score: <number>/100
Grade: <A+ / A / B / C / D>

Strengths:
- Point 1
- Point 2

Weaknesses:
- Point 1
- Point 2

Suggestions:
- Point 1
- Point 2

Expected Answer:
{st.session_state.reference_answer}

Student Answer:
{transcript}
"""

            # -------------------------------
            # Gemini AI
            # -------------------------------
            with st.spinner("🤖 Evaluating using Gemini..."):

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

            ai_text = response.text

            st.subheader("🤖 AI Feedback")
            st.write(ai_text)

            # -------------------------------
            # Extract Results
            # -------------------------------
            similarity_match = re.search(r"Similarity:\s*(\d+)", ai_text)
            score_match = re.search(r"Score:\s*(\d+)", ai_text)
            grade_match = re.search(r"Grade:\s*([A-D]\+?)", ai_text)

            similarity = similarity_match.group(1) if similarity_match else "0"
            score = score_match.group(1) if score_match else "0"
            grade = grade_match.group(1) if grade_match else "N/A"

            # -------------------------------
            # Save Session
            # -------------------------------
            st.session_state.result = {
                "transcript": transcript,
                "feedback": ai_text,
                "similarity": similarity,
                "score": score,
                "grade": grade
            }

            # -------------------------------
            # Save Database
            # -------------------------------
            cursor.execute("""
            INSERT INTO results
            (transcript, feedback, similarity, score, grade)
            VALUES (?, ?, ?, ?, ?)
            """, (
                transcript,
                ai_text,
                similarity,
                score,
                grade
            ))

            conn.commit()

            # -------------------------------
            # Show Metrics
            # -------------------------------
            st.success("✅ Analysis Completed Successfully!")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Score", f"{score}/100")

            with col2:
                st.metric("Similarity", f"{similarity}%")

            with col3:
                st.metric("Grade", grade)

        except Exception as e:
            st.error(f"Error: {e}")

        finally:
            if os.path.exists(audio_path):
                os.remove(audio_path)
# ==========================================
# DASHBOARD
# ==========================================
elif page == "📊 Dashboard":

    st.title("📊 Student Performance Dashboard")

    if st.session_state.result is None:
        st.warning("⚠️ Please complete AI Analysis first.")
        st.stop()

    result = st.session_state.result

    st.subheader("📊 Performance Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="📊 Score",
            value=f"{result['score']}/100"
        )

    with col2:
        st.metric(
            label="📈 Similarity",
            value=f"{result['similarity']}%"
        )

    with col3:
        st.metric(
            label="🏆 Grade",
            value=result["grade"]
        )

    st.divider()

    st.subheader("📄 Student Transcript")

    st.write(result["transcript"])

    st.divider()

    st.subheader("🤖 AI Feedback")

    st.write(result["feedback"])

    st.divider()

    st.success("✅ Student evaluation completed successfully.")
# ==========================================
# REPORT
# ==========================================
elif page == "📄 Report":

    st.title("📄 AI Analysis Report")

    if st.session_state.result is None:
        st.warning("⚠️ Please complete AI Analysis first.")
        st.stop()

    result = st.session_state.result

    st.subheader("📋 Report Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📊 Score", f"{result['score']}/100")

    with col2:
        st.metric("📈 Similarity", f"{result['similarity']}%")

    with col3:
        st.metric("🏆 Grade", result["grade"])

    st.divider()

    st.subheader("📄 Transcript")
    st.write(result["transcript"])

    st.divider()

    st.subheader("🤖 AI Feedback")
    st.write(result["feedback"])

    st.divider()

    pdf = generate_pdf(result)

    st.download_button(
        label="📥 Download PDF Report",
        data=pdf,
        file_name="AI_Report.pdf",
        mime="application/pdf"
    )

    st.success("✅ PDF Report is ready for download.")
