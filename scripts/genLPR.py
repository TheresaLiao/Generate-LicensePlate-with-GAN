import cv2;
from PIL import Image, ImageFont, ImageDraw
import numpy as np;
import os;
from math import *

index = {"-": 0, "0": 1, "1": 2, "2": 3, "3": 4, "4": 5, "5": 6,"6": 7, "7": 8, "8": 9, "9": 10, "A": 11, "B": 12, "C": 13, "D": 14, "E": 15, "F": 16, "G": 17, "H": 18,"J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "P": 24, "Q": 25, "R": 26, "S": 27, "T": 28, "U": 29, "V": 30, "W": 31, "X": 32, "Y": 33, "Z": 34};

chars = [ "-","0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
             "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
             "Y", "Z"];
def r(val):
    return int(np.random.random() * val)

def genPlateString(pos,val):
        plateStr = "";
        box = [0,0,0,0,0,0,0,0];
        if(pos!=-1):
            box[pos]=1;
        for unit,cpos in zip(box,range(len(box))):
            if unit == 1:
                plateStr += val
            else:
                if cpos <= 2:
                    plateStr += chars[11+r(24)]
                elif cpos == 3:
                    plateStr += chars[0]
                else:
                    plateStr += chars[1+r(10)]

        return plateStr;

if __name__ == '__main__':
        for i in range(50):
          image = Image.open("../images/template_w.jpg")
          draw = ImageDraw.Draw(image)  
          font = ImageFont.truetype("../font/platechar.ttf", 25)
          plateStr = genPlateString(-1,-1)
          text = plateStr
          draw.text((7,10), text, fill ="black", font = font, align ="left")  
          filename = os.path.join("../LPRSamples/"+str(i).zfill(4) + '-' + plateStr + ".jpg")
          image.save(filename, "JPEG")
