import RPi.GPIO as GPIO

from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(18, GPIO.IN)

while(True):
    switch = GPIO.input(18)

    if(switch):
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
