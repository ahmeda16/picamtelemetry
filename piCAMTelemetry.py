import math
import os.path

import numpy as np
import serial
from PIL import Image

#Image Data To Be Mimicked
# @0000 03DEF FD8FFDB0084000D09090B0A080D0B0A0B0E0E0D0F13201513121213 ⇐ ⇐|

#1 @ being initial packet
#2 0000 being current sentance (starts at 0000)
#3 03DEF being total amount of sentances (0x03DDh + 1 telemetry sentance at end = 0x03DEh)
#4 data being 2 byte ascii hex bye of raw image data (0xFFh = 255, 0xD8h = 216, and etc) / 56 bytes fixed
#5 ⇐ CR character
#6 ⇐| LF character

#User Input For Any Given Image
imageName = str(input("Enter Image To Mimic Telemetry: "))
img = Image.open(imageName)

#Converts Image to 3D array (H x W x 3), 3 -> [255,255,255]
imageArray = np.asarray(img)

#INT of #3
def totalSentances(imageArray):

    height = len(imageArray)
    width = len(imageArray[0]) 
    pixelAmount = height*width
    
    totalSentances = int(math.ceil(pixelAmount / (56/2/3))) + 1

    return totalSentances

dataDecimalArray = np.zeros(0)

# for height in imageArray:
#     for width in height:
#         for value in width:

