
# Twitterbot/bots/followfollowers.py

import tweepy as tp

from config import create_api
import csv
import time
api = create_api()



def get_all_tweets(screen_name):


    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[len(alltweets)-1]

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print
        "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print
        "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.favorite_count, tweet.retweet_count]
                 for tweet in alltweets]

    # write the csv
    with open('%s_tweets.csv' % screen_name, mode='w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)

    pass

def warn_everyone(screen_name):
    oldtweet = ""
    while True:
        tweet = api.user_timeline(screen_name=screen_name, count=1) #get most recent status/tweet
        if tweet == oldtweet:   #if it's the same as the most recent tweet, skip
            time.sleep(60)
            print(tweet[0].id)
            pass
        else:
            api.update_status("@" + screen_name + " Disclaimer: This post not financial advice. Subsequent and potentially related market swings may be highly volatile. Independent due diligence is always recommended.", tweet[0].id)
            print(tweet[0].id)  # reply to most recent tweet
            oldtweet = tweet
            time.sleep(60)

def main():

    while True:
        warn_everyone("elonmusk")

if __name__ == "__main__":
    main()
