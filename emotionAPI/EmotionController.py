#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 07:32:12 2020

@author: tincythomas
"""

from . import extractTweet 
from . import calculateSentiment
from _ast import If
import pandas as pd
from django.shortcuts import render


def start(request):
    location = request.GET['location'] 
    print(location)
    analyticScore = 0;    
    tentativeScore = 0;    
    confidentScore = 0;    
    joyScore = 0;    
    sadnessScore = 0;    
    fearScore = 0;
    if(location.casefold()=='canada'):
        CAhotspotCSV=pd.read_csv('COVIDCANADA.csv')
        for column_name, column in CAhotspotCSV.transpose().iterrows():
            if(column_name=='province'):
                CAhotspot=CAhotspotCSV[column_name].dropna().unique()
                for uniqueHotspotCA in CAhotspot: 
                    print('HOTSPOTS IN CANADA')
                    print(uniqueHotspotCA)
                    analyticScore, tentativeScore, confidentScore, joyScore, sadnessScore, fearScore = calculateSentiment.tweetEmotions(uniqueHotspotCA)
    if(location.casefold()=='india'):
        INhotspotCSV=pd.read_csv('covid_19_india.csv')
        for column_name, column in INhotspotCSV.transpose().iterrows():
            if(column_name=='State/UnionTerritory'):
                INhotspot=INhotspotCSV[column_name].dropna().unique()
                for uniqueHotspotIN in INhotspot: 
                    print('HOTSPOTS IN INDIA')
                    print(uniqueHotspotIN)
                    analyticScore, tentativeScore, confidentScore, joyScore, sadnessScore, fearScore = calculateSentiment.tweetEmotions(uniqueHotspotIN) 
    
    return render(request,'result.html',{'analyticScore':analyticScore,
    'tentativeScore':tentativeScore,'confidentScore':confidentScore,'joyScore':joyScore,
    'sadnessScore':sadnessScore,'fearScore':fearScore} )