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




users = Cursor(auth_api.friends, screen_name="uae_3G").items()


HEADER = ['Screenname','name','followers_count','friends_count','statuses_count','location']


def processing_loop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)

    while True:
        try:
            user = next(users)
        except tweepy.TweepError:
            t.sleep(60*20)
            user = next(users)
        except StopIteration:
            break
        csv_writer.writerow([user.screen_name,user.name,user.followers_count,user.friends_count,user.statuses_count,user.location])
        csvfile.flush()
        t.sleep(5)

with open('results22.csv', 'w') as csvfile:
    processing_loop(csvfile)


