from fastapi import APIRouter, UploadFile, File
from sentinel_x.modules.nlp.service import nlp_service
import shutil
import os

router = APIRouter()

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Save file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        result = nlp_service.transcribe_audio(temp_path)
        return result
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

@router.post("/analyze-text")
async def analyze_text(text: str):
    analysis = nlp_service.detect_threats(text)
    return {"analysis": analysis}
