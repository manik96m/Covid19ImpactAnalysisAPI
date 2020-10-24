#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 07:32:12 2020

@author: ashlychinnuvarghese
"""

import pandas as pd

entireCSV=pd.read_csv('covid19_tweets.csv')

def getTweets(location):
    tweet=pd.DataFrame(entireCSV,columns =['user_verified','user_location','text'])
    tweetbyLocation=tweet[tweet["user_location"]== location]
    tweetbyLocationAndVerifiedUsers=tweetbyLocation[tweetbyLocation["user_verified"]== True]
    tweetText=pd.DataFrame(tweetbyLocationAndVerifiedUsers,columns =['text'])
    
    return tweetText