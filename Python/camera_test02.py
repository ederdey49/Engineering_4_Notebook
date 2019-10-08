from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
num = 0
num2 = 0
effectsList = ['sketch', 'posterise', 'gpen', 'cartoon', 'negative', 'solarize', 'pastel', 'none', 'denoise', 'emboss', 'oilpaint', 'hatch', 'watercolor', 'film', 'blur', 'saturation', 'colorswap', 'washedout', 'colorpoint', 'colorbalance', 'deinterlace1', 'deinterlace2']

while(num < 22):
    camera.start_preview()
    camera.image_effect = effectsList[num]
    camera.annotate_text_size = 55
    camera.annotate_background = Color('Blue')
    camera.annotate_text = "This is effect " + effectsList[num]
    sleep(5)
    if(num2 < 5):
        camera.capture('/home/pi/Desktop/' + effectsList[num] + '.jpg')
        num2 = num2 + 1
    num = num + 1
camera.stop_preview()
