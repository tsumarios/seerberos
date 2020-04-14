#!usr/bin/python

from config import getApi, query, tweetsNo, user_screen_name
from Bot import Bot
import schedule
import time


def jobRT(bot):
    bot.searchHashtags(query, tweetsNo)


def main():
    bot = Bot(getApi())
    bot.print()
    print()

    jobRT(bot)
    schedule.every(2).to(3).hours.do(jobRT, bot)

    print(schedule.jobs)
    print()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()