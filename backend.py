from gtts import gTTS
import os

def generate_audio(text, filename="output.mp3"):
    """
    Generate speech audio from text using Google Text-to-Speech (gTTS).
    Saves output as an MP3 file and returns the filename.
    """
    if not text.strip():
        raise ValueError("Text input is empty. Please provide valid text.")

    # Generate speech
    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    return filename
