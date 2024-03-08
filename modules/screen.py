import os 
import sys

#Clean screen based on the operative system
def clean():
  if sys.platform == 'windows': #if operative system is windows
    os.system('cls')
  elif sys.platform == 'linux': #If operative system is linux
    os.system('clear')
  else:
    os.system('cls')

#Pause screen based on the operative system
def pause():
  if sys.platform == 'windows': #if operative system is windows
    os.system('pause')
  elif sys.platform == 'linux': #If operative system is linux
    input('Press any key to continue . . .')

