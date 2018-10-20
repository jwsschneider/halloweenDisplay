import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
import subprocess
import datetime
import os
import random



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

def killLights():
	subprocess.Popen(["pigs","p 27 255"], stdout=subprocess.PIPE) # R
	subprocess.Popen(["pigs","p 17 255"], stdout=subprocess.PIPE) # G
	subprocess.Popen(["pigs","p 22 255"], stdout=subprocess.PIPE) # B

i = 0

GPIO.setmode(GPIO.BOARD)                          #Set GPIO pin numbering
pir = 26                                          #Associate pin 26 to pir
GPIO.setup(pir, GPIO.IN)                          #Set pin as GPIO in 
print "HALLOWEEN LIGHTS - Waiting for sensor to settle"
time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate
print "Detecting motion"
while True:
	if GPIO.input(pir):                            #Check whether pir is HIGH
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

	time.sleep(2)                               #D1- Delay to avoid multiple detection
	time.sleep(0.1)                                #While loop delay should be less than detection(hardware) delay





