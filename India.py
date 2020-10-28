"""
Created on Oct 29 2020

@author: tincythomas
"""
import pandas as pd
from CovidHotSpots import CovidHotSpots

class India(CovidHotSpots):
    
    def getHotSpots(self):
        INhotspotCSV=pd.read_csv('covid_19_india.csv')
        for column_name, column in INhotspotCSV.transpose().iterrows():
            if(column_name=='State/UnionTerritory'):
                INhotspot=INhotspotCSV[column_name].dropna().unique()
                return INhotspot