#!/usr/bin/env python3
import os
import time
import bluetooth 
from virtual_sense_hat import VirtualSenseHat
from Monitor import Monitor
from Notification import Notification
from DataLogger import DataLogger

class Bluetooth:

        """ 
            This class represents the sending of a message to a connected device
            stating the current temperature and humidity

        """

     def __init__(self):

        """
            On initialisation the Bluetooth class retrieves the current Temperature and Humidity from the DataLogger class
            and sends a notification via Pushbullet with a message stating that a Bluetooth connection has been made aswell
            as the current Temperature and Humidity.
        """
        #declare variables that handle interactions with other classes 
         self.__bluetooth = BluetoothManager()
         self.__dataLogger = DataLogger()
         
        #declare variables that store the current temperature and humidity to 1 decimal point
         self.__currentTemperature = round(self.__dataLogger.getTemperature(),1)
         self.__currentHumidity = round(self.__dataLogger.getHumidity(),1)

        # using the bluetoothManager initialisation to create a message for the current temperature and humidity 
         self.__bluetooth.createMessage(self.__currentTemperature,self.__currentHumidity)
         
        # self.__deviceName = input("Please enter your device' name: ")

        #Hardcode the device that bluetooth will search for
         self.__deviceName = "Yonas"

        #search for the device that needs to be connected once found print on cmd line that it is, if not found continue searching
         self.__bluetooth.connectToNearByDevice(self.__deviceName)

        #once that device has been connected send a pushbullet notifcation with the message
         self.__bluetooth.sendMessage()

class BluetoothManager:
    """ 
         This class represents a single interaction with a bluetooth device.
    """

    def __init__(self):

        """
            On initialisation the BluetoothManager class retrieves the temperature ranges from the Monitor Class
        """

        #declare variables that handle interactions with other classes 
        self.__monitor = Monitor()
        self.__notifier = Notification()

        #declare variables that will store the head and message that will be sent via pushbullet
        self.__head = None
        self.__message = None

        #declare variables the store the ranges from the Monitor class using the classes methods 
        self.__minTemperature = self.__monitor.getMinTemperature()
        self.__maxTemperature = self.__monitor.getMaxTemperature()
        self.__minHumidity = self.__monitor.getMinHumidity()
        self.__maxHumidity = self.__monitor.getMaxHumidity()
    
    def connectToNearByDevice(self,deviceName = "Yonas"): 

        """
            connects the Raspberry Pi to the device that was passed through the deviceName parameter
            Once connected returns a string stating that a connection was made with the device on the command line
        """

          #search for the device until it has been found
          while True:

            #declare variables that store the the connected device's mac address and the current time
               connectedDeviceMACAddress = None
               dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
               print("\nCurrently: {}".format(dt))

            #make the raspberry pi sleep for 3 seconds to recalibrate its sensors
               time.sleep(3) 
            
            #declare a variable that will store an array of all current nearby devices
               nearby_devices = bluetooth.discover_devices()

            #iterate through the list of devices 
               for mac_address in nearby_devices:

                #if the device at this index has the same name as the device attempting to be connected do the following
                    if deviceName == bluetooth.lookup_name(mac_address, timeout = 5):

                        # store the devices mac address to this variable
                         connectedDeviceMACAddress = mac_address

                        # stop iterating through the list of devices because the devices mac address has been found
                         break

                #if the variable connectedDeviceMACAddress contains a MAC address do the following
               if connectedDeviceMACAddress is not None:

                    #store the head of the message with the device's name
                    self.__head = "Connected to " + str(deviceName) + " via Bluetooth."

                    #print into the command line that the device has been connected via bluetooth 
                    print("\nConnected to {} Via Bluetooth! ({}) has the MAC address: {}\n".format( deviceName,deviceName, connectedDeviceMACAddress))
                    
                    #exit the search for the device
                    break 

                # if the variable connectedDeviceMACAddress does not contain a mac address  do the following 
               else:

                    #print that the device that is being searched for can not be found  
                    print("\nCould not find target device nearby...")
          
    
    def createMessage(self,currentTemperature,currentHumidity):
    """
            Takes in the current temperature and humidity as parameters and constructs a message that is stored 
            in the global variable __message 
    """
        #store the first values of the message to be the current temperature and humidity
        self.__message = "current Temperature: "+str(currentTemperature)+"*C\nCurrent Humidity: "+str(currentHumidity)+"%\n"
        
        #if statements to append the __message variable when the temperature and humidity arent within the specified range
        if currentTemperature < self.__minTemperature:
             self.__message += str(round(self.__minTemperature - currentTemperature,1))+"*C below minimum temperature.\n"
        
        if currentTemperature > self.__maxTemperature:
             self.__message += str(round(currentTemperature - self.__maxTemperature,1))+"*C above maximum temperature.\n"
        
        if currentHumidity < self.__minHumidity:
             self.__message += str(round(self.__minHumidity - currentHumidity,1))+"% below minimum humidity.\n"

        if currentHumidity > self.__maxHumidity:
             self.__message += str(round(currentHumidity - self.__maxHumidity,1))+"% above maximum humidity.\n"
        
    def sendMessage(self):
    """
            Sends a meessage via Pushbullet with the values of the global variable __head and __message
            Once sent prints a string on the commandline of the contents of the message being sent 
    """
        #set the head and body of the notification that is to be sent then send it 
          self.__notifier.setMessageHead(self.__head)
          self.__notifier.setMessageBody(self.__message)
          self.__notifier.sendMessage()
        
        #print the contents of the message sent on the command line 
          print("*********************************")
          print("*       NOTIFICATION SENT       *")
          print("*********************************")
          print(str(self.__head))
          print("\n"+str(self.__message))
          
#Initialise the Bluetooth class
Bluetooth()