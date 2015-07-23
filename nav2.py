import RPi.GPIO as io
import time
import subprocess
import threading
import pdb

LEFT=22
RIGHT=24
FORWARD=8
BACK=10
ECHORIGHT = 19
TRIGRIGHT = 21
ECHOLEFT = 38
TRIGLEFT = 40



TurnsMade=0
LeftTurnTime=1.5
RightTurnTime=1.5
LeftSonarData=50
RightSonarData=50
checking = False


io.setmode(io.BOARD)

io.setup(LEFT,io.OUT)
io.setup(RIGHT,io.OUT)
io.setup(FORWARD, io.OUT)
io.setup(BACK, io.OUT)

io.setup(TRIGRIGHT, io.OUT)
io.setup(ECHORIGHT, io.IN)
io.setup(TRIGLEFT, io.OUT)
io.setup(ECHOLEFT, io.IN)


DC=40
pwm = io.PWM(FORWARD, 50)
pwm2 = io.PWM(BACK, 50)



io.output(LEFT, False)
io.output(LEFT, False)
io.output(LEFT, False)
io.output(LEFT, False)

answer=raw_input("Set Path: > ")
nTurns=len(answer)
try:
	pwm.start(DC)
	
	while ( TurnsMade < nTurns) :			
		procL=subprocess.Popen(["sudo" , "python", "sonarTestLeft.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		procR=subprocess.Popen(["sudo" , "python", "sonarTestRight.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


		ansL, stderr = procL.communicate()
		ansR, stderr = procR.communicate()
		#pdb.set_trace()
		LeftSonarData=float(ansL)
		RightSonarData=float(ansR)
		
		log=open("navigate.log", "a")
		
		print 'ansL: %s, ansR: %s' % (str(ansL), str(ansR))
		if (checking== True):
			pwm.start(DC)
		if answer[TurnsMade]=="l":
			if (LeftSonarData > 180): #if hallway, execute turn
				if (checking == False):
					print "checking left"
					checking = True
					pwm.stop()
					pwm2.start(DC)
					time.sleep(0.1)
					pwm2.stop()
					continue
				else:
					checking=False
					print "turning left"

					pwm.stop()
					
					io.output(LEFT, True)
					pwm.start(100)
					
					time.sleep(LeftTurnTime)
					io.output(LEFT, False)	
					
					TurnsMade=TurnsMade+1
				
					pwm.stop()
					pwm.start(DC)
					time.sleep(0.5)
					pwm.stop()
			if (RightSonarData < 80): #if to the right side of halla
				if (checking == True):
					checking = False
				if (RightSonarData < LeftSonarData):
					print "attempting to correct left"
					io.output(LEFT, True)
					time.sleep(.15)
					io.output(LEFT, False)	
			if (LeftSonarData < 80): #if to the left side of hall
				if (checking == True):
					checking = False
				if (LeftSonarData < RightSonarData):
					print "attempting to correct right"
					io.output(RIGHT, True)
					time.sleep(.15)
					io.output(RIGHT, False)	
			if (LeftSonarData >= 60 and RightSonarData >= 60 and RightSonarData <= 180 and checking == True):
				checking = False

		elif answer[TurnsMade]=="r":
			print 'left sonar: %i, right sonar: %i' % (int(LeftSonarData), int(RightSonarData))
			if (RightSonarData > 180):
				if (checking == False):
					print "checking right"
					checking = True
					pwm.stop()
					pwm2.start(DC)
					time.sleep(0.1)
					pwm2.stop()
					continue
				else:
					checking=False
					io.output(RIGHT, True)
					print "turning right"
					pwm.stop()
					#io.output(FORWARD, True)
					io.output(RIGHT, True)
					pwm.start(100)
					time.sleep(RightTurnTime)
					io.output(RIGHT, False)
					TurnsMade=TurnsMade+1
					pwm.stop()
					pwm.start(DC)
					time.sleep(0.5)
					pwm.stop()	
				#io.output(FORWARD, False)
			if (RightSonarData < 80): #if to the right side of hall
				print "correcting left"
				if (checking == True):
					checking = False
				io.output(LEFT, True)
				#io.output(FORWARD, True)
				time.sleep(0.15)
				io.output(LEFT, False)	
				#io.output(FORWARD, False)
			if (LeftSonarData < 80): #if to the left side of hall
				print "correcting right"
				if (checking == True):
					checking = False
				io.output(RIGHT, True)
				#io.output(FORWARD, True)
				time.sleep(0.15)
				io.output(RIGHT, False)	
				#io.output(FORWARD, False)
			if (LeftSonarData >= 60 and RightSonarData >= 60 and RightSonarData <= 180 and checking == True):
				checking = False
		log.close()

except KeyboardInterrupt:
	print "GPIO cleaned"
	io.cleanup()
	pwm.stop()
	try:
		procL.kill()
		procR.kill()
	except:
		pass
