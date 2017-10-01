import re
from datetime import datetime
from libjournal import json_journal
from voice import tts


libj = json_journal.libjournal()
libj.set_JSON_location("journal.json")


def create_entry(name, text):
    try:
        libj.add_entry(name, text)
        tts("Successfully added entry:" + name)
    except Exception as e:
        print(e)
        tts("Sorry, the journal did not save. Please try again!")


def delete_entry(name):
    try:
        libj.delete_entry(name)
        tts("Successfully deleted entry:" + name)
    except:
        tts("Sorry, the journal did not delete. Please try again!")


def read_entry(name):
    try:
        tts("Reading entry:" + name)
        libj.entry_read(name)
    except Exception as e:
        print(e)
        tts("Sorry, the journal did not read. Please try again!")

trigger_regex = re.compile('^post (.+) to my journal', re.IGNORECASE)

i = 1


def run(matches):
    global i
    create_entry(str(datetime.now()), matches.groups()[0])
    i += 1