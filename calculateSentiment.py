from ibm_watson import ToneAnalyzerV3 # @UnresolvedImport
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator # @UnresolvedImport
from extractTweet import *
import json

apikey = 'Kz7_imZk8dNzL2JMkhi4jjDm50EJouEe4O-90eH05g58'
url = 'https://api.au-syd.tone-analyzer.watson.cloud.ibm.com/instances/c4e49c5d-ea44-4c9c-9c63-e71c607c1268'

authenticator = IAMAuthenticator(apikey)
toneAnalyser = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
toneAnalyser.set_service_url(url)

def tweetEmotions(location):
    tweet = getTweets(location)
    outfile = open("sample.json",'w')
    analyticScore = 0;
    tentativeScore = 0;
    confidentScore = 0;
    joyScore = 0;
    sadnessScore = 0;
    fearScore = 0;
    for ind in tweet.index: 
        response = toneAnalyser.tone(str((tweet['text'][ind]).encode("utf-8")),content_type='text/plain')
        json_object = json.dumps(response.result)
        
        for row in response.result["document_tone"]["tones"]:
            #print(row)
            if(row['tone_id']=='analytical'):
                analyticScore+=row['score']
            if(row['tone_id']=='tentative'):
                tentativeScore+=row['score']
            if(row['tone_id']=='confident'):
                confidentScore+=row['score']
            if(row['tone_id']=='joy'):
                joyScore+=row['score']
            if(row['tone_id']=='sadness'):
                sadnessScore+=row['score']
            if(row['tone_id']=='fear'):
                fearScore+=row['score']
                       
        outfile.write(json_object)
    print('EMOTIONAL ANALYSIS')
    print('analyticScore') 
    print(analyticScore) 
    print('tentativeScore')   
    print(tentativeScore) 
    print('confidentScore') 
    print(confidentScore) 
    print('joyScore')  
    print(joyScore) 
    print('sadnessScore') 
    print(sadnessScore) 
    print('fearScore')
    print(fearScore)  