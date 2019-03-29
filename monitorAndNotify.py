#!/usr/bin/env python3
import Monitor as mon
import Database as db
import time 
from virtual_sense_hat import VirtualSenseHat as vsh
import Notification as notif

#defaulted to 1 record per minute
freq = 1
#Creates the config file with the ranges if it hasnt already been created
mon.create_config_file()

#store the config details on a dictionary
config = mon.get_config_file()

#main function 
def main():
    sense = vsh.getSenseHat()

    #the range is set to frequency of the records being created (1 per minute depending on the cronjob)
    for i in range(0,freq):
        db.createDB()
        db.getSenseHatData()
        time.sleep(freq)
    db.displayData()
    sense.show_message("Recorded Data!",text_colour = [0,255,0],scroll_speed=0.05)

#execute main program
main()






