"""
Authors: Yonas Sisay s3659939 
         Amrit Mundi s3659990
"""
# Import relevant modules and classes to be used by the program
from Database import Database
from DataLogger import DataLogger

class DatabaseManager:
    """
        This class represents the interaction with the DataLogger class and the Database
    """

    def __init__(self,data):
        """
            On initialisation the DatabaseManager class establishes a connection to the database by instantiating the Database Class
            and inserts the data that was passed through the parameter into the database

            Arguments:
                data {DataLogger()} -- An instantiation of the DataLogger class to get the current time,temperature,humidity and date
                                        that needs to be inserted into the database
        """
        
        # store the instantiation of the datalogger class into a variable
        self.__dataLogger = data
        # Instantiate the Database class to have a connection to the database
        self.__database = Database()

        # Hard code the name of the table that needs to be created
        self.__table = "TEMPERATURE_data"

        # Get the data needed to be insert into the database from the DataLogger class
        self.__currentTemperature = str(data.getTemperature())
        self.__currentHumidity = str(data.getHumidity())
        self.__currentTime = str(data.getTime())
        self.__currentDate = str(data.getDate())
        
        # Create the database table with the hard coded value
        self.__database.createDBTable(self.__table)

        # insert the data into the table created
        self.__database.insertDBData(self.__currentTime, self.__currentTemperature,self.__currentHumidity,self.__currentDate)

        # inform the database to save changes made to the table
        self.__database.saveChanges()

    def closeDBConnection(self):
        """
            Closes the connection to the database through the inheritance of the Database function

        """
        # close the database connection
        self.__database.closeDBConnection()
        
        
    def verifyDate(self):
        """
           Verifies if the date has been recorded in the database 
           
           Returns:
                [True] -- Returns a True if the the data is being inserted for the first time for the current date
                [False] -- Returns a False if the the data being inserted is not for the first time

        """
        # declare a count to store a number that represents how many data rows have been created within the current date
        count = self.__database.verifyDate(self.__currentDate)

        # If the number of rows in the database is 1 meaning this is the initial row for the day return a True
        if (count == 1):
            return True
        # If the number of rows in the database is greater than 1 meaning this isnt the initial row for the day return a False
        elif (count >= 1 ):
            return False
        # If the number of rows in the database is 0 
        else:
            return True
