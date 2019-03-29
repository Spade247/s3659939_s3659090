import time 
import sqlite3 
from virtual_sense_hat import VirtualSenseHat as vsh

dbName = "sensehat.db"

#Create the database if it hasnt been created already
def createDB():
    connection = sqlite3.connect(dbName)
    with connection:
         cursor = connection.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS TEMPERATURE_data(time_stamp DATETIME, temperature NUMERIC, humidity NUMERIC)")
    

#get data from the sensehat
def getSenseHatData():
    sense = vsh.getSenseHat()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    if temp or humidity is not None:
        temp = round(temp,1)
        humidity = round(humidity,1)
        recordData(temp,humidity)

#log sensor data on database
def recordData(temp,humidity):
    connection = sqlite3.connect(dbName)
    cursor = connection.cursor()
    insertQuery = "INSERT INTO TEMPERATURE_data values(datetime('now'),"+str(temp)+","+str(humidity)+")"
    cursor.execute(insertQuery)
    connection.commit()
    connection.close()

#display database content
def displayData():
    connection = sqlite3.connect(dbName)
    cursor = connection.cursor()
    print("\nRecords Within "+dbName+" Database:\n")
    selectAllQuery = "SELECT * FROM TEMPERATURE_data"
    for row in cursor.execute(selectAllQuery):
        print(row)
    connection.close()



