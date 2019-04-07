#!/usr/bin/env python3
"""
Authors: Yonas Sisay s3659939 
         Amrit Mundi s3659990
"""
# Import relevant modules and classes to be used by the program
import json 


class Monitor:
    """
        This class represents the ranges within the config json file
    
    """

    def __init__(self):
        """
            On initialisation the Monitor class reads the config json file and stores the ranges into global variables
        """

        # Read the json file 
        with open ('config.json','r') as configFile:

            # store the contents of the JSON file into the ranges variable 
            self.__ranges = json.load(configFile)

            # store the ranges into variables by calling their keys
            self.__maximumTemperature = self.__ranges['max_temperature']
            self.__minimumTemperature = self.__ranges['min_temperature']
            self.__maximumHumidity = self.__ranges['max_humidity']
            self.__minimumHumidity = self.__ranges['min_humidity']



    def getMinTemperature(self):
        """
            Retrieves the minimum temperature 

            Returns:
                [Integer] -- An Integer that represents the minimum temperature

        """
        # return the minimum temperature
        return (self.__minimumTemperature)
    
    def getMaxTemperature(self):
        """
            Retrieves the maximum temperature 

            Returns:
                [Integer] -- An Integer that represents the maximum temperature

        """
        # return the maximum temperature
        return (self.__maximumTemperature)

    def getMinHumidity(self):
        """
            Retrieves the minimum humidity

            Returns:
                [Integer] -- An Integer that represents the minimum humidity

        """
        # return the minimum humidity 
        return (self.__minimumHumidity)

    def getMaxHumidity(self):
        """
            Retrieves the maximum humidity

            Returns:
                [Integer] -- An Integer that represents the maximum humidity

        """
        # return the maximum humidity
        return (self.__maximumHumidity)


