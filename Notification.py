# Import relevant modules and classes to be used by the program
from DatabaseManager import DatabaseManager
from pushbullet import Pushbullet

class Notification:
    """
        This class represents the sending of Notification 
    
    """
    def __init__(self,databaseManager = None):
        """
            On initialisation the Notification class establishes a connection to PushBullet 
            and instantiates the DatabaseManager that was passed through the parameter
        
        Arguments:
            databaseManager {DatabaseManager()} -- A DatabaseManager instance so that has access to the database
            (default: {None}) -- If no DatabaseManager is passed through instantiate a new DatabaseManager
        """

        # declare variables
        self.__databaseManager = databaseManager
        self.__pushbullet = Pushbullet("o.mhFygDkFL66fHWqvcLN4S7kW2R0xQaBU")
        self.__push = None
        self.__messageHead = "head"
        self.__messageBody = "body"
    


    def setMessageHead(self,messageHead):
        """
        Sets the message head to be sent 
        
        Arguments:
            messageHead {String} -- A String containing the message head to be sent
        """

        # store the message head to be sent 
        self.__messageHead = messageHead
    
    
    def setMessageBody(self, messageBody):
        """
        Sets the message body to be sent 
        
        Arguments:
            messageBody {String} -- A String containing the message body to be sent
        """

        # store the message body to be sent
        self.__messageBody = messageBody
    
    def sendNotification(self):
        """
            Send notification that needs to be sent once a day
        """

        self.__databaseManager.verifyDate()

        if(self.__databaseManager.verifyDate()):

            self.__push = self.__pushbullet.push_note(self.__messageHead,self.__messageBody)
        else:
            
            pass

    def sendMessage(self):
        """
            Send Message once a bluetooth device is connected 
        """
        
        self.__push = self.__pushbullet.push_note(self.__messageHead,self.__messageBody)
