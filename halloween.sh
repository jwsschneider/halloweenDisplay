# Oct. 25,2018
# Bash script that brings up the LED daemon and launches both the lights and sounds Python programs to run in the background. This script is called from the root's /etc/init.d/rc.local script at startup.
#!/bin/bash

# Launch LED daemon
sudo pigpiod &

# Launch Python programs
python /home/pi/halloweenDisplay/halloween_sounds.py &> /home/pi/halloweenDisplay/log.out
