# Oct. 22, 2018
# Python program that plays random MP3 when IR sensor is triggered
import RPi.GPIO as GPIO                           
import time                                      
import datetime
import  subprocess
import os
import random

mp3Files=[]

i = 0

for root, dirs, files in os.walk("/home/pi/halloweenDisplay/SpookySounds"):
	for filename in files:
		mp3Files.append(filename)
		i=i+1

GPIO.setmode(GPIO.BOARD)                          #Bring up GPIO pins
pir = 26                                          #Set to whichever pin is listening to the IR sensor
GPIO.setup(pir, GPIO.IN)                          
print "HALLOWEEN MUSIC - Waiting for sensor to settle"
time.sleep(2)                                     #Give the sensor 2 seconds to warm up
print "Detecting motion"
while True:					  #Loop forever
   if GPIO.input(pir):                             
      print "Motion Detected!"
      print (datetime.datetime.now())

      j = random.randint(0,i-1)

      print "Playing: " + "/home/pi/halloweenDisplay/SpookySounds/"+mp3Files[j]

      p = subprocess.Popen(["omxplayer", "/home/pi/halloweenDisplay/SpookySounds/"+mp3Files[j]], stdout=subprocess.PIPE)

      print p.communicate()

      time.sleep(2)                               #Delay to avoid false, double detection
   time.sleep(0.1)                               

