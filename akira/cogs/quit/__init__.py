import re
from voice import tts

trigger_regex = re.compile('^quit$', re.IGNORECASE)

def run():
    tts("Bye!")
    quit()