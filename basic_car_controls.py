#operates left/right/forward/backward on a by manual input basis

import RPi.GPIO as io
import time
import subprocess

LEFT=24
RIGHT=22
FORWARD=10
BACK=8

io.setmode(io.BOARD)

io.setup(LEFT,io.OUT)
io.setup(RIGHT,io.OUT)
io.setup(FORWARD, io.OUT)
io.setup(BACK, io.OUT)

io.output(LEFT, False)
io.output(LEFT, False)
io.output(LEFT, False)
io.output(LEFT, False)

proc=subprocess.Popen(["sudo" , "python", "sonarTestLeft.py"])
proc=subprocess.Popen(["sudo" , "python", "sonarTestRight.py"])

try:
	while 1:
		answer=raw_input("l/r/f/b > ")
		if answer=="l":
			timeToTurn=raw_input("Time? > ")
			io.output(LEFT, True)
			io.output(FORWARD, True)
			time.sleep(float(timeToTurn))
			io.output(LEFT, False)
			io.output(FORWARD, False)
		if answer=="r":
			timeToTurn=raw_input("Time? > ")
			io.output(RIGHT, True)
			io.output(FORWARD, True)
			time.sleep(float(timeToTurn))
			io.output(RIGHT, False)	
			io.output(FORWARD, False)
		if answer=="f":
			start = time.time()
			while (time.time() - start < 5):
				io.output(FORWARD, True)
				time.sleep(.01)
				io.output(FORWARD, False)
				time.sleep(.01)
		if answer=="b":
			io.output(BACK, True)
			time.sleep(3)
			io.output(BACK, False)
		
except KeyboardInterrupt:
	print "GPIO cleaned"
	io.cleanup()


