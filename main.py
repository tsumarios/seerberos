#!usr/bin/python

from config import getApi
from Bot import Bot
import schedule
import random
import time

query = '#cybersecurity #infosec OR #cybersecurity OR #infosec OR #pentesting OR #security OR #privacy -is:retweet -is:reply followers_count:500'
tweetsNo = 10
trustThershold = 500  # Min number of followers to make the bot retweet
user_screen_name = 'zMrDevJ'


def jobQoD(bot):
    bot.postQuoteOfDay()


def jobRT(bot):
    bot.searchHashtags(query, tweetsNo, trustThershold)


def jobRTFrom(bot):
    bot.postRetweetFromUser(user_screen_name, tweetsNo)


def main():
    bot = Bot(getApi())

    schedule.every().day.at("10:00").do(jobQoD, bot)
    schedule.every(2).hours.do(jobRTFrom, bot)
    schedule.every(5).to(10).minutes.do(jobRT, bot)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()