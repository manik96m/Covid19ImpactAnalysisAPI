"""
Created on Oct 22 2020

@author: tincythomas
"""
from ExtractTweet import *
from CalculateSentiment import *
import queue
from threading import Thread
import numpy as np
import time;

class EmotionController:

    def start(self, location):
        print('Start---------')
        start = int(time.time())
        data = {}

        print('After taking HorSpots')
        que = queue.Queue()
        threads_list = list()
        hotSpotsValues=""
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

    def scoreforProvince(self, lat, long):
        data = {}
        emotions = CalculateSentiments()
        tweet = ExtractTweet()
        province = str(lat)+ str(long)
        locationTweet = tweet.getTweetsLatLong(lat, long)
        if(locationTweet.empty==False):
            #print(uniqueHotspot)
            data[province] = emotions.getScoresforTweets(province, locationTweet)
        else:
            data =  {
                "provinceName": province,
                "analyticScore": 0,
                "tentativeScore": 0,
                "confidentScore": 0,
                "joyScore": 0,
                "sadnessScore": 0,
                "fearScore": 0,
                "angerScore": 0
            }
        #print(data)
        return data

    def getTweetsScores(self, hashtag):
        print('Inside getTweetsScores')
        emotions = CalculateSentiments()
        tweet = ExtractTweet()
        result = tweet.getTweetsHashTag(hashtag)

        tweets = {}
        i = 0;
        for tweet in result:
            data = emotions.getScoreForText(tweet.text)
            tweets[i] = data
            i+=1

        return tweets