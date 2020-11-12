"""
Created on Oct 29 2020

@author: tincythomas
"""
import pandas as pd
from CovidHotSpots import CovidHotSpots

class Canada(CovidHotSpots):
    
    def getHotSpots(self):
        CAhotspotCSV=pd.read_csv('COVIDCANADA1.csv')
        for column_name, column in CAhotspotCSV.transpose().iterrows():
            if(column_name=='province'):
                CAhotspot=CAhotspotCSV[column_name].dropna().unique()
                return CAhotspot;
        
    