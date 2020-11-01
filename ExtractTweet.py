#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 07:32:12 2020

@author: ashlychinnuvarghese
"""

import pandas as pd
import tweepy as tw
from opencage.geocoder import OpenCageGeocode



class ExtractTweet:
    def __init__(self):
        #OpenGeoCoder Credentials
        self.geocoderkey = 'c71a1dad8baa41ef9183884ca41eaa8e'
        self.geocoder = OpenCageGeocode(self.geocoderkey)
        ####TWEEPY API Credentials
        self.consumer_key = 'HYf9hWD2GTQIE9FJj2KnmEgK3'
        self.consumer_secret = 'UcoTUERlFUdNEH8bSGdsurWmBgkWBeQ8bibYpGCTJ6yBETRZoi'
        self.access_token = '1072429171282825216-vaSqhHHiH1qgiSG8G6RVO7XlfmUj9v'
        self.access_token_secret = 'LeQGo79kgA9dLcpgRYIbpnqX4tDgzTDU6C2xbpgJsFyKy'
        self.auth = tw.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tw.API(self.auth,wait_on_rate_limit=True)
        self.search_words = "#covid19"
        #date_since = "2020-03-01"
        self.new_search = self.search_words + " -filter:retweets"


    def getTweets(self,province,country):
        location_geo=str(province)+','+ str(country)
        print(location_geo)
        results = self.geocoder.geocode(location_geo)

        print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                                results[0]['geometry']['lng'],
                                results[0]['components']['country_code'],
                                results[0]['annotations']['timezone']['name']))
        geo=str(results[0]['geometry']['lat']) +','+str(results[0]['geometry']['lng'])+ ','+'5000km'
        print(geo)
        tweets = tw.Cursor(self.api.search,q=self.new_search,lang="en",geocode=geo).items(20)
        tweetsviatweepy = [[tweet.text.encode('utf-8'), tweet.user.location] for tweet in tweets]
        tweet_text = pd.DataFrame(data=tweetsviatweepy,
                                  columns=['text', "user_location"])
        print(tweet_text)
        return tweet_text