#!/usr/bin/env python3
from DataLogger import DataLogger 
from DatabaseManager import DatabaseManager
from Monitor import Monitor
from Weather import Weather
from sense_hat import SenseHat
from Schedule import Schedule
from pushbullet import Pushbullet
class Notification:

    def __init__(self,databaseManager):
    
        self.__databaseManager = databaseManager
        self.__pushbullet = Pushbullet("o.mhFygDkFL66fHWqvcLN4S7kW2R0xQaBU")
        self.__push = None
        self.__messageHead = "head"
        self.__messageBody = "body"
    


    def setMessageHead(self,messageHead):
        self.__messageHead = messageHead
    
    
    def setMessageBody(self, messageBody):
        self.__messageBody = messageBody
    
    def sendNotification(self):
        self.__databaseManager.verifyDate()

        if(True):

            self.__push = self.__pushbullet.push_note(self.__messageHead,self.__messageBody)
        else:
            
            pass
    