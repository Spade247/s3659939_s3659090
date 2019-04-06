from BluetoothManager import BluetoothManager
from DataLogger import DataLogger

class bluetooth:

     def __init__(self):

         self.__bluetooth = BluetoothManager()
         
         self.__dataLogger = DataLogger()
         
         
         self.__currentTemperature = None
         self.__currentHumidity = None

         self.__message =  self.__bluetooth.createMessage(self.__currentTemperature,self.__currentHumidity)

         self.__bluetooth.connectToNearByDevice()

         self.__bluetooth.sendMessage(self.__message)


bluetooth()