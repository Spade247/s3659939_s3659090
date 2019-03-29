import json 

config = {
            "min_temperature":20,
            "max_temperature":30,
            "min_humdity":50,
            "max_humidity":60,
            }
json_string = json.dumps(config)

print(json_string)