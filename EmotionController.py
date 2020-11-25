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

    def start(self, location):
        print('Start---------')
        start = int(time.time())
        data = {}


        if(location.casefold() == 'canada'):
            hotSpots = Canada()
        if(location.casefold() == 'india'):
            hotSpots = India()

        hotSpotsValues = hotSpots.getHotSpots()
        print('After taking HorSpots')
        que = queue.Queue()
        threads_list = list()
        for uniqueHotspot in hotSpotsValues:
            tweet = ExtractTweet()
            print('Getting tweets for hotspots')
            th = Thread(target=lambda q, arg1: q.put(tweet.getTweets(uniqueHotspot,location)), args=(que, '' ))
            #t.append(threading.Thread(target=tweet.getTweets, args=(uniqueHotspot,location)))
            th.start()
            threads_list.append(th)
            print('Ending tweets for hotspots')


        # Join all the threads
        for t in threads_list:
            #t.start()
            #time.sleep(2)
            print('Joining tweets for hotspots',t)
            t.join();
            #print('t.isAlive()',t,' -- ', t.isAlive())

        # Check thread's return value
        tweets = {}
        while not que.empty():
            print('Storing return value from tweets')
            province,locationTweet  = que.get()
            tweets[province] = locationTweet

        que = queue.Queue()
        threads_list = list()
        for location in tweets:
            self.emotions = CalculateSentiments()
            print('Starting IBM Tone Analyser')
            th = Thread(target=lambda q, arg1: q.put(self.emotions.getScoresforTweets(
                location, tweets[location])), args=(que, '' ))
            #t.append(threading.Thread(target=tweet.getTweets, args=(uniqueHotspot,location)))
            th.start()
            threads_list.append(th)
            print('Ending IBM Tone Analyser')

        # Join all the threads
        for t in threads_list:
            print('Joining IBM Tone Analyser ', t)
            #t.start()
            t.join()

        # Check thread's return value
        while not que.empty():
            print('Return Values from IBM Tone Analyser')
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