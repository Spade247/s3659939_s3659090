from Report import Report

class createReport:

    def __init__(self):

        self.__report = Report()
        self.__report.writeIntoCSV()



createReport()