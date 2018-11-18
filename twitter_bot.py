import tweepy
from tweepy.auth import OAuthHandler
import authentication
import time

auth = OAuthHandler(authentication.consumerKey, authentication.consumerSecretKey)
auth.set_access_token(authentication.accessToken, authentication.accessTokenSecret)

api = tweepy.API(auth)

def retweeting(since_id):
    for tweet in api.mentions_timeline(since_id):
        try:
            tweet.favorite()
        except tweepy.TweepError:
            continue
        api.update_status('@' + tweet.user.screen_name + " this is a retweet from my bot :-) ",tweet.id)
        file.truncate(0)
        file.seek(0)
        file.writelines(str(tweet.id))
while True:
    with open('idfile.txt','r+') as file:
                lastTweetId = file.readlines()
                retweeting(lastTweetId[0].strip('\n'))
                time.sleep(5)
