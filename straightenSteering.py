import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

timeToCorrect = raw_input("Time > ")
floatTime = float(timeToCorrect)

GPIO.output(24, False)
GPIO.output(22, True)
sleep(3)

GPIO.output(22, False)
GPIO.output(24, True)

sleep(floatTime) #time to correct to straight
GPIO.output(24, False)



