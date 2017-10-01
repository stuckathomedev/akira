import re
from modules.duck_search.ddg_instant_search import ddg_instant_answer
from voice import tts

trigger_regex = re.compile('^search for (.+)$')

def run(search_query):
    try:
        tts(f"Your results: {ddg_instant_answer(search_query.groups()[0])}")
    except:
        tts("Sorry, no results.")