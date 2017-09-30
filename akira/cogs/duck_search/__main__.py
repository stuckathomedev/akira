import urllib3

import requests
from lxml import html
from voice import tts

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'



def run(query):
    urlencoded_query = urllib3.sparse.quote_plus(query)
    r = requests.get("http://api.duckduckgo.com/?q=" + urlencoded_query +"&format=json&pretty=1",
                     headers={'User-Agent': USER_AGENT})

    jdata = r.json()
    tts("Your results: " + jdata["RelatedTopics"][0]["Text"])