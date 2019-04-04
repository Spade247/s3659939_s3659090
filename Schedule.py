#!/usr/bin/env python3
from crontab import CronTab
import os

class Schedule:

    def __init__(self):
        self.__directorypath = os.path.abspath("")
        self.__filepath = os.path.abspath("monitorAndNotify.py")
        self.__cron = CronTab(user = "pi")
        self.__job = None
        
    
    def createSchedule(self):
        self.__cron.remove_all()
        # self.__job = self.__cron.new(command = "cd "+ str(self.__directorypath) + " && " + str(self.__filepath) )
        self.__job = self.__cron.new(command = "/usr/bin/env python3 " + str(self.__filepath) )
        self.__job.minute.every(1)
        self.__cron.write()
 

