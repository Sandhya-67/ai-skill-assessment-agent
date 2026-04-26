from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    resume_text: str
    jd_text: str
    
# 👇 NEW MODELS

class QuestionRequest(BaseModel):
    skill: str

class EvaluateRequest(BaseModel):
    skill: str
    answer: str