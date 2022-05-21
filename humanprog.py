import pyttsx3
import os

#pyttsx3.speak("welocome my tool")


print("chat with me with your requirements:" , end='')

p = input()

#print(p)
#os.system(p)

if ("run" in p) and (("player" in p) or ("media" in p)):
  os.system("wmplayer")

elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
  os.system("notepad")

else:
  print("Does't Support")