# 🎙️ Voice-Based Concept Understanding Analyser

> **An AI-powered application that evaluates a user's conceptual understanding through spoken responses using Speech-to-Text, Semantic Analysis, and Audio Feature Extraction.**

---

## 📌 About the Project

The **Voice-Based Concept Understanding Analyser (VBCUA)** is an AI-powered web application developed to assess a user's understanding of concepts through voice input. The application converts speech into text, analyzes semantic similarity between the spoken response and the expected answer, evaluates speech characteristics, and generates an overall performance score along with personalized feedback.

This project is being developed as part of the **APSCHE Google Generative AI Cloud Program**.

---

## ✨ Key Features

- 🎤 Speech-to-Text Conversion
- 🧠 Semantic Understanding & Similarity Analysis
- 🎵 Audio Feature Extraction
- 📊 Intelligent Scoring System
- 📈 Interactive Streamlit Dashboard
- 📄 PDF Report Generation
- 💡 AI-Powered Personalized Feedback

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **Speech Recognition:** OpenAI Whisper
- **Semantic Analysis:** Sentence Transformers / Gemini API
- **Audio Processing:** Librosa
- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib
- **Report Generation:** ReportLab
- **Version Control:** Git & GitHub

---

## 📂 Repository Structure

```text
Voice-Based-Concept-Understanding-Analyser/
│
├── backend/
├── frontend/
├── utils/
├── tests/
├── docs/
├── data/
├── assets/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Project Workflow

```text
User Uploads Audio
        │
        ▼
Speech-to-Text Conversion
        │
        ▼
Semantic Understanding Analysis
        │
        ▼
Audio Feature Extraction
        │
        ▼
Performance Scoring
        │
        ▼
Feedback Generation
        │
        ▼
PDF Report Generation
```

---

## 👨‍💻 Team

| Name | Role |
|------|------|
| Amjuri Sai Chaturya | Team Leader |
| Jami Yuktasri | Member |
| Patnana Mahesh | Member |
| Vayalapalli Maneesha | Member |

---

## 📌 Current Status

🟢 **Project Initialization Completed**

- ✅ Repository Created
- ✅ Folder Structure Initialized
- ✅ Development in Progress

---

## 🚀 Future Enhancements

- Multi-language Speech Support
- Emotion & Sentiment Analysis
- Advanced AI Feedback
- Cloud Deployment
- Performance Analytics Dashboard

---

## 📜 Acknowledgement

This project is developed under the **APSCHE Google Generative AI Cloud Program** as part of a collaborative learning initiative in **Generative AI and Cloud Technologies**.

---

<div align="center">
---

## ⚙️ Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- FFmpeg installed and added to PATH (required by Whisper for audio decoding)
- Git

### Setup Steps

1. **Clone the repository**
```bash
   git clone https://github.com/saichaturya018/Voice-Based-Concept-Understanding-Analyser.git
   cd Voice-Based-Concept-Understanding-Analyser
```

2. **Create and activate a virtual environment**
```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
```

3. **Install FFmpeg** (required by Whisper)
```bash
   # Windows (using Chocolatey)
   choco install ffmpeg

   # macOS (using Homebrew)
   brew install ffmpeg

   # Linux (Debian/Ubuntu)
   sudo apt update && sudo apt install ffmpeg
```

4. **Install Python dependencies**
```bash
   pip install -r "5. Project Development Phase/requirements.txt"
```

5. **Download NLTK data (first run only)**
```bash
   python -m nltk.downloader punkt stopwords
```

6. **Run the application**
```bash
   streamlit run "5. Project Development Phase/app.py"
```

7. **Open in browser**
   The app will open automatically at `http://localhost:8501`.
   
## 🎯 Workflow

The application follows a simple and efficient workflow for evaluating a student's conceptual understanding:

1. Launch the Streamlit application.
2. Upload the student's audio response.
3. Enter the expected answer for comparison.
4. Convert the uploaded speech into text using **OpenAI Whisper**.
5. Analyze and evaluate the response using **Google Gemini AI**.
6. Generate the similarity percentage, score, and grade based on the evaluation.
7. Display detailed AI feedback, including strengths, weaknesses, and improvement suggestions.
8. Download a comprehensive PDF evaluation report.

---

## 📸 Application Screenshots

### 🏠 1. Home Page
The home page provides an overview of the project, its objectives, and the key features available in the application.

<img width="1773" height="946" alt="Screenshot 2026-07-06 211412" src="https://github.com/user-attachments/assets/31d2a3f4-fb8a-4713-ad61-4c0b98a00779" />

<img width="1745" height="896" alt="Screenshot 2026-07-06 211423" src="https://github.com/user-attachments/assets/226f413a-3de1-4bec-b00a-71fcaff5f6d2" />

---

### 🎤 2. Upload Audio
Users can upload the student's voice recording and provide the expected answer that will be used as the reference for evaluation.

<img width="1847" height="947" alt="Screenshot 2026-07-06 211510" src="https://github.com/user-attachments/assets/2e60653f-4701-4d94-a3f6-4ab8a2b3d992" />

---

### 🤖 3. AI Analysis
The uploaded audio is transcribed into text using **OpenAI Whisper**. The transcribed response is then evaluated by **Google Gemini AI** to assess the student's conceptual understanding.

<img width="1868" height="939" alt="Screenshot 2026-07-06 211603" src="https://github.com/user-attachments/assets/58d447ca-8896-4471-896f-5fbf6c27955a" />

<img width="1733" height="863" alt="Screenshot 2026-07-06 211618" src="https://github.com/user-attachments/assets/8818a52e-ca17-4316-8443-fabf161bbc2b" />

---

### 📊 4. Dashboard
The dashboard presents the complete evaluation results, including the similarity percentage, score, grade, transcript, AI-generated feedback, strengths, weaknesses, and suggestions for improvement.

<img width="1814" height="867" alt="Screenshot 2026-07-06 211640" src="https://github.com/user-attachments/assets/4ffc9f3c-8e8a-4c04-a84e-a2214b29ef47" />

<img width="1839" height="946" alt="Screenshot 2026-07-06 211701" src="https://github.com/user-attachments/assets/691b52d6-2fe3-4f97-bc73-c2e853559a63" />

---

### 📄 5. PDF Report
The application generates a professional and downloadable PDF report that summarizes the complete evaluation. The report includes the student's transcript, similarity percentage, score, grade, AI-generated feedback, strengths, weaknesses, and suggestions for improvement.

<img width="1824" height="939" alt="Screenshot 2026-07-06 211724" src="https://github.com/user-attachments/assets/9a6f14e0-653c-4f8f-9fb1-abbe6c5536ce" />

<img width="1920" height="1017" alt="Screenshot 2026-07-06 211734" src="https://github.com/user-attachments/assets/8f1e5471-80c5-4dc5-a537-c3166d826255" />

## 📂 Project Documentation

This repository includes complete project documentation covering every phase of the development lifecycle:

- 💡 Brainstorming & Ideation
- 📋 Requirement Analysis
- 🏗️ System Design
- 📅 Project Planning
- 💻 Development Phase
- 🧪 Testing & Validation
- 📖 Project Documentation
- 🎥 Project Demonstration

---

## 🎓 Academic Information

### **Project Title**
**Voice-Based Concept Understanding Analyser**

### **Domain**
Artificial Intelligence | Machine Learning | Speech Processing | Natural Language Processing

### **Institution**
Anil Neerukonda Institute of Technology and Sciences (ANITS)

### **Department**
Computer Science and Engineering (Data Science)

---

## 🔮 Future Enhancements

- 🌐 Multi-language speech support
- ⚡ Real-time voice evaluation
- ☁️ Cloud database integration
- 🔐 User authentication and role-based access
- 📈 Student performance analytics dashboard
- 📱 Mobile application support
- 👨‍🏫 Teacher analytics and report management
- 🤖 Advanced AI-powered feedback generation
- 📊 Historical performance tracking
- 🎙️ Noise reduction and enhanced speech processing

---

## 👨‍💻 Project Team

This project was collaboratively developed by the following team members as part of the academic project at **Anil Neerukonda Institute of Technology and Sciences (ANITS)**.

| Name | Role | GitHub Profile |
|------|------|----------------|
| **Amjuri Sai Chaturya** | **Team Leader** | [@SaiChaturya](https://github.com/saichaturya018) |
| **Jami Yuktasri** | Team Member | [@Yuktasri](https://github.com/jamiyuktasri24csd-afk) |
| **Patnana Mahesh** | Team Member | [@Mahesh](https://github.com/maheshpatnana25) |
| **Vayalapalli Maneesha** | Team Member | [@Maneesha](https://github.com/maneesha2007) |


---

## 📜 License

This project is developed for educational and academic purposes.

---

## ⭐ Acknowledgements

We sincerely thank the following organizations and technologies for supporting this project:

- SmartBridge
- Anil Neerukonda Institute of Technology and Sciences (ANITS)
- Streamlit
- Google Gemini AI
- OpenAI Whisper
- Sentence Transformers
- Python Open Source Community
- Flask
- FFmpeg


### Thank you for visiting our repository!

</div>
