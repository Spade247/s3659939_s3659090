#!/usr/bin/env python3
"""
Authors: Yonas Sisay s3659939 
         Amrit Mundi s3659990
"""
# Import relevant modules and classes to be used by the program
import json 


class Monitor:
    def __init__(self):

        with open ('config.json','r') as configFile:

            self.__ranges = json.load(configFile)
            self.__maximumTemperature = self.__ranges['max_temperature']
            self.__minimumTemperature = self.__ranges['min_temperature']
            self.__maximumHumidity = self.__ranges['max_humidity']
            self.__minimumHumidity = self.__ranges['min_humidity']



    def getMinTemperature(self):
        return (self.__minimumTemperature)
    
    def getMaxTemperature(self):
        return (self.__maximumTemperature)

    def getMinHumidity(self):
        return (self.__minimumHumidity)

    def getMaxHumidity(self):
        return (self.__maximumHumidity)


