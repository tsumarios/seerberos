#!usr/bin/python

import tweepy
import os

query = '#cybersecurity OR #infosec OR #security OR #privacy -filter:retweets -filter:replies'
tweetsNo = 10
user_screen_name = 'kerb3ros05'

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
key = os.environ['TOKEN_KEY']
secret = os.environ['TOKEN_SECRET']


def getApi():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    return tweepy.API(auth,
                      wait_on_rate_limit=True,
                      wait_on_rate_limit_notify=True)
