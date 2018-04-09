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

    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    if (not api):
        print ("Can't Authenticate")
        sys.exit(-1)


    files = ["./SNOPES.JSON","POLITIFACT.JSON","BUZZFEED.JSON","URBAN_LEGENDS.JSON"]

    counter = 0
    for file in files:
        try:
            documents = json.load(open(file))
            for document in documents:
                counter = counter + 1
                query = ' '.join(document['terms'])
                print(query)
                searched_tweets = [status._json for status in tweepy.Cursor(api.search, q=query).items(1000)]
                file = 'output/{}.json'.format(''.join(document['terms']))

                if searched_tweets:
                    with open(file, 'w', encoding='utf8') as fp:
                        json.dump(searched_tweets, fp)
        except FileNotFoundError:
            print("File does not exists")


    #new_tweets = api.search(q=' '.join(terms), count=100, lang="en")
    #print(new_tweets)

    #stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['carrot','chlorin','babi','cut'])
