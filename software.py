import pyttsx3
import os

pyttsx3.speak("welocome my tool")

print()
print('Press:1 to open Notepad')
print('Press:2 to open Window Media Player')
print()

print("enter ur choice of:" , end='')

x = input()
print()
#os.system(x)

if int(x) == 1 :
  os.system("Notepad")

elif int(x) == 2 :
  os.system("Wmplayer")

else:
  print("Does't Support")