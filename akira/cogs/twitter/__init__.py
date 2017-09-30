import re
from cogs.twitter.twitter import send_tweet

trigger_regex = re.compile('^tweet (.+)', re.IGNORECASE + re.UNICODE)

def run(tweet_r):
    send_tweet(tweet_r.groups(1).index(0))