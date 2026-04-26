#  AI Skill Assessment & Learning Agent

##  Overview
This project is an AI-powered system that analyzes a user's resume against a job description and identifies skill gaps. It also conducts mock interviews and provides personalized study plans.

---

##  Features

- 📄 Resume upload and parsing  
- 📊 Skill extraction (Resume vs JD)  
- ❗ Missing skill detection  
- 🎤 AI Mock Interview  
- 🗣️ Speech-to-Text (User can speak answers)  
- 🔊 Text-to-Speech (AI speaks questions & feedback)  
- 📝 Answer evaluation with score  
- 📚 Study plan generation  

---

## 🎙️ Voice Features

This system supports real-time voice interaction:
- Users can answer using voice (Speech-to-Text)
- AI responds using voice (Text-to-Speech)

---

## 🛠️ Tech Stack

- Backend: FastAPI (Python)  
- Frontend: HTML, CSS, JavaScript  
- AI Model: OpenRouter (LLaMA 3)  
- Speech Recognition: Web Speech API (STT)  
- Speech Synthesis: Web Speech API (TTS)  

---

## ▶️ How to Run

1. Clone the repository
```bash
git clone https://github.com/Sandhya-67/ai-skill-assessment-agent.git
## 🔧 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sandhya-67/ai-skill-assessment-agent.git
cd ai-skill-assessment-agent
```

---

### 2️⃣ Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variable

Create a `.env` file inside backend folder and add:

```text
OPENROUTER_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Backend Server

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

### 6️⃣ Run Frontend

Open this file in browser:

```
frontend/chat.html
```

---

### 🎤 Optional (Voice Features)

* Uses browser Speech Recognition (STT)
* Uses Speech Synthesis (TTS)
* Works best in Google Chrome

---

### ✅ Features

* Resume Upload & Parsing
* Skill Extraction (Resume vs JD)
* Missing Skills Detection
* AI Mock Interview
* Answer Evaluation + Score
* Personalized Study Plan
* Voice Interaction (STT + TTS)

---
