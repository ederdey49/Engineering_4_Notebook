import time #importing various libraries

import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303() #idk what this actually does but it's a setup thing

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) #disp is the lcd display

disp.begin() #start lcd

disp.clear() #clear lcd
disp.display() #display the newly-cleared display

width = disp.width #width is width
height = disp.height #height is height
image = Image.new('1', (width, height)) 
draw = ImageDraw.Draw(image) 
padding = 2 #this is how much space is used as padding on the sides of the display, for good formatting purposes
top = padding #same
x = padding #same

font = ImageFont.load_default() #font is default

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0) #clear display
    accel, mag = lsm303.read() #read the acceleration and mag
    accel_x, accel_y, accel_z = accel #split into components
    mag_x, mag_y, mag_z = mag #split into components
    
    draw.text((x, top + 40), '0',  font=font, fill=255) #draws a 0 at one end of the bar
    draw.text((x + 110, top + 40), '10',  font=font, fill=255) #draws a 10 at the other end, for scaling
    draw.text((x + 35, top + 50), "X ACCEL",  font=font, fill=255) #prints "X ACCEL" to label graph
    draw.rectangle((0, 10, accel_x/10*1.28, 30), outline=1, fill=255) #makes the bar the right size with some scaling math
    disp.image(image)
    disp.display() #displays updated size of bar
    time.sleep(.5) #pauses for 1/2 a second so it isn't constantly updating and looks like it's glitching
