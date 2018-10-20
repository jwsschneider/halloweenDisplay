import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
import datetime
import  subprocess
import os
import random

mp3Files=[]

i = 0

for root, dirs, files in os.walk("/home/pi/motionSensor/SpookySounds"):
	for filename in files:
		mp3Files.append(filename)
		i=i+1

GPIO.setmode(GPIO.BOARD)                          #Set GPIO pin numbering
pir = 26                                          #Associate pin 26 to pir
GPIO.setup(pir, GPIO.IN)                          #Set pin as GPIO in 
print "HALLOWEEN MUSIC - Waiting for sensor to settle"
time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate
print "Detecting motion"
while True:
   if GPIO.input(pir):                            #Check whether pir is HIGH
      print "Motion Detected!"
      print (datetime.datetime.now())

      j = random.randint(0,i-1)

      print "Playing: " + "/home/pi/motionSensor/SpookySounds/"+mp3Files[j]

      p = subprocess.Popen(["omxplayer", "/home/pi/motionSensor/SpookySounds/"+mp3Files[j]], stdout=subprocess.PIPE)

      print p.communicate()

      time.sleep(2)                               #D1- Delay to avoid multiple detection
   time.sleep(0.1)                                #While loop delay should be less than detection(hardware) delay

