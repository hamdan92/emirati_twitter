from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import csv
import time as t


consumer_key="mcEc6I8ydFzzIZjqndPqyjrqH"
consumer_secret="xI8uxUEs1A5Qw3zvNsX8YgCH99pMryeRecBzMeclz2kovFoz52"
access_token="356283787-AI5TEyBDRnu1ZtDLMyMiYfzii9ayrWcOtdSFLOi8"
access_token_secret="1vi6NS15x5ohQhuEZ6x840PeDzZAM2Ovwr9eKLRvZu20l"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

account_list = []

with open('results22.csv') as csv_file:
  csv_reader=csv.reader(csv_file,delimiter=',')
  line_count=0
  for row in csv_reader:
    if line_count == 0 :
      line_count=line_count+1
    else:
      print (row[0])
      account_list.append(row[0])

for tweet in auth_api.user_timeline(account_list[0]):
      print(tweet.text)




""" if len(account_list) > 0:
  for target in account_list:
    print("Getting data for " + target)
    item = auth_api.get_user(target)
    print (item)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))

    tweets = item.statuses_count
    account_created_date = item.created_at
    delta = datetime.utcnow() - account_created_date
    account_age_days = delta.days
    print("Account age (in days): " + str(account_age_days))
    if account_age_days > 0:
      print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))

    hashtags = []
    mentions = []
    tweet_count = 0
    end_date = datetime.utcnow() - timedelta(days=30)


    for tweet in auth_api.user_timeline(account_list[0]):
      print(tweet.user.location)

      



    for status in Cursor(auth_api.user_timeline, id=target).items():
      tweet_count += 1
      if hasattr(status, "entities"):
        entities = status.entities
        if "hashtags" in entities:
          for ent in entities["hashtags"]:
            if ent is not None:
              if "text" in ent:
                hashtag = ent["text"]
                if hashtag is not None:
                  hashtags.append(hashtag)
        if "user_mentions" in entities:
          for ent in entities["user_mentions"]:
            if ent is not None:
              if "screen_name" in ent:
                name = ent["screen_name"]
                if name is not None:
                  mentions.append(name)
      if status.created_at < end_date:
        break
    
    

    print
    print("Most mentioned Twitter users:")
    for item, count in Counter(mentions).most_common(10):
      print(item + "\t" + str(count))
 
    print
    print("Most used hashtags:")
    for item, count in Counter(hashtags).most_common(10):
      print(item + "\t" + str(count))
 
    print
    print ("All done. Processed " + str(tweet_count) + " tweets.")
    print

 """