from fastapi import APIRouter
from app.services.ai_service import generate_study_plan

router = APIRouter()

@router.post("/study-plan")
def study_plan(data: dict):
    skills = data.get("skills", "")

    plan = generate_study_plan(skills)

    return {
        "plan": plan
    }