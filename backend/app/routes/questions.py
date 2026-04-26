from fastapi import APIRouter
from app.services.ai_service import generate_questions

router = APIRouter()

@router.post("/questions")
def get_questions(data: dict):
    try:
        skill = data.get("skill")

        # ❌ अगर skill नहीं मिला
        if not skill:
            return {
                "questions": "Please specify a skill to start the interview."
            }

        # 🔥 AI से question generate
        question = generate_questions(skill)

        # 🔥 Safety: multiple questions avoid
        if "?" in question:
            question = question.split("?")[0] + "?"

        return {
            "questions": question.strip()
        }

    except Exception as e:
        return {
            "questions": "Unable to generate question right now."
        }