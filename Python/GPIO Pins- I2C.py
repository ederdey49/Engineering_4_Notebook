import time #importing various libraries 

import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()

RST = 24 #setup stuff
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) #disp is the lcd display

disp.begin() #starts the lcd

disp.clear() #clears lcd
disp.display() #displays nothing because lcd was just cleared

width = disp.width #how wide the display is
height = disp.height #how long the display is
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
padding = 2 #how many pixels from the edge for purposes of good display
top = padding #same as above
x = padding #same as above

font = ImageFont.load_default()

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0) #clear the lcd background
    accel, mag = lsm303.read() #read the acceleration from the accelerometer
    accel_x, accel_y, accel_z = accel #breaks the acceleration into components
    mag_x, mag_y, mag_z = mag #breaks mag into components
    draw.text((x, top),    'ACCEL DATA',  font=font, fill=255) #print "ACCEL DATA" on the lcd screen
    draw.text((x, top+15), 'X = ' + str(accel_x/100), font=font, fill=255) #print x data
    draw.text((x, top+30), 'Y = ' + str(accel_y/100), font=font, fill=255) #print y data
    draw.text((x, top+45), 'Z = ' + str(accel_z/100), font=font, fill=255) #print z data
    disp.image(image) 
    disp.display() #displays the text
    time.sleep(.5) #wait half a second so the lcd is not updating literally constantly
