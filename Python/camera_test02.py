from picamera import PiCamera, Color #get these obects in here
from time import sleep #and this one

camera = PiCamera() #make a camera object called 'camera'
num = 0 #this is a counter
num2 = 0 #this too
effectsList = ['sketch', 'posterise', 'gpen', 'cartoon', 'negative', 'solarize', 'pastel', 'none', 'denoise', 'emboss', 'oilpaint', 'hatch', 'watercolor', 'film', 'blur', 'saturation', 'colorswap', 'washedout', 'colorpoint', 'colorbalance', 'deinterlace1', 'deinterlace2']
#this long boi contains all the effects we're gonna rotate through

while(num < 22): #do this 22 times (we used a while loop because for loops are really gross in Python)
    camera.start_preview() #open the camera window
    camera.image_effect = effectsList[num] #set the effect to element 'num' of the effects list (first time is 'sketch', then 'posterise', etc.)
    camera.annotate_text_size = 55 #set text size
    camera.annotate_background = Color('Blue') #set background color
    camera.annotate_text = "This is effect " + effectsList[num] #write some text that says what affect we're using
    sleep(5) #pause for 5 seconds
    if(num2 < 5): #for the first 5 iterations,
        camera.capture('/home/pi/Desktop/' + effectsList[num] + '.jpg') #take a photo at this location with filename of effect type
        num2 = num2 + 1 #increment this counter
    num = num + 1 #increment this counter
camera.stop_preview() #close the camera window
