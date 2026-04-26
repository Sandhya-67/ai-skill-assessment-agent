from fastapi import APIRouter
from app.services.ai_service import extract_skills
from app.models.request_model import AnalyzeRequest
import json

router = APIRouter()

@router.post("/analyze")
async def analyze(data: AnalyzeRequest):
    try:
        resume_text = data.resume_text
        jd_text = data.jd_text

        result = extract_skills(resume_text, jd_text)

        skills = json.loads(result)

        resume_skills = skills.get("resume_skills", [])
        jd_skills = skills.get("jd_skills", [])

        # 🔥 GAP LOGIC
        missing_skills = list(set(jd_skills) - set(resume_skills))

        return {
            "analysis": {
                "resume_skills": resume_skills,
                "jd_skills": jd_skills,
                "missing_skills": missing_skills
            }
        }

    except Exception as e:
        return {
            "analysis": {
                "resume_skills": [],
                "jd_skills": [],
                "missing_skills": []
            },
            "error": str(e)
        }