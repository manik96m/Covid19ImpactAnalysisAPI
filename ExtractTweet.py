#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 07:32:12 2020

@author: ashlychinnuvarghese
"""

import pandas as pd
import tweepy as tw
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
load_dotenv()
import os

class ExtractTweet:
    def __init__(self):
        #OpenGeoCoder Credentials
        self.geocoderkey = os.environ.get("geocoderkey")
        self.geocoder = OpenCageGeocode(self.geocoderkey)
        ####TWEEPY API Credentials
        self.consumer_key = os.environ.get("consumer_key")
        self.consumer_secret = os.environ.get("consumer_secret")
        self.access_token = os.environ.get("access_token")
        self.access_token_secret = os.environ.get("access_token_secret")
        self.auth = tw.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tw.API(self.auth,wait_on_rate_limit=True)
        self.search_words = "#covid19"
        #date_since = "2020-03-01"
        self.new_search = self.search_words + " -filter:retweets"


    def getTweets(self,province,country):
        print('Tweet Start')
        location_geo=str(province)+','+ str(country)
        #print(location_geo)
        results = self.geocoder.geocode(location_geo)

        #print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
        #                        results[0]['geometry']['lng'],
        #                        results[0]['components']['country_code'],
        #                        results[0]['annotations']['timezone']['name']))
        geo=str(results[0]['geometry']['lat']) +','+str(results[0]['geometry']['lng'])+ ','+'5000km'
        #print(geo)
        tweets = tw.Cursor(self.api.search,q=self.new_search,lang="en",geocode=geo).items(20)
        tweetsviatweepy = [[tweet.text.encode('utf-8'), tweet.user.location] for tweet in tweets]
        tweet_text = pd.DataFrame(data=tweetsviatweepy,
                                  columns=['text', "user_location"])
        #print(tweet_text)
        print('Tweet Stop')
        return province,tweet_text

    def getTweetsHashTag(self, hashtag):
        self.new_search = hashtag + " -filter:retweets"
        tweets = tw.Cursor(self.api.search,q=self.new_search,lang="en",
                           since="2017-04-03",full_text = True).items(20)
        return tweets