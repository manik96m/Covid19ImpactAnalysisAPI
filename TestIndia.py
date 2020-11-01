import unittest

from India import *

class TestIndia(unittest.TestCase):

    def testgetHotSpots(self):
        INhotspotCSV=pd.read_csv('covid_19_india.csv')
        for column_name, column in INhotspotCSV.transpose().iterrows():
            if(column_name=='State/UnionTerritory'):
                INhotspot=INhotspotCSV[column_name].dropna().unique()

        i = India()
        actualValue = i.getHotSpots()
        self.assertEqual(INhotspot[1], actualValue[1])

if __name__ == '__main__':
    unittest.main()