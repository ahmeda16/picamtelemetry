import math
import numpy as np
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
fileNotFound = False
while(fileNotFound == False):
    try:
        imageName = str(input("Enter Image To Mimic Telemetry: "))

        if (imageName == "quit"):

            fileNotFound = True

        else:

            img = Image.open(imageName)
            imageArray = np.asarray(img)
            fileNotFound = True

    except(FileNotFoundError):

        print("File Not Found, Try Again Or Type 'quit' To Exit")

#Converts Image to 3D array (H x W x 3), 3 -> [255,255,255]

#INT of #3
def totalSentances(imageArray):

    height = len(imageArray)
    width = len(imageArray[0]) 
    pixelAmount = height*width
    
    totalSentances = int(math.ceil(pixelAmount / (56/2/3))) + 1

    return totalSentances

#MASTER FUNCTION TO WRITE CAMERA TELEMETRY
def sentanceWriter(imageArray):
    intTotalSentances = totalSentances(imageArray)
    hexTotalSentances = "%04x" % intTotalSentances

    intSentanceCounter = -1
    imageHexLine = ""
    
    textFile = open("C:/{INSERT DIRECTORY HERE}/piCAMTELEMTRY.txt", "w")

    for height in imageArray:
        for width in height:
            for value in width:
                
                imageHexLine += ("%02x" % value).upper()
                
                if (len(imageHexLine) == 56):
                
                    intSentanceCounter += 1
                    hexSentanceCounter = ("%04x" % intSentanceCounter).upper()

                    sentance = "@" + hexSentanceCounter + hexTotalSentances + imageHexLine + "\r\n"
                    textFile.write(sentance)

                    imageHexLine = ""
    
    intSentanceCounter += 1
    hexSentanceCounter = ("%04x" % intSentanceCounter).upper()
    sentance = "@" + hexSentanceCounter + hexTotalSentances + (imageHexLine.ljust(56, "0")) + "\r\n"
    textFile.write(sentance)
    textFile.close()

sentanceWriter(imageArray)