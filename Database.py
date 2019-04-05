
import sqlite3
from datetime import datetime
from datetime import date
from virtual_sense_hat import VirtualSenseHat as SenseHat

class Database:
    
    def __init__(self):

        self.__connection = sqlite3.connect('sensehat.db')
        self.__database = self.__connection.cursor()
        self.__table = None
        self.__date = None
        self.__count = None
        self.__sense = SenseHat()
        self.__arrayOfDates = None
        self.__avgTemperature = None
        self.__avgHumidity = None

    def createDBTable(self,table):
        self.__table = table
        createTbQuery = "CREATE TABLE IF NOT EXISTS " + self.__table + " ( time TEXT, temperature NUMERIC, humidity NUMERIC, date TEXT)"
        self.__database.execute(createTbQuery)

    def insertDBData(self,time,temperature,humidity,date):
        # insertDataQuery = "INSERT INTO TEMPERATURE_data values("+ str(time) +","+  str(temperature) +","+ str(humidity) +","+ str(date) +")"
        self.__database.execute("INSERT INTO TEMPERATURE_data values(?,?,?,?)",(time,temperature,humidity,date))
        self.__sense.clear()
        self.__sense.show_message("Data Added!",text_colour = [0,255,0],scroll_speed=0.05)

    def verifyDate(self, todayDate):
        self.__database.execute("SELECT COUNT(*) FROM TEMPERATURE_data WHERE date like ""'%" + todayDate +"'")
        self.__date = self.__database.fetchone()
        self.__count = self.__date[0]
        
        return (self.__count)

    def getDates(self):
        self.__database.execute("SELECT distinct date from TEMPERATURE_data")
        self.__arrayOfDates = self.__database.fetchall()
        
        return (self.__arrayOfDates)

    def getAvgTemperature(self,date):
        print(str(date))
        self.__database.execute("select avg(temperature) from TEMPERATURE_data where date like ""'%" + date  +"'")
        self.__avgTemperature = self.__database.fetchone()
        self.__avgTemperature = round(self.__avgTemperature[0],1)
        
        
        return (self.__avgTemperature)
    
    def getAvgHumidity(self,date):
        self.__database.execute("select avg(humidity) from TEMPERATURE_data where date like ""'%" + date +"'")
        self.__avgHumidity = self.__database.fetchone()
        self.__avgHumidity = round(self.__avgHumidity[0],1)
        
        
        return (self.__avgHumidity)

    def saveChanges(self):

        self.__connection.commit()

    def closeDBConnection(self):

        self.__connection.close()

    
