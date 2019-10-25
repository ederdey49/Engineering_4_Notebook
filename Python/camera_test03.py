from picamera import PiCamera #get this object in here
from time import sleep #this one too

camera = PiCamera() #create a camera object called "camera"

camera.start_preview() #open the camera window on the screen
sleep(1) #pause for 1 second
camera.start_recording('/home/pi/Desktop/video.h264') #start recording to a file at this location
sleep(10) #pause for 10 seconds
camera.stop_recording() #stop recording
camera.stop_preview() #close the camera window
