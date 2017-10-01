import re
from voice import tts

trigger_regex = re.compile('^quit.*$', re.IGNORECASE)

def run(x):
    tts("Okay, bye!")
    quit()