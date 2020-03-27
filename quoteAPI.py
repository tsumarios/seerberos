#!usr/bin/python

import requests

url = 'https://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=1'


def getQuoteOfDay():
    response = requests.get(url=url)
    json_data = response.json(
    ) if response and response.status_code == 200 else None

    # Parse data
    if json_data:
        quote = json_data['thought']['quote']
        author = json_data['thought']['thoughtAuthor']['name']
        return quote, author