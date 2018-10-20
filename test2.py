import os

for root, dirs, files in os.walk("/home/pi/motionSensor/SpookySounds"):
	for filename in files:
		print (filename)
