#!/usr/bin/env python3
import os
import time
import bluetooth 
from virtual_sense_hat import VirtualSenseHat
from Monitor import Monitor
from Notification import Notification

class BluetoothManager:

    def __init__(self):

        self.__monitor = Monitor()
        self.__notifier = Notification()

        self.__connectedDevice = None
        self.__bluetooth = bluetooth()
        
        self.__head = None
        self.__message = None

        self.__minTemperature = self.__monitor.getMinTemperature()
        self.__maxTemperature = self.__monitor.getMaxTemperature()
        self.__minHumidity = self.__monitor.getMinHumidity()
        self.__maxHumidity = self.__monitor.getMaxHumidity()
        
    def search(self,user_name, device_name):
          while True:
               device_address = None
               dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
               print("\nCurrently: {}".format(dt))
               time.sleep(3) # Sleep three seconds.
               nearby_devices = self.__bluetooth.discover_devices()

               for mac_address in nearby_devices:
                    if device_name == self.__bluetooth.lookup_name(mac_address, timeout = 5):
                         device_address = mac_address
                         break
               if device_address is not None:
                    print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
                    sense = VirtualSenseHat.getSenseHat()
                    temp = round(sense.get_temperature(), 1)
                    sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed = 0.05)
                    break 
               else:
                    print("Could not find target device nearby...")

    def connectToNearByDevice(self,deviceName = "Yonas"): 
          self.__head = "Connected to " + str(deviceName) + " via Bluetooth."
          self.__bluetooth = "connect to specific device"
    
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
          



