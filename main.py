#!usr/bin/python

from config import getApi, query, tweetsNo, user_screen_name
from Bot import Bot
import schedule
import time


def jobRT(bot):
    bot.searchHashtags(query, tweetsNo)


def jobRTFrom(bot):
    bot.postRetweetFromUser(user_screen_name, tweetsNo)


def main():
    bot = Bot(getApi())
    bot.print()
    print()

    schedule.every(30).to(60).minutes.do(jobRT, bot)
    schedule.every().day.at("19:19").do(jobRTFrom, bot)

    print(schedule.jobs)
    print()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()