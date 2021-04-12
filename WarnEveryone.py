
# Twitterbot/bots/followfollowers.py


from config import create_api
import time
api = create_api()

def warn_everyone(screen_name):
    oldtweet = ""
    HelpfulBotSays = " Disclaimer: This post not financial advice. Subsequent and potentially related market swings may be highly volatile. Independent due diligence is always recommended."
    while True:
        tweet = api.user_timeline(screen_name=screen_name, count=1) #get most recent status/tweet
        if tweet == oldtweet:   #if it's the same as the most recent tweet, skip
            time.sleep(60)
            print(tweet[0].id)
            pass
        elif HelpfulBotSays == api.user_timeline(screen_name="NiceHelpfulBot1", count=1)[0].text:
            time.sleep(60)
            print(tweet[0].id)
            oldtweet = tweet
            pass
            api.update_status("@" + screen_name + HelpfulBotSays, tweet[0].id)
            print(tweet[0].id)  # reply to most recent tweet
            oldtweet = tweet
            time.sleep(60)
def main():

    while True:
        warn_everyone("elonmusk")

if __name__ == "__main__":
    main()
