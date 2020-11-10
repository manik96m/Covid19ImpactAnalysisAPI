"""
Created on Oct 30 2020

@author: tincythomas
JUNIT test cases to check the scores of Tweets from Covid19 Hotspots
"""
import unittest
from CalculateSentiment import *
import pandas as pd
from io import StringIO
class TestCalculateSentiments(unittest.TestCase):
    def setUp(self):
        c = CalculateSentiments()
        self.sadnessScore = c.getScoreForText('I am sad');
        self.joyScore = c.getScoreForText('I am happy');
        self.angerScore = c.getScoreForText('I am angry');
        self.fearScore = c.getScoreForText('I am afraid');
        self.confidentScore = c.getScoreForText('I am confident that I have found the right path.');
        self.tentativeScore = c.getScoreForText('She tentatively raised her hand.');
        self.analyticScore = c.getScoreForText('Everybody knows that the world is round.');


    def testGetSadScore(self):
        self.assertTrue((self.sadnessScore['text']['sadnessScore'])>0)

    def testGetHappyScore(self):
        self.assertTrue((self.joyScore['text']['joyScore'])>0)

    def testGetAngryScore(self):
        self.assertTrue((self.angerScore['text']['angerScore'])>0)

    def testGetFearScore(self):
        self.assertTrue((self.fearScore['text']['fearScore'])>0)

    def testGetConfidentScore(self):
        self.assertTrue((self.confidentScore['text']['confidentScore'])>0)

    def testGetTentativeScore(self):
        self.assertTrue((self.tentativeScore['text']['tentativeScore'])>0)

    def testGetAnalyticScore(self):
        self.assertTrue((self.analyticScore['text']['analyticScore'])>0)


    def testNegativeSadScore(self):
        self.assertTrue((self.sadnessScore['text']['joyScore'])==0)

    def testNegativeJoyScore(self):
        self.assertTrue((self.joyScore['text']['sadnessScore'])==0)

    def testNegativeFearScore(self):
        self.assertTrue((self.fearScore['text']['joyScore'])==0)

    def testNegativeAngerScore(self):
        self.assertTrue((self.angerScore['text']['sadnessScore'])==0)

    def testNegativeConfidentScore(self):
        self.assertTrue((self.confidentScore['text']['sadnessScore'])==0)

    def testNegativeTentativeScore(self):
        self.assertTrue((self.tentativeScore['text']['angerScore'])==0)

    def testNegativeAnalyticScore(self):
        self.assertTrue((self.analyticScore['text']['confidentScore'])==0)

    def testTweetsSentiments(self):
        StringData = StringIO("""text;user_location
            #COVID19 does not even spare alcoholics. So, bust this myth and stop consuming alcohol to safeguard yourself from #Coronavirus.;Delhi
             Better be at home and take precautionary measures to fight against #CoronavirusPandemic. ;Poetry
            """)
        tweet_text = pd.read_csv(StringData, sep =";")
        #tweet_text = pd.DataFrame(data=str('').encode('utf-8'), columns=['text', "user_location"])
        cal = CalculateSentiments()
        result = cal.getScoresforTweets('Delhi',tweet_text)
        self.assertTrue(len(result) != 0)
        self.assertTrue('Delhi' in result.values())
        self.assertTrue('fearScore' in result.keys())


if __name__ == '__main__':
    unittest.main()