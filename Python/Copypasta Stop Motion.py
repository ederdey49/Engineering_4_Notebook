from picamera import PiCamera #importing libraries 
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Button

GPIO.setwarnings(False) #stop warning us python we aren't doing anything wrong
GPIO.setmode(GPIO.BCM) #gpio setup
GPIO.setup(4, GPIO.IN) #setting up pi to take input from pin 4
camera = PiCamera() #camera object
frame = 1 #counts the number of pictures taken
toggle = 0 #for making button work right and not think it's being pressed 10 billion times if it's accidentally held down

camera.start_preview()

try:
    while True:
        if (GPIO.input(4) and not toggle): #runs when button is pressed and toggle makes this only activate once because the button has to stop being pressed for this to run again
            camera.capture("/home/pi/Documents/Engineering_4_Notebook/Python/Animation/frame%03d.jpg" % frame) #saves pictures to Animation folder named as frame plus a number that increases
            frame += 1 #increases frame by 1
            toggle = 1 #button problem fix
        if (not GPIO.input(4) and toggle): #having the button not pressed resets toggle
            toggle = 0 #button problem fix
except KeyboardInterrupt: #if the user presses control-c then
    camera.stop_preview() #stop the camera
