# Oct. 23, 2018
# Simple Python program that sets every LED on the strip to "OFF." Useful for debugging.

import subprocess
import os

subprocess.Popen(["pigs","p 27 255"], stdout=subprocess.PIPE) # R
subprocess.Popen(["pigs","p 17 255"], stdout=subprocess.PIPE) # G
subprocess.Popen(["pigs","p 22 255"], stdout=subprocess.PIPE) # B
