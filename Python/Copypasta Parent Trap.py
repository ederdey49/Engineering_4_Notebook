from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
camera = PiCamera()

while(True):
    now = datetime.now()
    pir = GPIO.input(17)
    filename =  '{0:%H}:{0:%M}:{0:%S} {0:%m}-{0:%d}'.format(now)

    if(pir):
        camera.start_preview()
        camera.start_recording('/home/pi/Desktop/parent_video' + filename + '.h264')
        sleep(10)
        camera.stop_recording()
        camera.stop_preview()
    
        
