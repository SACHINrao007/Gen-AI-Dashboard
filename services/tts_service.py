# tts_service.py

import uuid
import os
from TTS.api import TTS

# Load model once
tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

AUDIO_DIR = "audio_outputs"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_tts(text: str) -> str:
    unique_filename = f"{uuid.uuid4()}.wav"
    file_path = os.path.join(AUDIO_DIR, unique_filename)
    tts_model.tts_to_file(text=text, file_path=file_path)
    return unique_filename
