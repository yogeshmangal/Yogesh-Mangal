from playsound import playsound
import datetime
alarmHr=int(input("At which hour you want to wake up? "))
alarmMin=int(input("At which min. you want to wake up? "))
ampm=input("am or pm ? ")
if(ampm=='pm'):
    alarmHr=alarmHr+12

while(1):
    if(alarmHr==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute):
        print("Wake up")
        playsound('beep.mp3')    #Here beep is the name of ringtone…
        break
