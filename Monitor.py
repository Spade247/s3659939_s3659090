import json 

#Created A Dictionary to store the temperature and humidity ranges
config = {
            "min_temperature":20,
            "max_temperature":30,
            "min_humidty":50,
            "max_humidty":60,
            }

#A method that creates the config.json file with the ranges 
def create_config_file():
    with open("config.json","w") as json_file:
        json.dump(config,json_file,indent = 4)





