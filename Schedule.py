#!/usr/bin/env python3
from crontab import CronTab

def createSchedule(minute):
    # Init cron.
    cron = CronTab(user = "pi")
    cron.remove_all()



    # Add new cron job.
    job = cron.new(command = "cd /home/pi/Desktop/PIoT/s3659939_s3659090 && /home/pi/Desktop/PIoT/s3659939_s3659090/monitorAndNotify.py")

    # Job settings.
    job.minute.every(minute)
    cron.write()