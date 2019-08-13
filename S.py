import tweepy
import json
import re
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer


class Tweet:
    def __init__(self, date, user, retweet, hashtags, text, words):
        self.date = date
        self.user = user
        self.retweet = retweet
        self.hashtags = hashtags
        self.text = text
        self.words = words

    def printTweet(self):
        print("\n\n",80*"#","\n")
        print("DATA    : " + self.date)
        print("USERNAME: " + self.user)
        print("RETWEET?  " + str(self.retweet))
        print("HASHTAGS: ", end='')
        print(self.hashtags)
        print("TEXT:     " + self.text)
        print("STEMS:    ", end='')
        print(self.words)


################################################################################
#MAIN
################################################################################

capturedTweets = []

#import API keys
with open("alicia.keys","r") as f_open:
    keys = f_open.read().splitlines()

consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_secret = keys[3]

#auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#get stopwords from nltk
stopwords = set(stopwords.words('portuguese'))
stemmer = RSLPStemmer()


total = 0
c = tweepy.Cursor(api.search ,q="#lavajato" , lang="pt" ,tweet_mode="extended").items()
#iterate over the tweets
while True:
    total += 1
    try:
        tweet = c.next()
        if "retweeted_status" in tweet._json:
            retweet = 1
            hashtags = tweet._json["retweeted_status"]["entities"]["hashtags"]
            #remove mentions and hashtags
            text = re.sub(r"([^\s]+:\/\/[^\s]+)|(@[^\s]+)|(#[^\s]+)|(\n)", "", tweet._json["retweeted_status"]["full_text"].lower(), flags=re.MULTILINE)
        else:
            retweet = 0
            hashtags = hashtags = tweet._json["entities"]["hashtags"]
            #remove mentions and hashtags
            text = re.sub(r"([^\s]+:\/\/[^\s]+)|(@[^\s]+)|(#[^\s]+)|(\n)", "", tweet._json["full_text"].lower(), flags=re.MULTILINE)

        date = tweet._json["created_at"]
        user = tweet._json["user"]["screen_name"]
        words = re.findall(r"([-'a-zA-ZÀ-ÖØ-öø-ÿ]+)",text)
        words = [stemmer.stem(word) for word in words if word not in stopwords]

        capturedTweets.append(Tweet(date, user, retweet, hashtags, text, words))
        capturedTweets[-1].printTweet()
        print(total)

    except Exception as e:
        print(str(e))
        if capturedTweets != []:
            print("\n\n\n\n## SAVING ##")
            with open("twitter_lava.data","a") as f:
                for twt in capturedTweets:
                    f.write(twt.date.rstrip() + "\t-\t" + twt.text.rstrip() + "\t\n")
            capturedTweets = []
        print("## WAITING FOR 5 MINUTES ##\n\n\n\n")
        time.sleep(300)
        continue
