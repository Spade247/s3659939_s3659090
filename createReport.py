from ReportManager import ReportManager
from Report import Report


class createReport:

    def __init__(self):

        self.__reportManager = ReportManager()
        self.__reportManager.writeIntoCSV("report.csv")
        # self.__report = Report()
        # self.__report.writeIntoCSV()



createReport()