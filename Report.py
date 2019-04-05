from Database import Database 
from datetime import date
import csv

class Report:

    def __init__(self):
        self.__database = Database()

        self.__arrayOfDates = self.__database.getDates()
        self.__avgTemperature = None
        self.__avgHumidity = None
        

    
    def writeIntoCSV(self):
        with open("report.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Temp","Humidity"])

            for date in self.__arrayOfDates:
                self.__avgTemperature = self.__database.getAvgTemperature(str(date))
                self.__avgHumidity = self.__database.getAvgHumidity(str(date))
                writer.writerow([str(date), str(self.__avgTemperature),str(self.__avgHumidity)])






