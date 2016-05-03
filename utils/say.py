import os
from gtts import gTTS
from subprocess import call

def speak(text):
    tts = gTTS(text=text, lang = 'en')
    tts.save('temp.mp3')
    call(['mpg123', 'temp.mp3'])
