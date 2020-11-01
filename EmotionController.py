"""
Created on Oct 22 2020

@author: tincythomas
"""
from ExtractTweet import *
from CalculateSentiment import *
from Canada import *
from India import *
from _ast import If
from flask_cors import CORS
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

class EmotionController:
    def __init__(self):
        self.emotions = CalculateSentiments();

    @app.route('/getScores', methods=['GET'])
    def start(self,location = 'canada'):
        data = {}

        tweet = ExtractTweet()
        if(location.casefold()=='canada'):
            hotSpots = Canada()
        if(location.casefold()=='india'):
            hotSpots = India()

        hotSpotsValues = hotSpots.getHotSpots()

        for uniqueHotspot in hotSpotsValues:
            locationTweet = tweet.getTweets(uniqueHotspot,location)
            if(locationTweet.empty==False):
                print(uniqueHotspot)
                data[uniqueHotspot] = self.emotions.getScoresforTweets(uniqueHotspot,locationTweet)

        print(data)
        return data

    def scoreForText(self,text):
        data = self.emotions.getScoreForText(text)
        print(data)
        return data

app.run()

if __name__ == "__main__":
    # running controller function
    e = EmotionController()
    e.scoreForText('This is my text and I am feeling happy to write this text but it could have been better')
    e.start()
