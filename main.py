#!usr/bin/python

from config import getApi
from Bot import Bot


def main():
    bot = Bot(getApi())
    bot.print()


if __name__ == "__main__":
    main()