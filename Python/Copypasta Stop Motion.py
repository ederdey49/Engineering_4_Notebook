from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Button

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
camera = PiCamera()
frame = 1
toggle = 0

camera.start_preview()

try:
    while True:
        if (GPIO.input(4) and not toggle):
            camera.capture("/home/pi/Documents/Engineering_4_Notebook/Python/Animation/frame%03d.jpg" % frame)
            frame += 1
            toggle = 1
        if (not GPIO.input(4) and toggle):
            toggle = 0
except KeyboardInterrupt:
    camera.stop_preview()
