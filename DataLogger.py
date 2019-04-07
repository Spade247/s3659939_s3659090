"""
Authors: Yonas Sisay s3659939 
         Amrit Mundi s3659990
"""
# Import relevant modules and classes to be used by the program
from datetime import datetime
from datetime import date
from virtual_sense_hat import VirtualSenseHat 

class DataLogger:
    """
        This class represents the data that needs to be logged into the database
    
    
    """

    def __init__(self):
        """
            On initialisation the DataLogger class 
            record the following from the sensehat:
                                                    current time
                                                    current temperature
                                                    current humidity
                                                    current date
        
        """
        
        # Instantiate the sensehat 
        self.__sense = VirtualSenseHat.getSenseHat()

        # Declare variable to store the table name that the data needs to be logged into
        self.__table = "TEMPERATURE_data"

        # Declare variables that store the time and date of the required data 
        self.__date = str(date.today())
        self.__time = datetime.now().strftime("%H:%M:%S")
        
        # Declare variables that store the humidity and temperature from the sensehat  
        self.__humidity = round(self.__sense.get_humidity(),2)
        self.__temperature = round(self.__sense.get_temperature(),2)


    def getTable(self):
        """
            Retrieves the table name 

            Returns:
                [String] -- A String containing the table name where all the data is stored

        """
        # return the table name
        return(self.__table)
        
    def getHumidity(self):
        """
            Retrieves the current humidity 

            Returns:
                [Float] -- A Float containing the current humidity rounded to 2 decimal places
        """
        # return the current humidity 
        return (self.__humidity)
    
    def getTemperature(self):

        """
            Retrieves the current temperature

            Returns:
                [Float] -- A Float containing the current temperature rounded to 2 decimal places
        """
        # return the current temperature
        return (self.__temperature)
    
    def getDate(self):
        """
            Retrieves the current date

            Returns:
                [String] -- A String containing the current date 
        """
        # return the current date
        return (self.__date)
    
    def getTime(self):
        """
            Retrieves the current time

            Returns:
                [String] -- A String containing the current time 
        """
        # return the current time
        return (self.__time)