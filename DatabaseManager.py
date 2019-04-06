from Database import Database
from DataLogger import DataLogger

class DatabaseManager:

    def __init__(self,data):

        self.__dataLogger = data
        self.__database = Database()
        self.__table = "TEMPERATURE_data"

        self.__currentTemperature = str(data.getTemperature())
        self.__currentHumidity = str(data.getHumidity())
        self.__currentTime = str(data.getTime())
        self.__currentDate = str(data.getDate())
         
        self.__database.createDBTable(self.__table)
        self.__database.insertDBData(self.__currentTime, self.__currentTemperature,self.__currentHumidity,self.__currentDate)
        self.__database.saveChanges()

    def closeDBConnection(self):

        self.__database.closeDBConnection()
        
        
    def verifyDate(self):
        
        count = self.__database.verifyDate(self.__currentDate)

        if (count == 1):
            return True
        elif (count >= 1 ):
            return False
        else:
            return True
