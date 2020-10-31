"""Created on Oct 21 2020@author: ashlychinnuvarghese, tincythomas"""from ibm_watson import ToneAnalyzerV3 # @UnresolvedImportfrom ibm_cloud_sdk_core.authenticators import IAMAuthenticator # @UnresolvedImportimport jsonclass CalculateSentiments:    def __init__(self):        self.__apikey = 'Kz7_imZk8dNzL2JMkhi4jjDm50EJouEe4O-90eH05g58'        self.__url = 'https://api.au-syd.tone-analyzer.watson.cloud.ibm.com/instances/c4e49c5d-ea44-4c9c-9c63-e71c607c1268'        self.__authenticator = IAMAuthenticator(self.__apikey)        self.__toneAnalyser = ToneAnalyzerV3(version='2017-09-21', authenticator=self.__authenticator)        self.__toneAnalyser.set_service_url(self.__url)        self.__analyticScore = 0;        self.__tentativeScore = 0;            self.__confidentScore = 0;            self.__joyScore = 0;            self.__sadnessScore = 0;            self.__fearScore = 0;                def __tweetEmotion(self,tweet):        response = self.__toneAnalyser.tone(tweet,content_type='text/plain')                #json_object = json.dumps(response.result)                        return response        def __calculateScores(self,response):        for row in response.result["document_tone"]["tones"]:                        #print(row)                        if(row['tone_id']=='analytical'):                                self.__analyticScore+=row['score']                        if(row['tone_id']=='tentative'):                                self.__tentativeScore+=row['score']                        if(row['tone_id']=='confident'):                                self.__confidentScore+=row['score']                        if(row['tone_id']=='joy'):                                self.__joyScore+=row['score']                        if(row['tone_id']=='sadness'):                                self.__sadnessScore+=row['score']                        if(row['tone_id']=='fear'):                                self.__fearScore+=row['score']                     def getScoresforTweets(self,location,tweet):         data = {}         for ind in tweet.index:              response = self.__tweetEmotion(str((tweet['text'][ind]).encode("utf-8")))            self.__calculateScores(response)                                    data =  {                    "provinceName": location,                    "analyticScore": self.__analyticScore,                    "tentativeScore": self.__tentativeScore,                    "confidentScore": self.__confidentScore,                    "joyScore": self.__joyScore,                    "sadnessScore": self.__sadnessScore,                    "fearScore": self.__fearScore                    }        print('Total tweets :',tweet.size)        print('EMOTIONAL ANALYSIS')           print('analyticScore :',self.__analyticScore)             print('tentativeScore :',self.__tentativeScore)             print('confidentScore :',self.__confidentScore)             print('joyScore :',self.__joyScore)             print('sadnessScore :',self.__sadnessScore)             print('fearScore :',self.__fearScore)             return  data        def getScoreForText(self,text):        data = {}         response = self.__tweetEmotion(str((text).encode("utf-8")))        self.__calculateScores(response)                            data["text"] =  {                    "type": "text",                    "analyticScore": self.__analyticScore,                    "tentativeScore": self.__tentativeScore,                    "confidentScore": self.__confidentScore,                    "joyScore": self.__joyScore,                    "sadnessScore": self.__sadnessScore,                    "fearScore": self.__fearScore                    }        return data                                                