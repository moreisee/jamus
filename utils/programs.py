from subprocess import call
from utils import say

def parse_program(audio):
    if audio.startswith('open browser') or audio.startswith('open chrome'):
        open_browser(None)
    elif audio.startswith('google'):
        google_search(audio)
    elif audio.startswith('open reddit'):
        say.speak("Opening reddit for you sir.")
        open_browser('reddit.com')

def google_search(audio):
    search_for = audio.replace('google ', '')
    say.speak("Searching for {0}".format(search_for))
    open_browser('https://www.google.com/search?q={0}'.format(search_for))

def open_browser(url):
    if url == None:
        call('sensible-browser')
    else:
        call(['sensible-browser', url])
