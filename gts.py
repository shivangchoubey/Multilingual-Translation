from gtts import gTTS
import os

text = "नमस्ते, यह एक परीक्षण है"
language = "hi"

try:
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("test_hindi.mp3")
    os.system("test_hindi.mp3")  # Try to play the file
    print("Speech generated successfully!")
except Exception as e:
    print("Error:", e)
