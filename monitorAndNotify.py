#!/usr/bin/env python3
"""
    This program monitors the current temperature and humidity and stores it into a database.
     Sends one notification a day to notify the user of the avg temperature and humidity of that date.
     This program is scheduled to run every minute of when the Raspberry Pi boots up.

    Authors: Yonas Sisay s3659939 
            Amrit Mundi s3659990
"""
# Import relevant modules and classes to be used by the program
from DataLogger import DataLogger 
from DatabaseManager import DatabaseManager
from Monitor import Monitor
from Notification import Notification 
from Weather import Weather
from virtual_sense_hat import VirtualSenseHat
from Schedule import Schedule

class MonitorAndNotify:
    """
        This class represents the monitoring and notifying of data 
    
    """
    def __init__(self):
        """ 
            On initialisation the MonitorAndNotify class reads the current data and inserts into the datbase every minute 
            and only sends a notification once a day
        
        """

        # Scheduler = Schedule()
        # Instantiate all relevant classes
        data = DataLogger()
        dataManager = DatabaseManager(data)
        monitor = Monitor()
        weather = Weather(data,dataManager,monitor)
        sense = VirtualSenseHat.getSenseHat()

        # Scheduler.createSchedule()

        # verify if the temperature is within the range
        weather.verifyTemperature()
        # verify if the humidity is within the range
        weather.verifyHumidity()

        # close the connection to the database
        dataManager.closeDBConnection()

        # clear anything displayed on the sense hat
        sense.clear()

# #Initialise the createReport class
MonitorAndNotify()