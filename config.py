# Twitterbot/bots/config.py


import tweepy as tp
from os import environ




def create_api():
    consumer_key = environ['CONSUMER_KEY']
    consumer_secret = environ['CONSUMER_SECRET']
    access_token = environ['ACCESS_KEY']
    access_secret = environ['ACCESS_SECRET']

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:

        raise e

    return api
