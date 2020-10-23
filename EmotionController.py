
from extractTweet import *
from calculateSentiment import *
from _ast import If


def start():
    location = input("Enter the location to analyse tweets : ") 
    if(location.casefold()=='canada'):
        CAhotspotCSV=pd.read_csv('COVIDCANADA.csv')
        for column_name, column in CAhotspotCSV.transpose().iterrows():
            if(column_name=='province'):
                CAhotspot=CAhotspotCSV[column_name].dropna().unique()
                for uniqueHotspotCA in CAhotspot: 
                    print('HOTSPOTS IN CANADA')
                    print(uniqueHotspotCA)
                    tweetEmotions(uniqueHotspotCA)

    if(location.casefold()=='INDIA'):
        INhotspotCSV=pd.read_csv('covid_19_india.csv')
        for column_name, column in INhotspotCSV.transpose().iterrows():
            if(column_name=='State/UnionTerritory'):
                INhotspot=INhotspotCSV[column_name].dropna().unique()
                for uniqueHotspotIN in INhotspot: 
                    print('HOTSPOTS IN INDIA')
                    print(uniqueHotspotIN)
                    tweetEmotions(uniqueHotspotIN)              
if __name__ == "__main__":
   # running controller function
   start()
