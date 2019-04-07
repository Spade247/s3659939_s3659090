"""
Authors: Yonas Sisay s3659939 
         Amrit Mundi s3659990
"""
# Import relevant modules and classes to be used by the program
import sqlite3
from datetime import datetime
from datetime import date
from virtual_sense_hat import VirtualSenseHat 


class Database:
    """
        This class represents the interaction with an sqlite3 database
    """

    def __init__(self):
        """
            On initialisation the Database class connects to a database if it is not there it will create that database.
        """

        # Declare a variable to store the connection to a database if that data is not there it will create it and store it to the variable
        self.__connection = sqlite3.connect('sensehat.db')

        # Declare a variable to store the database' cursor to conduct commands and execute sql statements
        self.__database = self.__connection.cursor()

        # declare a variable to store the table name
        self.__table = None
        # declare a variable to store a date that is being verified
        self.__date = None
        # declare a variable to store the count of records within a specified date
        self.__count = None

        # Declare a variable to instatiate the sensehat
        self.__sense = VirtualSenseHat.getSenseHat()

        # Declare a variable to store an array of dates
        self.__arrayOfDates = None

        # Declare variables to store the average temeperature and humidity of of a specified date
        self.__avgTemperature = None
        self.__avgHumidity = None

    def createDBTable(self,table):
        """ 
            Creates a table  if it doesnt exist to contain the Time,Temperature,Humidity and Date every minute
            
            Arguments:
                table {String} -- A string of what the table will be named.
        """
        # store the table name to the global variable so it can be accessed within the whole class
        self.__table = table

        # Declare a variable to store a query to be run to create the table within the database
        createTbQuery = "CREATE TABLE IF NOT EXISTS " + self.__table + " ( time TEXT, temperature NUMERIC, humidity NUMERIC, date TEXT)"

        # Execute the query to create a table
        self.__database.execute(createTbQuery)

    def insertDBData(self,time,temperature,humidity,date):
        """
            Inserts the Time, Temperature, Humidity and Date that needs to be recorded every minute into the database
            
            Arguments:
                time {String} -- A string that outlines the time the temperature and humidity were taken
                temperature {String}-- A string that outlines the temperature that was taken
                humidity {String} -- A string that outlines the humidity that was taken
                date {String} -- A string that outlines the date the temperature and humidity were taken
        """

        # insertDataQuery = "INSERT INTO TEMPERATURE_data values("+ str(time) +","+  str(temperature) +","+ str(humidity) +","+ str(date) +")"
        
        # Execute a query to insert the data into the table
        self.__database.execute("INSERT INTO TEMPERATURE_data values(?,?,?,?)",(time,temperature,humidity,date))

        # recalibrate the sensor so it clears anything that is shown
        self.__sense.clear()
        # Display the a Data Added message everytime that data has been inserted into the database
        self.__sense.show_message("Data Added!",text_colour = [0,255,0],scroll_speed=0.05)

    def verifyDate(self, todayDate):
        """
            Verifies if the date passed is available within the database. Usually used to confirm if a Notification has been sent in that Date
            
            Arguments:
                todayDate {String} -- A String that contains the date that needs to queried in the database
            
            Returns:
                [integer] -- Returns an integer that represents how many records were created in that date
        """
        # Execute a query to count how many values have been added within the specified date
        self.__database.execute("SELECT COUNT(*) FROM TEMPERATURE_data WHERE date LIKE ""'%" + todayDate +"'")

        # store the first row returned from the database for that date
        self.__date = self.__database.fetchone()

        # store the number of rows created within that date to the global variable 
        self.__count = self.__date[0]
        
        # return the number of rows created within that date
        return (self.__count)

    def getDates(self):
        """
            Returns an array of all the distinct dates within the database
            
            Returns:
                [] -- Returns a list of all the distinct dates within the database
        """
        # Execute a query to list all the distinct dates within the database in ascending order
        self.__database.execute("SELECT DISTINCT date FROM TEMPERATURE_data ORDER BY date ASC")
        # Store the results of the query into the global variable 
        self.__arrayOfDates = self.__database.fetchall()
        # clean up the results given from the query and store them as a list eg. "2019-04-05","2019-04-06"
        self.__arrayOfDates = [item[0] for item in self.__arrayOfDates] 

        # return the list of all the distinct dates from the database
        return (self.__arrayOfDates)

    def getAvgTemperature(self,date):
        """
            Returns the average temperature for the specified date.
            
            Arguments:
                date {String} -- A string that contains a date to be queried
            
            Returns:
                [Integer] -- Returns the average temperature for the specified date rounded to 1 decimal
        """

        # Print the date that needs to be queried onto the commad line
        # print(str(date))
        # Execute a query to return the average temperature of the specified date 
        self.__database.execute("SELECT avg(temperature) FROM TEMPERATURE_data WHERE date LIKE ""'%" + date  +"'")
        # Store the average temperature row returned into the global variable
        self.__avgTemperature = self.__database.fetchone()
        # Round the temperature at index 0 to 1 decimal point
        self.__avgTemperature = round(self.__avgTemperature[0],1)
        
        # Return the average temperature for the specified date 
        return (self.__avgTemperature)
    
    def getAvgHumidity(self,date):
        """
            Returns the average humidity for the specified date.
            
            Arguments:
                date {String} -- A string that contains a date to be queried
            
            Returns:
                [Integer] -- Returns the average humidity for the specified date rounded to 1 decimal
        """
        # Execute a query to return the average humidity of the specified date 
        self.__database.execute("SELECT avg(humidity) FROM TEMPERATURE_data WHERE date LIKE ""'%" + date +"'")
        # Store the average humidity row returned into the global variable
        self.__avgHumidity = self.__database.fetchone()
        # Round the humidity at index 0 to 1 decimal point
        self.__avgHumidity = round(self.__avgHumidity[0],1)
        
        # Return the average humidity for the specified date 
        return (self.__avgHumidity)

    def saveChanges(self):
        """
            Saves the changes made to the database.
        """

        # Commit the changes made to connected database
        self.__connection.commit()

    def closeDBConnection(self):
        """
            Closes the connect made to the database.
        """

        # Closes the connection to the database
        self.__connection.close()

    
