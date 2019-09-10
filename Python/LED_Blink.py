import RPi.GPIO as GPIO

from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW)

for i in range(0,9):
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    sleep(.5)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    sleep(.5)

GPIO.output(18, GPIO.LOW)
