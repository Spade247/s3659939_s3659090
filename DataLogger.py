from datetime import datetime
from datetime import date
from virtual_sense_hat import VirtualSenseHat 

class DataLogger:

    def __init__(self):

        self.__table = "TEMPERATURE_data"
        self.__date = str(date.today())
        self.__time = datetime.now().strftime("%H:%M:%S")
        self.__sense = VirtualSenseHat.getSenseHat()
        self.__humidity = round(self.__sense.get_humidity(),2)
        self.__temperature = round(self.__sense.get_temperature(),2)


    def getTable(self):
        return(self.__table)
        
    def getHumidity(self):
        return (self.__humidity)
    
    def getTemperature(self):
        return (self.__temperature)
    
    def getDate(self):
        return (self.__date)
    
    def getTime(self):
        return (self.__time)