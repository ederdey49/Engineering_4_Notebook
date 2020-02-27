from picamera import PiCamera #get this object
from time import sleep #and this one

camera = PiCamera() #make a camera object called 'camera'

camera.start_preview() #open the camera window
sleep(5) #wait 5 seconds
camera.stop_preview() #close the window
