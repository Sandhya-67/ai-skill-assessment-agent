from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔥 ROUTES IMPORT
from app.routes import upload
from app.routes import analyze
from app.routes import questions
from app.routes import study_plan
from app.routes import evaluate

# 🚀 APP INIT
app = FastAPI(title="AI Skill Assessor 🚀")

# 🔥 CORS (Frontend connect ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production me restrict karna
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 🏠 HOME ROUTE
@app.get("/")
def home():
    return {"message": "Backend running perfectly 🚀"}

# 🔗 ROUTES CONNECT
app.include_router(upload.router)
app.include_router(analyze.router)
app.include_router(interview.router)
app.include_router(questions.router)
app.include_router(study_plan.router)
app.include_router(evaluate.router)