import RPi.GPIO as io
import time

ECHO = 38
TRIG = 40

io.setmode(io.BOARD)
io.setup(TRIG, io.OUT)
io.setup(ECHO, io.IN)



f=open("sonar_test_data_right.txt", "w")

try:
#	while 1:
	io.output(TRIG, False)
	time.sleep(0.01)

	io.output(TRIG, True)
	time.sleep(.00001)
	io.output(TRIG, False)

	pulse_start = 0
	pulse_end = 0

	while io.input(ECHO) == 0 :
		pulse_start = time.time()

	while io.input(ECHO) == 1 :
		pulse_end = time.time()

	pulse_dur = pulse_end - pulse_start


	distance = pulse_dur * 17150 
	distance = round(distance, 2)
	print distance
	
	sonar_dist = str(distance) + " cm\n"
	f.write(sonar_dist)
except KeyboardInterrupt:
	f.close()
