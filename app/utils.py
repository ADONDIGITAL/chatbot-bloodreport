# app/utils.py

from gtts import gTTS
from googletrans import Translator
import uuid
import os

# Create a folder for audio if it doesn't exist
AUDIO_FOLDER = "audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def translate_text(text, target_lang):
    if target_lang == "en":
        return text
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

def text_to_speech(text, lang_code):
    tts = gTTS(text=text, lang=lang_code)
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)
    tts.save(filepath)
    return f"/audio/{filename}"
