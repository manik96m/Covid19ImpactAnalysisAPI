"""
Created on Oct 30 2020

@author: tincythomas
JUNIT test cases to caluculate scores of tweets using IBM Tone Analyser
"""

from EmotionController import *
import unittest


class TestEmotionController(unittest.TestCase):
    def setUp(self):
        self.e = EmotionController()

    def testTweetEmotions(self):
        data = self.e.start('Canada')
        #self.assertTrue('Ontario' in data.values()['provinceName'])
        self.assertTrue('provinceName' in data.keys())

    def testTextEmotions(self):
        data = self.e.scoreForText('#COVID19 does not even spare alcoholics. So, bust this myth and stop consuming alcohol to safeguard yourself from #Coronavirus.;Delhi Better be at home and take precautionary measures to fight against #CoronavirusPandemic. ;Poetry')
        self.assertTrue('text' in data.keys())

if __name__ == '__main__':
    unittest.main()
