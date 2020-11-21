"""
Created on Oct 22 2020

@author: tincythomas
"""
from ExtractTweet import *
from CalculateSentiment import *
from Canada import *
from India import *
import queue
from threading import Thread
import numpy as np
import time;

class EmotionController:
    def __init__(self):
        self.emotions = CalculateSentiments()

    def start(self, location):
        print('Start---------')
        start = int(time.time())
        data = {}

        tweet = ExtractTweet()
        if(location.casefold() == 'canada'):
            hotSpots = Canada()
        if(location.casefold() == 'india'):
            hotSpots = India()

        hotSpotsValues = hotSpots.getHotSpots()
        print('Start---------1')
        que = queue.Queue()
        threads_list = list()
        for uniqueHotspot in hotSpotsValues:
            print('Start---------2')
            th = Thread(target=lambda q, arg1: q.put(tweet.getTweets(uniqueHotspot,location)), args=(que, '' ))
            #t.append(threading.Thread(target=tweet.getTweets, args=(uniqueHotspot,location)))
            th.start()
            threads_list.append(th)

        time.sleep(10)
        # Join all the threads
        for t in threads_list:
            #t.start()
            print('Start---------3')
            t.join();

        # Check thread's return value
        tweets = {}
        while not que.empty():
            print('Start---------4')
            province,locationTweet  = que.get()
            tweets[province] = locationTweet

        que = queue.Queue()
        threads_list = list()
        for location in tweets:
            print('Start---------5')
            th = Thread(target=lambda q, arg1: q.put(self.emotions.getScoresforTweets(
                location, tweets[location])), args=(que, '' ))
            #t.append(threading.Thread(target=tweet.getTweets, args=(uniqueHotspot,location)))
            th.start()
            threads_list.append(th)

        # Join all the threads
        for t in threads_list:
            print('Start---------6')
            #t.start()
            t.join()

        # Check thread's return value
        while not que.empty():
            print('Start---------7')
            location,result  = que.get()
            print("data----",result)
            data[location] = result
            #tweets[province] = locationTweet

        #print(data)
        stop = int(time.time())
        print("Function(Emotion Controller) a is running at time: " + str(stop-start) + " seconds.")
        return data

    def scoreForText(self, text):
        data = self.emotions.getScoreForText(text)
        #print(data)
        return data

    def scoreforProvince(self, province, country):
        data = {}
        tweet = ExtractTweet()
        locationTweet = tweet.getTweets(province,country)
        if(locationTweet.empty==False):
            #print(uniqueHotspot)
            data[province] = self.emotions.getScoresforTweets(province, locationTweet)

        #print(data)
        return data

    def getTweetsScores(self, hashtag):
        print('Inside getTweetsScores')
        tweet = ExtractTweet()
        result = tweet.getTweetsHashTag(hashtag)

        tweets = {}
        i = 0;
        for tweet in result:
            data = self.emotions.getScoreForText(tweet.text)
            tweets[i] = data
            i+=1

        return tweets