# Oct. 24, 2018
# Python program that flashes an LED strip RED, GREEN, PURPLE and ORANGE for 1 sec. each, with no repeats, on loop for 1 minute.

import RPi.GPIO as GPIO                           
import time                                     
import subprocess
import datetime
import os
import random


# Series of functions that use command-line commands to set the RGB of the LED strip
def purple():
	subprocess.Popen(["pigs","p 27 0"], stdout=subprocess.PIPE) # R
	subprocess.Popen(["pigs","p 17 255"], stdout=subprocess.PIPE) # G
	subprocess.Popen(["pigs","p 22 0"], stdout=subprocess.PIPE) # B

def green():
	subprocess.Popen(["pigs","p 27 255"], stdout=subprocess.PIPE) # R
	subprocess.Popen(["pigs","p 17 0"], stdout=subprocess.PIPE) # G
	subprocess.Popen(["pigs","p 22 255"], stdout=subprocess.PIPE) # B

def red():
	subprocess.Popen(["pigs","p 27 0"], stdout=subprocess.PIPE) # R
	subprocess.Popen(["pigs","p 17 255"], stdout=subprocess.PIPE) # G
	subprocess.Popen(["pigs","p 22 255"], stdout=subprocess.PIPE) # B

def orange():
	subprocess.Popen(["pigs","p 27 0"], stdout=subprocess.PIPE) # R
	subprocess.Popen(["pigs","p 17 175"], stdout=subprocess.PIPE) # G
	subprocess.Popen(["pigs","p 22 255"], stdout=subprocess.PIPE) # B

# Helper function for debugging - sets RBG on LED strip to OFF
def killLights():
	subprocess.Popen(["pigs","p 27 255"], stdout=subprocess.PIPE) # R
	subprocess.Popen(["pigs","p 17 255"], stdout=subprocess.PIPE) # G
	subprocess.Popen(["pigs","p 22 255"], stdout=subprocess.PIPE) # B

i = 0

GPIO.setmode(GPIO.BOARD)                          #Bring up Raspberry PI GPIO pins
pir = 26                                          #Set this value to whichever pin is listening to the sensor
GPIO.setup(pir, GPIO.IN)                          
print "HALLOWEEN LIGHTS - Waiting for sensor to settle"
time.sleep(2)                                     #Give the sensor 2 sec. to come online
print "Detecting motion"
while True:					  #Loop forever
	if GPIO.input(pir):                            #Check pin
      		print "Motion Detected!"
	      	print (datetime.datetime.now())

		for k in range(0,60):
	
			j = 0
	
			while (i == j):
				j = random.randint(0,3)
				
			i = j
			
			if (j == 0):
				purple()
			
			if (j == 1):
				green()
			
			if (j == 2):
				red()
			
			if (j == 3):
				orange()
		
			time.sleep(1)	

			killLights()
	
		# for k

	time.sleep(2)                               #Delay for 2 sec. to avoid false, double detection
	time.sleep(0.1)                              





