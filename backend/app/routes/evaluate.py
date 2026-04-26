from fastapi import APIRouter
from app.services.ai_service import evaluate_answer

router = APIRouter()

@router.post("/evaluate")
def evaluate(data: dict):
    skill = data.get("skill", "")
    answer = data.get("answer", "")

    result = evaluate_answer(skill, answer)

    return {
        "evaluation": result
    }