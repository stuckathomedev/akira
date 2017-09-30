import re
import tweepy
from voice import tts
from modules.twitter.twitter import send_tweet

trigger_regex = re.compile('^tweet(?: that)? (.+)', re.IGNORECASE + re.UNICODE)

def run(tweet_r):
    tweet = tweet_r.groups()[0]
    try:
        send_tweet(tweet)
        tts("Successfully sent tweet.")
    except tweepy.TweepError as e:
        if e.api_code == 187:
            tts("Sorry, you already posted that.")