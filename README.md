# Seerberos

Seerberos Feeds is a Twitter bot for cybersecurity and information security news.

## Features

Seerberos is currently able to update its status, retweet by seaching for given queries, retweet from a given user, post a quote of the day.
Especially, in the `config.py`file you can change the following default values:

```python
query = '#cybersecurity OR #infosec OR #security OR #privacy -filter:retweets -filter:replies'
tweetsNo = 10
user_screen_name = 'zMrSec'
```

Note that this project currently works with a free Twitter Developer plan and it's deployed on [PythonAnywhere](https://www.pythonanywhere.com/user/seerberos/), thus it can't post - the feature is implemented anyway - quotes of the day because of the free account limitations.

### Tech

Seerberos is developed in [Python](https://www.python.org/downloads/) using [Twitter APIs](https://developer.twitter.com/en/docs). The main modules and dependecies which make this tool to work properly are:

- [Tweepy](http://docs.tweepy.org/en/latest/) - an easy-to-use Python library for accessing the Twitter API
- [Schedule](https://pypi.org/project/schedule/) - an in-process scheduler for periodic jobs that uses the builder pattern for configuration

### Usage

Seerberos needs access to a set of keys and tokens generated by a [Twitter Developer App](https://developer.twitter.com/en/apps). These values are required to be exported as path variables, in order to make the bot using them, as follows:

```sh
export CONSUMER_KEY="<your_consumer_key>"
export CONSUMER_SECRET="<your_consumer_secret>"
export TOKEN_KEY="<your_token_key>"
export TOKEN_SECRET="<your_token_secret>"
```

You can start the bot by simply opening your favourite Terminal and typing:

```sh
python3 main.py
```

## Author

The project is developed with ♥ by [Mario Raciti](https://marioraciti.ml).

#### Contacts

For any questions or suggetions, please feel free to contact me:

- Email: marioraciti@pm.me
- LinkedIn: linkedin.com/in/marioraciti
- Twitter: twitter.com/zMrSec

## Todos

- Add more features and improve tweets quality.

**Enjoy Seerberos!**
