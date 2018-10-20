import subprocess
import os

subprocess.Popen(["pigs","p 27 255"], stdout=subprocess.PIPE) # R
subprocess.Popen(["pigs","p 17 255"], stdout=subprocess.PIPE) # G
subprocess.Popen(["pigs","p 22 255"], stdout=subprocess.PIPE) # B