#-*- coding: utf-8 -*-
import tweepy
import time
import traceback

# These are the required authentication keys, you should create your own and store them somewhere
from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret

# This is the listener, resposible for receiving data
class StreamListener(tweepy.StreamListener):
    # This will collect only status messages
    # If we use on_data instead, we need to process the json data ourselves
    def on_status(self, status):
        #import pdb; pdb.set_trace() # Use this if you want to stop the execution at this point (for debugging)
        print status.text # This will print the text content of the tweet
        return True

    def on_error(self, status):
        print "Error",status
        return False

if __name__ == '__main__':
    while True:
        try:
            l = StreamListener()
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            stream = tweepy.Stream(auth, l)
            stream.filter(track=[u"#peoplewhomademyday2015"],languages=["fi", "en"])
        except:
            traceback.print_exc()
            time.sleep(10)
