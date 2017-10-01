from libjournal import json_journal
from voice import tts


libj = json_journal()


def create_entry(name, text):
    try:
        libj.add_entry(name, text)
        tts("Successfully added entry:" + name)
    except:
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
        libj.read_entry(name)
    except:
        tts("Sorry, the journal did not read. Please try again!")
