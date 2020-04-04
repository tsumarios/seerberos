#!usr/bin/python

from config import getApi
from Bot import Bot
import random
import time

query = '#cybersecurity #infosec -filter:retweets'
tweetsNo = 10


def main():
    bot = Bot(getApi())

    bot.postQuoteOfDay()
    time.sleep(random.randrange(100, 300))

    while (True):
        bot.searchHashtags(query, tweetsNo)
        time.sleep(random.randrange(1800, 3600))


if __name__ == "__main__":
    main()