"""
Created on Oct 30 2020

@author: tincythomas
JUNIT test cases to get Covid19 Hotspots of Canada
"""
import unittest

from Canada import *

class TestCanada(unittest.TestCase):

    def testgetHotSpots(self):
        CAhotspotCSV=pd.read_csv('COVIDCANADA.csv')
        for column_name, column in CAhotspotCSV.transpose().iterrows():
            if(column_name=='province'):
                CAhotspot=CAhotspotCSV[column_name].dropna().unique()

        c = Canada()
        actualValue = c.getHotSpots()
        self.assertEqual(CAhotspot[1], actualValue[1])

if __name__ == '__main__':
    unittest.main()