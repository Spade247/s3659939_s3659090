import Monitor as mon
import Database as db
import Notification as notif

#defaulted to 1 second but should be 60 seconds
freq = 1
#Creates the config file with the ranges if it hasnt already been created
mon.create_config_file()

#store the config details on a dictionary
config = mon.get_config_file()

#main function 
def main():
    for i in range(0,60):
        db.createDB()
        db.getSenseHatData()
        db.time.sleep(freq)
    db.displayData()

#execute main program
main()






