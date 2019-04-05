from Database import Database 
from Monitor import Monitor
from datetime import date
import csv

class Report:

    def __init__(self):
        self.__database = Database()
        self.__monitor = Monitor()

        self.__minTemperature = self.__monitor.getMinTemperature()
        self.__maxTemperature = self.__monitor.getMaxTemperature()
        self.__minHumidity = self.__monitor.getMinHumidity()
        self.__maxHumidity = self.__monitor.getMaxHumidity()

        self.__arrayOfDates = self.__database.getDates()
        self.__avgTemperature = None
        self.__avgHumidity = None
        self.__status = "some status"
        self.__message = "some message"



    def getDates(self):
        return (self.__arrayOfDates)
    
    def setAvgTemperature(self,date):

        self.__avgTemperature = self.__database.getAvgTemperature(str(date))
   
    def getAvgTemperature(self,date):

        self.setAvgTemperature(date)

        return (self.__avgTemperature)
    
    def setAvgHumidity(self,date):
        self.__avgHumidity = self.__database.getAvgHumidity(str(date))
    
    def getAvgHumidity(self,date):

        self.setAvgHumidity(date)

        return (self.__avgHumidity)

    def getStatus(self):

        if self.__avgTemperature < self.__minTemperature or self.__avgTemperature > self.__maxTemperature  or self.__avgHumidity < self.__minHumidity or self.__avgHumidity > self.__maxHumidity :
            self.__status = "BAD!"
            return(self.__status)
        else:
            self.__status = "OK!"
            return(self.__status)

    def getMessage(self,status):

        self.__message = status+" "

        if self.__avgTemperature < self.__minTemperature:
             self.__message += str(round(self.__minTemperature - self.__avgTemperature,1))+"*C below minimum temperature:  "
        
        if self.__avgTemperature > self.__maxTemperature:
             self.__message += str(round(self.__avgTemperature - self.__maxTemperature,1))+"*C above maximum temperature:  "
        
        if self.__avgHumidity < self.__minHumidity:
             self.__message += str(round(self.__minHumidity - self.__avgHumidity,1))+"% below minimum humidity:  "

        if self.__avgHumidity > self.__maxHumidity:
             self.__message += str(round(self.__avgHumidity - self.__maxHumidity,1))+"% above maximum humidity:  "
        
        return (self.__message)
        
    






