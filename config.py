#!usr/bin/python

import tweepy
import os

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
key = os.environ['token_key']
secret = os.environ['token_secret']


def getApi():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    return tweepy.API(auth,
                      wait_on_rate_limit=True,
                      wait_on_rate_limit_notify=True)
