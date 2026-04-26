from fastapi import APIRouter
from app.services.interview_service import generate_questions, evaluate_answer
from app.models.request_model import QuestionRequest, EvaluateRequest


router = APIRouter()

@router.post("/questions")
async def questions(data: QuestionRequest):
    return {"questions": generate_questions(data.skill)}


@router.post("/evaluate")
async def evaluate(data: EvaluateRequest):
    return {"evaluation": evaluate_answer(data.skill, data.answer)}