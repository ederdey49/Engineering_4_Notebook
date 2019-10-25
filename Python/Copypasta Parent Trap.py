from gpiozero import MotionSensor #importing necessary libraries
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setwarnings(False) #don't warn us every time we try to run this
GPIO.setmode(GPIO.BCM) #setup of GPIO
GPIO.setup(17, GPIO.IN) #take input from pin 17
camera = PiCamera() #making a camera object

while(True):
    now = datetime.now() #sets the time
    pir = GPIO.input(17) #the pir sensor is at pin 17
    filename =  '{0:%H}:{0:%M}:{0:%S} {0:%m}-{0:%d}'.format(now) #date and time for the name of the file

    if(pir): #if the pir sensor sees motion
        camera.start_preview() #show what the camera's seeing on the computer
        camera.start_recording('/home/pi/Desktop/parent_video' + filename + '.h264') #saves the file to the desktop with the name parent_video and then the date and time
        sleep(10) #pauses the program for 10 seconds so that it continues recording
        camera.stop_recording() #stops the recording
        camera.stop_preview() #stops the computer view of what the camera is seeing
    
        
