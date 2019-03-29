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

#A method that returns the config.json file into a Dictionary
def get_config_file():
    with open("config.json","r") as json_file:
        config_file = json.load(json_file)
    return config_file

#Test DATA
create_config_file()
d1 = get_config_file()
print(d1)




