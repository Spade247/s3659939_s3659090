#!/usr/bin/env python3
import os
import time
import bluetooth 
from virtual_sense_hat import VirtualSenseHat
from Monitor import Monitor
from Notification import Notification
from DataLogger import DataLogger

class Bluetooth:

     def __init__(self):

         self.__bluetooth = BluetoothManager()
         
         self.__dataLogger = DataLogger()
         
         
         self.__currentTemperature = round(self.__dataLogger.getTemperature(),1)
         self.__currentHumidity = round(self.__dataLogger.getHumidity(),1)

         self.__bluetooth.createMessage(self.__currentTemperature,self.__currentHumidity)
         
            # self.__deviceName = input("Please enter your device' name: ")
         self.__deviceName = "Yonas"

         self.__bluetooth.connectToNearByDevice(self.__deviceName)

         self.__bluetooth.sendMessage()

class BluetoothManager:

    def __init__(self):

        self.__monitor = Monitor()
        self.__notifier = Notification()

        self.__connectedDevice = None
        self.__bluetooth = None
        
        self.__head = None
        self.__message = None

        self.__minTemperature = self.__monitor.getMinTemperature()
        self.__maxTemperature = self.__monitor.getMaxTemperature()
        self.__minHumidity = self.__monitor.getMinHumidity()
        self.__maxHumidity = self.__monitor.getMaxHumidity()
    
    def connectToNearByDevice(self,deviceName = "Yonas"): 

          while True:
               connectedDeviceMACAddress = None
               dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
               print("\nCurrently: {}".format(dt))

               time.sleep(3) 
               
               nearby_devices = bluetooth.discover_devices()

               for mac_address in nearby_devices:
                    if deviceName == bluetooth.lookup_name(mac_address, timeout = 5):
                         connectedDeviceMACAddress = mac_address
                         break

               if connectedDeviceMACAddress is not None:
                    self.__head = "Connected to " + str(deviceName) + " via Bluetooth."

                    print("\nConnected to {} Via Bluetooth! ({}) has the MAC address: {}\n".format( deviceName,deviceName, connectedDeviceMACAddress))
                    
                    break 

               else:
                    print("\nCould not find target device nearby...")
          
    
    def createMessage(self,currentTemperature,currentHumidity):

        self.__message = "current Temperature: "+str(currentTemperature)+"*C\nCurrent Humidity: "+str(currentHumidity)+"%\n"

        if currentTemperature < self.__minTemperature:
             self.__message += str(round(self.__minTemperature - currentTemperature,1))+"*C below minimum temperature.\n"
        
        if currentTemperature > self.__maxTemperature:
             self.__message += str(round(currentTemperature - self.__maxTemperature,1))+"*C above maximum temperature.\n"
        
        if currentHumidity < self.__minHumidity:
             self.__message += str(round(self.__minHumidity - currentHumidity,1))+"% below minimum humidity.\n"

        if currentHumidity > self.__maxHumidity:
             self.__message += str(round(currentHumidity - self.__maxHumidity,1))+"% above maximum humidity.\n"
        
    def sendMessage(self):
          self.__notifier.setMessageHead(self.__head)
          self.__notifier.setMessageBody(self.__message)
          self.__notifier.sendMessage()

          print("*********************************")
          print("*       NOTIFICATION SENT       *")
          print("*********************************")
          print(str(self.__head))
          print("\n"+str(self.__message))
          

Bluetooth()