# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:05:46 2015

@author: Jaaksi
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#consumer key, consumer secret, access token, access secret.
ckey='FpP4HT9mx2pyeRLmmznfhfMID'
csecret='SPG9mQvGnPz722MhOZYvtlVKyhFX1fOnICmfShjdx0n5GYZDBO'
atoken='3430530850-QPgfRXIVLHU8LPSzOUstoNDuyuoSZ9zPVkXzO1b'
asecret='muyJlFuaNAMSIitRUAHqVBqq9KRuqWF6zQ3idFs8nWwcI'

class listener(StreamListener):

    def on_data(self, status):
        try:
            print(status)
            saveFile = open('tweetbotdb.csv', 'a')
            saveFile.write(status)
            saveFile.write('\n')
            saveFile.close()
            return(True)
        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep(5)
    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#peoplewhomademyday2015"])