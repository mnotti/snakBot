import RPi.GPIO as io
import time
import subprocess

LEFT=22
RIGHT=24
FORWARD=8
BACK=10

io.setmode(io.BOARD)

io.setup(LEFT,io.OUT)
io.setup(RIGHT,io.OUT)
io.setup(FORWARD, io.OUT)
io.setup(BACK, io.OUT)

io.output(LEFT, False)
io.output(LEFT, False)
io.output(LEFT, False)
io.output(LEFT, False)


def forward(time):
	io.output(FORWARD, True)
	time.sleep(time)
	io.output(FOWARD, False)
def back(time):
	io.output(BACK, True)
	time.sleep(time):
	io.output(BACK, False)
def left(time):
	io.output(LEFT, True)
	io.output(FORWARD, True)
	time.sleep(time)
	io.output(LEFT, False)
	io.output(FORWARD, False)
def right(time):	
	io.output(LEFT, True)
	io.output(FORWARD, True)
	time.sleep(time)
	io.output(LEFT, False)
	io.output(FORWARD, False)



