from tweepy import Stream
from tweepy import OAuthHandler
import json
import tweepy
from tweepy.streaming import StreamListener
import csv
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

class MyListener(StreamListener):
    
    def __init__(self, wr,n,api=None):
        self.count=0
        self.limit=n
        self.wr=wr
        super(MyListener, self).__init__()
    
    def on_status(self, status):
        self.count+=1
        if self.count<=self.limit:
            details=[status.text,status.user.location]
            wr.writerow(details)
            print(status.user.location)
            print(status.text)
        else:
            return False
    
    def on_error(self, status_code):
        if status_code==420:
            return False
        

consumer_key="VbczOzz5uswXOFxfyoizZznwU"
consumer_secret="iA8q2cruVNMfECoeCjPmzYBd6pGLgvRLYSMcqQS6RInuX0dGwt"
oauth_token="1354020534-L2PnMNeyKb3646R1gNqJc8PkZOLul3Eh8Inc8Os"
oauth_token_secret="EInD6Nma3xOFlnEZ0Tc9kALPLlhdA7juzKRGenhbR3WtG"

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(oauth_token, oauth_token_secret)

api = tweepy.API(auth)

print 'Enter the number of tweets:'
n=input()

print 'Enter the keyword(s)'
keywords = raw_input().split(' ')

tweet_csv = open("/home/suriya/Desktop/tweets.csv","wb")
wr = csv.writer(tweet_csv)


twitter_stream = Stream(auth, MyListener(wr,n))
twitter_stream.filter(languages=['en'],track=keywords)
