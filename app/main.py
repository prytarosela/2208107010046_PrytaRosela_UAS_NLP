import os
import tempfile
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from app.stt import transcribe_speech_to_text
from app.llm import generate_response
from app.tts import transcribe_text_to_speech

app = FastAPI(title="Voice Chatbot API")

@app.get("/")
def read_root():
    return {"message": "Voice Chatbot API is running"}

@app.post("/voice-chat")
async def voice_chat_endpoint(file: UploadFile = File(...)):
    # Simpan file audio yang diunggah
    audio_content = await file.read()
    file_ext = os.path.splitext(file.filename)[1]
    
    # Step 1: Speech-to-Text - Transkrip audio ke teks
    transcription = transcribe_speech_to_text(audio_content, file_ext)
    print(f"[STT] Transcription: {transcription}")
    
    # Step 2: LLM - Dapatkan respons dari model bahasa
    llm_response = generate_response(transcription)
    print(f"[LLM] Response: {llm_response}")
    
    # Step 3: Text-to-Speech - Ubah respons teks menjadi audio
    audio_response_path = transcribe_text_to_speech(llm_response)
    
    # Kembalikan file audio sebagai respons
    if os.path.exists(audio_response_path):
        return FileResponse(
            path=audio_response_path,
            media_type="audio/wav",
            filename="response.wav"
        )
    else:
        return {"error": "Failed to generate audio response"}