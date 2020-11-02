from EmotionController import *


class TestEmotionController(unittest.TestCase):
    def setUp(self):
        self.e = EmotionController()

    def testTweetEmotions(self):
        data = self.e.start('Canada')
        self.assertTrue('Delhi' in result.values())
        self.assertTrue('fearScore' in result.keys())

    def testTextEmotions(self):
        data = self.e.scoreForText('#COVID19 does not even spare alcoholics. So, bust this myth and stop consuming alcohol to safeguard yourself from #Coronavirus.;Delhi Better be at home and take precautionary measures to fight against #CoronavirusPandemic. ;Poetry')
        self.assertTrue('fearScore' in result.keys())

if __name__ == '__main__':
    unittest.main()
