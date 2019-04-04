#!/usr/bin/env python3
from DataLogger import DataLogger 
from DatabaseManager import DatabaseManager
from Monitor import Monitor
from Notification import Notification 
from Weather import Weather
from sense_hat import SenseHat
from Schedule import Schedule

class MonitorAndNotify:

    def __init__(self):

        Scheduler = Schedule()
        data = DataLogger()
        dataManager = DatabaseManager(data)
        monitor = Monitor()
        weather = Weather(data,dataManager,monitor)
        sense = SenseHat()

        Scheduler.createSchedule()
        weather.verifyTemperature()
        weather.verifyHumidity()
        dataManager.closeDBConnection()
        sense.clear()

# End of main

 

# Call main function

MonitorAndNotify()