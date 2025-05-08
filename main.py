# main.py

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from services.llm_service import get_answer_from_ollama
from services.tts_service import generate_tts
import os

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    question: str
    answer: str
    audio_url: str

@app.post("/generate-answer", response_model=AnswerResponse)
async def generate_answer(request: QuestionRequest):
    answer = get_answer_from_ollama(request.question)
    filename = generate_tts(answer)
    audio_url = f"/audio/{filename}"
    return {
        "question": request.question,
        "answer": answer,
        "audio_url": audio_url
    }

@app.get("/audio/{filename}")
def get_audio(filename: str):
    file_path = os.path.join("audio_outputs", filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/wav", filename=filename)
    return {"error": "File not found"}
