#!usr/bin/python

from config import getApi
from Bot import Bot


def main():
    bot = Bot(getApi())
    bot.print()
    query = '#cybersecurity #infosec -filter:retweets'
    tweetsNo = 10
    bot.searchHashtags(query, tweetsNo)


if __name__ == "__main__":
    main()