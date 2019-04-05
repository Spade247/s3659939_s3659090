from Monitor import Monitor
from Report import Report
import csv 

class ReportManager:
    
    def __init__(self):

        self.__report = Report()
        self.__csvFile = None
        self.__arrayOfDates = self.__report.getDates()
        self.__avgTemperature = None
        self.__avgHumidity = None
        self.__status = None
        self.__message = None
    
    def writeIntoCSV(self,csvFile = 'report.csv'):
        self.__csvFile = csvFile
        with open(self.__csvFile, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date","Status"])

            # print("array of dates: ",self.__arrayOfDates)

            for date in self.__arrayOfDates:

                self.__avgTemperature = self.__report.getAvgTemperature(date)
                self.__avgHumidity = self.__report.getAvgHumidity(date)
                self.__status = self.__report.getStatus()
                self.__message = self.__report.getMessage(self.__status)
                # print("average temperature for {}  : {} ".format(date,self.__avgTemperature))
                # print("average humidity for {} : {}".format(date,self.__avgHumidity))
                # print("message: {}".format(self.__message))

                
                writer.writerow([str(date),str(self.__message)])
    
    
