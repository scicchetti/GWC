# Imports

import tweepy
import random
import time
# Keys and Access Tokens

CONSUMER_KEY    = 'Ex1O728RH0sYG2a1JHg15q7EO'
CONSUMER_SECRET = '7436DwSnFlyJH9wffbbJlqQkDneiUzZ8kwMTh8jiBw8ll0iUMc'

ACCESS_TOKEN    = '1017154866664230912-9sKE3avVrjH4S3hTVrjqpDBQdBGMUY'
ACCESS_SECRET   = 'aXOBU61LGYrh3KR1zYUywuaLWxWEJSRv6Libh6cUW1vdm'
# Authentication

tweets = ["Are chocolate pudding? cuz you thiccc bbg", "Are you google? cuz I just found what im lookin for", "baddies only <3", "Are you religious? Because you’re the answer to all my prayers.", " Is your dad a terrorist? Cause you’re the bomb.", "I’d say God Bless you, but it looks like he already did.", "Are you cake? Cause I want a piece of that.", "Are you a beaver? Cause daaaaaaaaam" ""]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
count = 0
while True:
    count += 1
    index = random.randint(0, len(tweets) -1)
    api.update_status(tweets[index] + str(count))
    time.sleep(5)
