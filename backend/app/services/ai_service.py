import os
import requests
import json
from dotenv import load_dotenv

load_dotenv


API_KEY = API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("api key not found")

# 🔥 COMMON CONFIG






URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


# 🚀 EXTRACT SKILLS (SAFE + STABLE)
def extract_skills(resume_text, jd_text):
    prompt = f"""
You are an expert resume analyzer.

Extract ONLY technical skills.

STRICT RULES:
- Return ONLY JSON
- No explanation
- No extra text

FORMAT:
{{
  "resume_skills": ["skill1", "skill2"],
  "jd_skills": ["skill1", "skill2"]
}}

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        print("🔍 RAW RESPONSE:", response.text)

        res_json = response.json()

        # 🔥 SAFE CHECK
        if "choices" not in res_json:
            print("❌ API ERROR:", res_json)
            return '{"resume_skills": [], "jd_skills": []}'

        output = res_json["choices"][0]["message"]["content"]

        # 🔥 CLEAN JSON
        start = output.find("{")
        end = output.rfind("}") + 1

        if start != -1 and end != -1:
            json_str = output[start:end]
            return json_str

        return '{"resume_skills": [], "jd_skills": []}'

    except Exception as e:
        print("❌ ERROR:", str(e))
        return '{"resume_skills": [], "jd_skills": []}'


# 🚀 GENERATE QUESTIONS
def generate_questions(skill):
    prompt = f"""
You are a strict technical interviewer.

Ask ONLY ONE interview question for {skill}.

Rules:
- Only one question
- No explanation
- No numbering
- Start from basic level
"""

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        print("❌ QUESTION ERROR:", e)
        return "Explain the basics of this skill."


# 🚀 EVALUATE ANSWER (SHORT + SPEAK FRIENDLY)
def evaluate_answer(skill, answer):
    prompt = f"""
You are a strict but helpful interviewer.

Evaluate the answer for skill: {skill}

Answer: {answer}

RULES:
- VERY SHORT response (max 1-2 lines)
- First say: Good answer OR Needs improvement
- Then give score out of 10
- If wrong → explain simply in ONE line

FORMAT:
Good answer. Score: X/10
OR
Needs improvement. Score: X/10. Reason: ...
"""

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        output = response.json()["choices"][0]["message"]["content"]

        return output.strip().replace("\n", " ")

    except Exception as e:
        print("❌ EVALUATION ERROR:", e)
        return "Needs improvement. Score: 5/10"


# 🚀 STUDY PLAN
def generate_study_plan(skills):
    prompt = f"""
You are a helpful career coach.

Create a SHORT and clear study plan for: {skills}

Include:
- Topics
- Steps
- Practice
- Resources

Keep it simple.
"""

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        print("❌ STUDY PLAN ERROR:", e)
        return "Error generating study plan"