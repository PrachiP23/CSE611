import sys
import json
import tweepy
from tweepy.streaming import StreamListener
from datetime import datetime, date, time, timedelta
from collections import Counter
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from tweepy import Stream

access_token="868133989-zOiRlT4RrupuQB5vqCcqxbFkOh7hULPDXYmmCTX0"
access_token_secret="PC0fqODk581Np0JNyXFhhzXxMbkP5dfOINMLvDWZKnYzB"
consumer_key="zjwKBKpRo9f0FlUvvLZDJQDg9"
consumer_secret="wI85D16PRjjx68AEaCIk0uZNFPqSFdByYnR8VcYPcsNDuvUzgW"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['carrot','chlorin','babi','cut'])
