import tweepy
from modules.twitter.twitter_cfg import cfg

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def send_tweet(tweet_contents):
    api = get_api(cfg)
    tweet = tweet_contents
    status = api.update_status(status=tweet)
