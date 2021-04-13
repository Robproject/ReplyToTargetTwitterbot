# Twitterbot/bots/ReplyToLatest.py
from config import create_api
import time

api = create_api()
from os import environ

Target_user = environ['Target_user']
Replying_user = environ['Replying_user']
sleeptime = environ[sleeptime]
reply_text = environ['reply_text']


def reply_everytime(target_user, replying_user):
    class InitTweet:
        id = [0]
    oldtweet = [InitTweet()]
    make_tweet = "@" + target_user + " " + reply_text
    while True:
        try:
            target_user_tweet = api.user_timeline(screen_name=target_user, count=1)  # get target most recent status/tweet
            target_user_tweet1 = api.user_timeline(screen_name=target_user, count=1)  # secondary get target most recent status/tweet
            target_user_tweet_id = target_user_tweet[0].id
            target_user_tweet1_id = target_user_tweet1[0].id
            my_tweet = api.user_timeline(screen_name=replying_user, count=1)  # get replying most recent status/tweet
            my_tweet1 = api.user_timeline(screen_name=replying_user, count=1)  # secondary get replying most recent status/tweet
            if target_user_tweet_id == oldtweet[0].id:
                # if it's the same as the most recent tweet, skip
                print(str(target_user_tweet_id) + " = " + target_user + "'s most recent status id, which hasn't changed")
                time.sleep(sleeptime)
            elif target_user_tweet_id == target_user_tweet1_id == my_tweet[0].in_reply_to_status_id == my_tweet1[0].in_reply_to_status_id:
                # if the most recent status id of the targeted user is the same id as the status the replying user replied to (already been replied to)]
                # this check performed so no replies occur on startup
                # checks both id calls to make sure they're correct
                print(str(target_user_tweet_id) + " = " + target_user + "'s status id that " + replying_user + " already replied to")
                oldtweet = target_user_tweet
                time.sleep(sleeptime)
            elif target_user_tweet == target_user_tweet1 != my_tweet[0].in_reply_to_status_id == my_tweet1[0].in_reply_to_status_id:
                api.update_status(make_tweet, target_user_tweet_id)
                print(str(target_user_tweet_id) + " " + replying_user + " replied")
                # reply to targeted user most recent tweet
                # checks both id calls to make sure they're correct
                oldtweet = target_user_tweet
                time.sleep(sleeptime)
            else:
                print(str(target_user_tweet_id) + " = " + target_user + "'s double status id calls didn't match")
                # if tweet != tweet1 for checking replying or targeted user's last tweet, loop
        except IndexError:
            print("Whoops index error ")


def main():
    while True:
        reply_everytime(Target_user, Replying_user)


if __name__ == "__main__":
    main()
