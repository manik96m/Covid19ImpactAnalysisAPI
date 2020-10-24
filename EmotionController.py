from extractTweet import *
from calculateSentiment import *
from _ast import If
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/getScores', methods=['GET'])
def start():
    location = input("Enter the location to analyse tweets : ") 
    analyticScore = 0;    
    tentativeScore = 0;    
    confidentScore = 0;    
    joyScore = 0;    
    sadnessScore = 0;    
    fearScore = 0;
    data = {}
    outfile = open("sample.json",'w')
    if(location.casefold()=='canada'):
        CAhotspotCSV=pd.read_csv('COVIDCANADA.csv')
        for column_name, column in CAhotspotCSV.transpose().iterrows():
            if(column_name=='province'):
                CAhotspot=CAhotspotCSV[column_name].dropna().unique()
                for uniqueHotspotCA in CAhotspot: 
                    print('HOTSPOTS IN CANADA')
                    print(uniqueHotspotCA)
                    analyticScore, tentativeScore, confidentScore, joyScore, sadnessScore, fearScore =  tweetEmotions(uniqueHotspotCA)
                    data[uniqueHotspotCA] =  {
                                  "proviceName": uniqueHotspotCA,
                                  "analyticScore": analyticScore,
                                  "tentativeScore": tentativeScore,
                                  "confidentScore": confidentScore,
                                  "joyScore": joyScore,
                                  "sadnessScore": sadnessScore,
                                  "fearScore": fearScore
                                }
                    
                    
    if(location.casefold()=='india'):
        INhotspotCSV=pd.read_csv('covid_19_india.csv')
        for column_name, column in INhotspotCSV.transpose().iterrows():
            if(column_name=='State/UnionTerritory'):
                INhotspot=INhotspotCSV[column_name].dropna().unique()
                for uniqueHotspotIN in INhotspot: 
                    print('HOTSPOTS IN INDIA')
                    print(uniqueHotspotIN)
                    analyticScore, tentativeScore, confidentScore, joyScore, sadnessScore, fearScore =  tweetEmotions(uniqueHotspotIN)              
                    data[uniqueHotspotIN] =  {
                                  "proviceName": uniqueHotspotIN,
                                  "analyticScore": analyticScore,
                                  "tentativeScore": tentativeScore,
                                  "confidentScore": confidentScore,
                                  "joyScore": joyScore,
                                  "sadnessScore": sadnessScore,
                                  "fearScore": fearScore
                                }
                              
                            
                    
    outfile.write(json.dumps(data))
    return json.dumps(data)

if __name__ == "__main__":
   # running controller function
   start()