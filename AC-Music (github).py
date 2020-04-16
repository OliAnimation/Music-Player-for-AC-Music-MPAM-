import datetime
from playsound import playsound
currentDT = datetime.datetime.now()
time_hr = currentDT.strftime("%I %p")
while True:
	time_hr = currentDT.strftime("%I %p")
	if time_hr == '12 AM' :
		playsound("/home/AC Music/12 AM.mp3")
	elif time_hr == '01 AM' :
		playsound("/home/AC Music/01 AM.mp3")
	elif time_hr == '02 AM' :
		playsound("/home/AC Music/02 AM.mp3")
	elif time_hr == '03 AM' :
		playsound("/home/AC Music/03 AM.mp3")
	elif time_hr == '04 AM' :
		playsound("/home/AC Music/04 AM.mp3")
	elif time_hr == '05 AM' :
		playsound("/home/AC Music/05 AM.mp3")
	elif time_hr == '06 AM' :
		playsound("/home/AC Music/06 AM.mp3")
	elif time_hr == '07 AM' :
		playsound("/home/AC Music/O7 AM.mp3")
	elif time_hr == '08 AM' :
		playsound("/home/AC Music/08 AM.mp3")
	elif time_hr == '09 AM' :
		playsound("/home/AC Music/09 AM.mp3")
	elif time_hr == '10 AM' :
		playsound("/home/AC Music/10 AM.mp3")
	elif time_hr == '11 AM' :
		playsound("/home/AC Music/11 AM.mp3")
	elif time_hr == '12 PM' :
		playsound("/home/AC Music/12 PM.mp3")
	elif time_hr == '01 PM' :
		playsound("/home/AC Music/01 PM.mp3")
	elif time_hr == '02 PM' :
		playsound("/home/AC Music/02 PM.mp3")
	elif time_hr == '03 PM' :
		playsound("/home/AC Music/03 PM.mp3")
	elif time_hr == '04 PM' :
		playsound("/home/AC Music/04 PM.mp3")
	elif time_hr == '05 PM' :
		playsound("/home/AC Music/05 PM.mp3")
	elif time_hr == '06 PM' :
		playsound("/home/AC Music/06 PM.mp3")
	elif time_hr == '07 PM' :
		playsound("/home/AC Music/07 PM.mp3")
	elif time_hr == '08 PM' :
		playsound("/home/AC Music/08 PM.mp3")
	elif time_hr == '09 PM' :
		playsound("/home/AC Music/09 PM.mp3")
	elif time_hr == '10 PM' :
                playsound("/home/AC Music/10 PM.mp3")
	elif time_hr == '11 PM' :
                playsound("/home/AC Music/11 PM.mp3")
