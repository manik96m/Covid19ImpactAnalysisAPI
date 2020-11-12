"""
Created on Oct 22 2020

@author: tincythomas
"""
from ExtractTweet import *
from CalculateSentiment import *
from Canada import *
from India import *


class EmotionController:
    def __init__(self):
        self.emotions = CalculateSentiments()

    def start(self, location='canada'):
        data = {}

        tweet = ExtractTweet()
        if(location.casefold() == 'canada'):
            hotSpots = Canada()
        if(location.casefold() == 'india'):
            hotSpots = India()

        hotSpotsValues = hotSpots.getHotSpots()

        for uniqueHotspot in hotSpotsValues:
            locationTweet = tweet.getTweets(uniqueHotspot,location)
            if(locationTweet.empty==False):
                #print(uniqueHotspot)
                data[uniqueHotspot] = self.emotions.getScoresforTweets(
                    uniqueHotspot, locationTweet)

        #print(data)
        return data

    def scoreForText(self, text):
        data = self.emotions.getScoreForText(text)
        #print(data)
        return data
