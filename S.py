import tweepy
import json

with open("alicia.keys","r") as f_open:
    keys = f_open.read().splitlines()

consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

i = 0

for tweet in tweepy.Cursor(api.search, q="#vazajato", rpp=100 , lang="pt" , tweet_mode="extended").items(100):
    
    print(tweet._json["created_at"])
    print(tweet._json["user"]["screen_name"])

    if "retweeted_status" in tweet._json:
        #print(tweet._json["retweeted_status"]["created_at"])
        #print(tweet._json["retweeted_status"]["user"]["screen_name"])
        print("RETWEET")
        print(tweet._json["retweeted_status"]["full_text"])
        #print("\n#\n")
        #print(tweet._json["full_text"])
        #print(tweet._json)
    else:
        #print(tweet._json["created_at"])
        #print(tweet._json["user"]["screen_name"])
        print(tweet._json["full_text"])
        #print(tweet._json)
    print("\n",80*"#","\n")

