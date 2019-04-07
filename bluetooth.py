from BluetoothManager import BluetoothManager
from DataLogger import DataLogger

class bluetooth:

     def __init__(self):

         self.__bluetooth = BluetoothManager()
         
         self.__dataLogger = DataLogger()
         
         
         self.__currentTemperature = self.__dataLogger.getTemperature()
         self.__currentHumidity = self.__dataLogger.getHumidity()

         self.__bluetooth.createMessage(self.__currentTemperature,self.__currentHumidity)

         self.__bluetooth.search("Yonas","Yonas")
         self.__bluetooth.connectToNearByDevice()

         self.__bluetooth.sendMessage()


bluetooth()