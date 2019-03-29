import Monitor as mon
import Database as db
import Notification as notif

#Creates the config file with the ranges if it hasnt already been created
mon.create_config_file()

#store the config details on a dictionary
config = mon.get_config_file()

print(config)




