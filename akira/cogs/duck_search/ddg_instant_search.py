import urllib
import json

import requests
from lxml import html

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'

def ddg_instant_answer(query):
    urlencoded_query = urllib.parse.quote_plus(query)
    r = requests.get("http://api.duckduckgo.com/?q=" + urlencoded_query +"&format=json&pretty=1",
                     headers={'User-Agent': USER_AGENT})

    jdata = r.json()
    return jdata["RelatedTopics"][0]["Text"]

