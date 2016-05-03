import speech_recognition as sr
from utils import programs, say

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        google_speech(audio)

def google_speech(audio):
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        parse_command(r.recognize_google(audio))

    except sr.UnknownValueError:
        print("I'm sorry, I couldn't understand, please try again.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def parse_command(audio):
    audio = audio.lower()
    if audio.startswith('open'):
        programs.parse_program(audio)

    elif audio.startswith('google'):
        programs.parse_program(audio)

    elif 'exit' in audio:
        say.speak("I am shutting down now sir, Goodbye.")
        exit()

    else:
        say.speak("I'm sorry, I didn't understand {0}".format(audio))
        print(audio)

if __name__ == '__main__':
    while True:
        listen()
