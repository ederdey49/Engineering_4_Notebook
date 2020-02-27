import RPi.GPIO as GPIO #importing libraries

from time import sleep

GPIO.setwarnings(False) #stop warning us it's fine
GPIO.setmode(GPIO.BCM) #setup of breadboard pins
GPIO.setup(17, GPIO.OUT, initial = GPIO.LOW) #set up alarm, intitially off
GPIO.setup(18, GPIO.IN) #set up switch so that pi can read input from it

while(True):
    switch = GPIO.input(18) #switch reads input from switch

    if(switch): #if switch is on
        GPIO.output(17, GPIO.HIGH) #turn on alarm
    else: #else
        GPIO.output(17, GPIO.LOW) #turn off alarm
