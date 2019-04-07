from Monitor import Monitor
from Notification import Notification

class BluetoothManager:

    def __init__(self):

        self.__monitor = Monitor()
        self.__notifier = Notification()

        self.__connectedDevice = None
        self.__bluetooth = None
        
        self.__head = "Connected to " + str(self.__connectedDevice) + " via Bluetooth."
        self.__message = None

        self.__minTemperature = self.__monitor.getMinTemperature()
        self.__maxTemperature = self.__monitor.getMaxTemperature()
        self.__minHumidity = self.__monitor.getMinHumidity()
        self.__maxHumidity = self.__monitor.getMaxHumidity()
        
    
    def connectToNearByDevice(self,deviceName = "Yonas"):
            self.__connectedDevice = deviceName
            self.__bluetooth = "connect to specific device"
    
    def createMessage(self,currentTemperature,currentHumidity):

        self.__message = "current Temperature: "+str(currentTemperature)+"\nCurrent Humidity: "+str(currentHumidity)+"\n"

        if currentTemperature < self.__minTemperature:
             self.__message += str(round(self.__minTemperature - currentTemperature,1))+"*C below minimum temperature.\n"
        
        if currentTemperature > self.__maxTemperature:
             self.__message += str(round(currentTemperature - self.__maxTemperature,1))+"*C above maximum temperature.\n"
        
        if currentHumidity < self.__minHumidity:
             self.__message += str(round(self.__minHumidity - currentHumidity,1))+"% below minimum humidity.\n"

        if currentHumidity > self.__maxHumidity:
             self.__message += str(round(currentHumidity - self.__maxHumidity,1))+"% above maximum humidity.\n"
        
    def sendMessage(self):
          self.__notifier.setMessageHead = self.__head
          self.__notifier.setMessageBody = self.__message
          self.__notifier.sendMessage()
          



