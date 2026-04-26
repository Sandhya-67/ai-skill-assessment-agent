from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import extract_text_from_pdf

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)
    return {"resume_text": text}