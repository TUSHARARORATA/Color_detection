import io
from gtts import gTTS
import pygame

def text_to_speech(text):
    # Convert the given text to speech and save it to an in-memory file
    tts = gTTS(text=text, lang='en')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

def play_sound(audio_fp):
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load the mp3 data from the in-memory file-like object
    audio_fp.seek(0)
    pygame.mixer.music.load(audio_fp, 'mp3')
    
    # Play the mp3 data
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    #while pygame.mixer.music.get_busy():
       # pygame.time.Clock().tick(10)

'''if __name__ == '__main__':
    q='hi how do you do'
    text = q
    
    # Convert text to speech and get in-memory file-like object
    audio_fp = text_to_speech(text)
    
    # Play the generated speech audio
    play_sound(audio_fp)'''
