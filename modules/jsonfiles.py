import modules.screen as scr
import json
import os 

BASE = 'data/'
#Checks if json file exists and if it doesn't then creates it
#receive: json file name
def check_json(file : str):
  if not os.path.isfile(BASE+file): #Checks if file exists
    with open(BASE+file, 'w') as create:
      json.dump({}, create, indent = 4) #Creates file

#Read json file and converts it into a python variable
#recive: Json file name
#return: Json file as a python variable
def read_json(file : str) -> dict:
  with open(BASE+file, 'r') as read:
    return json.load(read)

#update json file with new given data
#recive: Json file name, new data
def update_json(file : str, new_data : dict):
  with open(BASE+file, 'w') as update:
    json.dump(new_data, update, indent = 4)