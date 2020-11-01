import unittest

from ExtractTweet import *

class TestExtractTweet(unittest.TestCase):
    def setUp(self):
        self.e = ExtractTweet()
    def testgetTweets(self):
        self.e = ExtractTweet()
        result = self.e.getTweets('Ontario','Canada');
        #for ind in result.index:
            #print("#covid19" in str(result['text'][ind]).casefold())
        self.assertEqual(len(result),20)

if __name__ == '__main__':
    unittest.main()
