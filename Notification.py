from DatabaseManager import DatabaseManager
from pushbullet import Pushbullet
class Notification:

    def __init__(self,databaseManager):
    
        self.__databaseManager = databaseManager
        self.__pushbullet = Pushbullet("o.mhFygDkFL66fHWqvcLN4S7kW2R0xQaBU")
        self.__push = None
        self.__messageHead = "head"
        self.__messageBody = "body"
    


    def setMessageHead(self,messageHead):
        self.__messageHead = messageHead
    
    
    def setMessageBody(self, messageBody):
        self.__messageBody = messageBody
    
    def sendNotification(self):
        self.__databaseManager.verifyDate()

        if(True):

            self.__push = self.__pushbullet.push_note(self.__messageHead,self.__messageBody)
        else:
            
            pass
    