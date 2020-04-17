import os
import datetime
from playsound import playsound

directory = input('Folder Directory ')
while True:
        currentDT = datetime.datetime.now()
        time_hr = currentDT.strftime("%I %p")
        mp3_to_play = os.path.join(directory, time_hr + '.mp3')
        playsound(mp3_to_play)
