#!usr/bin/python

from quoteAPI import getQuoteOfDay
import tweepy
import time


# Class Bot
class Bot:
    def __init__(self, api):
        self.api = api
        self.user = api.me()
        self.hashtags = '#cybersecurity #infosec'
        self.tweetNo = 10

    def postStatus(self, update):
        self.api.update_status(update)
        print('Status updated!')

    def postQuoteOfDay(self):
        quote, author = getQuoteOfDay()
        tweet = f'{quote.lstrip()}\n~{author}\n\n#QoD #quoteoftheday #quote #seerberos #feeds'
        self.postStatus(tweet)
        print('Posted the QoD!')

    # TODO Schedule this function with a Cursor update every tot
    def searchHashtags(self):
        tweets = tweepy.Cursor(self.api.search,
                               self.hashtags).items(self.tweetNo)
        for tweet in tweets:
            try:
                # TODO Implement a simple account check before retweetting
                tweet.retweet()
                print('Retweeted a tweet!')
                time.sleep(5)
            except tweepy.TweepError as e:
                print(e.reason)
                time.sleep(5)

    def print(self):
        msg = f'Hello, I\'m {self.user.screen_name}!'
        print(msg)