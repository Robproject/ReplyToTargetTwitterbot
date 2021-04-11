# Twitterbot/bots/config.py

import logging
import tweepy as tp

logger = logging.getLogger()


def create_api():
    consumer_key = 'fZJFAqx5pGaToxORIKmjxW3cS'
    consumer_secret = '4wn9ZGs80g08tnwhaiqUF0RQgC8ZkABfwaIKjiJ0JQVaGFfCDO'
    access_token = '1366627415389212675-JHK0IbFIzZhfRe1XEHGmbnGiRLOT2T'
    access_secret = 'F15tNwEV8u9NzhThBVT1oiDhYst2YnQu2YPAz1pVZBU81'

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
