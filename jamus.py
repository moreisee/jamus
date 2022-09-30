import speech_recognition as sr
import pyttsx3
from utils import programs, say

r = sr.Recognizer()

MASTER = "Sir"


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S" )
    speak(Time)


def date():
    year = int(datetime.datetime.now().year )
    month = int(datetime.datetime.now().month )
    date = int(datetime.datetime.now().day )
    speak(date)
    speak(month)
    speak(year)


def wishMe():
    speak("Welcome back sir")
    # speak("The current time is")
    # time()
    # speak("The current date is")
    # date()
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning " + MASTER)


    elif hour>=12 and hour<18:
        speak("Good Afternoon " + MASTER)


    else:
        speak("Good Evening " + MASTER)
    speak("I am JARVIS. Please tell me sir how may I help you?")

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
