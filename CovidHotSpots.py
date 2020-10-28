"""
Created on Oct 29 2020

@author: tincythomas
"""
from abc import ABC, abstractmethod


class CovidHotSpots(ABC):
    @abstractmethod
    def getHotSpots(self):
        pass
    

    