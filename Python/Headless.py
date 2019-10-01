import time

import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
padding = 2
top = padding
x = padding

font = ImageFont.load_default()

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    draw.text((x, top + 40), '0',  font=font, fill=255)
    draw.text((x + 110, top + 40), '10',  font=font, fill=255)
    draw.text((x + 35, top + 50), "X ACCEL",  font=font, fill=255)
    draw.rectangle((0, 10, accel_x/10*1.28, 30), outline=1, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(.5)
