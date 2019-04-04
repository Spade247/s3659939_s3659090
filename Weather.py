#!/usr/bin/env python3
from DataLogger import DataLogger 
from DatabaseManager import DatabaseManager
from Monitor import Monitor
from Notification import Notification 
from sense_hat import SenseHat
from Schedule import Schedule

class Weather:

    def __init__(self,data,dataManager,monitor):

        self.__dataLogger = data
        self.__databaseManager = dataManager
        self.__monitor = monitor
        self.__notifier = Notification(self.__databaseManager)
        
        self.__temperature = self.__dataLogger.getTemperature()
        self.__humidity = self.__dataLogger.getHumidity()
        self.__minTemperature = self.__monitor.getMinTemperature()
        self.__maxTemperature = self.__monitor.getMaxTemperature()
        self.__minHumidity = self.__monitor.getMinHumidity()
        self.__maxHumidity = self.__monitor.getMaxHumidity()

    def verifyTemperature(self):

        if self.__temperature < self.__minTemperature:

            self.__notifier.setMessageHead("Temperature is very low!")
            self.__notifier.setMessageBody("Temperature: " + str(self.__temperature) +" is lower than the Min Temperature " + str(self.__minTemperature))
            self.__notifier.sendNotification()

        elif self.__temperature > self.__maxTemperature:

            self.__notifier.setMessageHead("Temperature is very high!")
            self.__notifier.setMessageBody("Temperature: " + str(self.__temperature) +" is higher than the Max Temperature " + str(self.__maxTemperature))
            self.__notifier.sendNotification()
            
        else: 
            self.__notifier.setMessageHead("Temperature is ok!")
            self.__notifier.setMessageBody("Temperature: " + str(self.__temperature) +" is ok." )
            self.__notifier.sendNotification()

    def verifyHumidity(self):

        if self.__humidity < self.__minHumidity:

            self.__notifier.setMessageHead("Humidity is very low!")
            self.__notifier.setMessageBody("Humidity: " + str(self.__humidity) +" is lower than the Min Humidity " + str(self.__minHumidity))
            self.__notifier.sendNotification()

        elif self.__humidity > self.__maxHumidity:

            self.__notifier.setMessageHead("Humidity is very high!")
            self.__notifier.setMessageBody("Humidity: " + str(self.__humidity) +" is higher than the Max Humidity " + str(self.__maxHumidity))
            self.__notifier.sendNotification()

        else: 

            self.__notifier.setMessageHead("humidity is ok!")
            self.__notifier.setMessageBody("Humidity: " + str(self.__humidity) +" is ok." )
            self.__notifier.sendNotification()



        


