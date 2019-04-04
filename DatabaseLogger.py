import time
import datetime 
import sqlite3 
from virtual_sense_hat import VirtualSenseHat as vsh

class DatabaseLogger:

                def __init__(self):


                        #get data from the sensehat
                        def getSenseHatData():
                                sense = vsh.getSenseHat()
                                temp = sense.get_temperature()
                                humidity = sense.get_humidity()
                                if temp or humidity is not None:
                                        temp = round(temp,1)
                                        humidity = round(humidity,1)
                                        (temp,humidity)