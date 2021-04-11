# Twitterbot/bots/config.py


import tweepy as tp




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

        raise e

    return api
