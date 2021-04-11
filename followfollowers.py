
# Twitterbot/bots/followfollowers.py

import tweepy as tp

from config import create_api
import time



def follow_followers(api):

    for follower in tp.Cursor(api.followers).items():
        if not follower.following:

            follower.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)

        time.sleep(60)

if __name__ == "__main__":
    main()
