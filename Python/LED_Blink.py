import RPi.GPIO as GPIO #libraries stuff

from time import sleep

GPIO.setwarnings(False) #don't warn me i know what i'm doing
GPIO.setmode(GPIO.BCM) #setup
GPIO.setup(17, GPIO.OUT, initial = GPIO.LOW) #first led set up, starts off
GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW) #same

for i in range(0,9): #do this 9 times
    GPIO.output(17, GPIO.HIGH) #turn led 1 on
    GPIO.output(18, GPIO.LOW) #led 2 off
    sleep(.5) #pause for 1/2 second
    GPIO.output(17, GPIO.LOW) #led 1 off
    GPIO.output(18, GPIO.HIGH) #led 2 on
    sleep(.5) #pause for 1/2 second

GPIO.output(18, GPIO.LOW) #turn led 2 off
