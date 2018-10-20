#!/bin/bash

sudo pigpiod &
python /home/pi/halloweenDisplay/halloween_sounds.py &> /home/pi/halloweenDisplay/log.out
