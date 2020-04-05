#!usr/bin/python

from config import getApi, query, tweetsNo, user_screen_name
from Bot import Bot
import schedule
import random
import time


def jobQoD(bot):
    bot.postQuoteOfDay()


def jobRT(bot):
    bot.searchHashtags(query, tweetsNo)


def jobRTFrom(bot):
    bot.postRetweetFromUser(user_screen_name, tweetsNo)


def main():
    bot = Bot(getApi())
    bot.print()
    print()

    schedule.every(15).to(30).minutes.do(jobRT, bot)
    # schedule.every().day.at("14:00").do(jobQoD, bot)
    schedule.every().day.at("16:00").do(jobRTFrom, bot)
    schedule.every().day.at("19:00").do(jobRTFrom, bot)
    schedule.every().day.at("21:00").do(jobRTFrom, bot)
    schedule.every().day.at("22:00").do(jobRTFrom, bot)

    print(schedule.jobs)
    print()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()