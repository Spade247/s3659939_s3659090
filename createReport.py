"""
Authors: Yonas Sisay s3659939 
         Amrit Mundi s3659990
"""
# Import relevant modules and classes to be used by the program
from ReportManager import ReportManager
from Report import Report

class createReport:
    """
        This class represents the creation of a csv file

    """

    def __init__(self):
        """
            On initialisation the createReport class retrieves an instance of the ReportManager class and creates a report.csv file
        """

        #create an instance of the ReportManager
        self.__reportManager = ReportManager()

        #create a report.csv file by calling the functions of the ReportManager
        self.__reportManager.writeIntoCSV("report.csv")
        # self.__report = Report()
        # self.__report.writeIntoCSV()


#Initialise the createReport class
createReport()