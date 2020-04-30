import os
import datetime
import time
from pygame import mixer
from mutagen.mp3 import MP3

directory = input('Folder Directory ')
while True:
        currentDT = datetime.datetime.now()
        time_hr = currentDT.strftime("%I %p")
        mp3_to_play = os.path.join(directory, time_hr + '.mp3')
        mixer.init()
        mixer.music.load(mp3_to_play)
        song = MP3(mp3_to_play)
        mixer.music.play()
        if mixer.music.get_busy() == 1:
                time.sleep(song.info.length)
