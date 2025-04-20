import os
import gtts
import pygame

def speak_text(text):
    try:
        # Generate speech and save as an MP3 file
        tts = gtts.gTTS(text=text, lang="en")
        save_path = os.path.join(os.getcwd(), "output", "speech.mp3")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        tts.save(save_path)
        print(f"Speech saved at: {save_path}")

        # Initialize Pygame mixer only once
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Load and play the speech file
        pygame.mixer.music.load(save_path)
        pygame.mixer.music.play()

        # Wait until audio finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Avoid CPU overuse

        # Properly unload the file to prevent issues
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("Speech played successfully!")

    except Exception as e:
        print(f"ERROR: {e}")
