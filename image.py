#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:22:25 2019

@author: ugoslight
"""
from PIL import Image
from PIL import ImageFilter

picture = Image.open("nicholascage.jpg")
size_of_image = picture.size

picture = picture.filter(ImageFilter.SHARPEN)
pix = picture.load()

"""Left eyebrow"""


"""Right eyebrow"""

"""Right eye"""
picture.show()
for eye_areax in range(400, 427):
    for eye_areay in range(331, 349):
        if picture.getpixel((eye_areax, eye_areay))[0] in range(60, 157):
            if picture.getpixel((eye_areax, eye_areay))[1] in range(60, 135):
                if picture.getpixel((eye_areax, eye_areay))[2] in range(60, 120):
                    pix[eye_areax, eye_areay] = (1, 2, 3)
                    
for eye_areax in range(400, 427):
    for eye_areay in range(331, 349):
        if picture.getpixel((eye_areax, eye_areay))[0] in range(40, 150):#70,150
            if picture.getpixel((eye_areax, eye_areay))[1] in range(40, 155):#70,135
                if picture.getpixel((eye_areax, eye_areay))[2] in range(0, 150):#54,130
                    pix[eye_areax, eye_areay] = (10, 20, 50)
                    
"""Left eye"""
#picture.show()
for eye_areax in range(250, 277):
    for eye_areay in range(357, 376):
        if picture.getpixel((eye_areax, eye_areay))[0] in range(60, 157):#89, 157
            if picture.getpixel((eye_areax, eye_areay))[1] in range(60, 135):#73, 135
                if picture.getpixel((eye_areax, eye_areay))[2] in range(60, 120):#90, 120
                    pix[eye_areax, eye_areay] = (1, 2, 3)
                    
#picture.show()
for eye_areax in range(250, 277):
    for eye_areay in range(357, 376):
        if picture.getpixel((eye_areax, eye_areay))[0] in range(30, 170):
            if picture.getpixel((eye_areax, eye_areay))[1] in range(40, 150):
                if picture.getpixel((eye_areax, eye_areay))[2] in range(0, 153):
                    pix[eye_areax, eye_areay] = (10, 20, 50)



"""Left Earring"""
for x in range(130, 140):
    for y in range(528, 538):
        pix[x, y] = (243, 238, 238)
       
"""Right Earring"""
for x in range(501, 508):
    for y in range(470, 476):
        pix[x, y] = (243, 238, 238)
               

picture.show()
"""Lips
top_lip = [ (116, 36, 36), (121, 60, 60), (133, 63, 63), (129, 73, 73),
            (131, 71, 71), (133, 66, 66), (133, 77, 77), (129, 64, 64),
            (173, 96, 96), (147, 73, 73), (130, 62, 62), (178, 89, 89),
            (80, 14, 16), (167, 78, 78), (130, 56, 45), (120, 44, 31),
            (230, 151, 156), (225, 145, 148), (212, 110, 109)]
#Get Pixels in area
pixel_area = []
for lip_area1 in range(298, 441):
    for lip_area2 in range(524, 572):
        pixel_area.append(picture.getpixel((lip_area1, lip_area2)))

#Loop through pixel area to determine colors pixels to change
        
for lip_area1 in range(298, 441):
    for lip_area2 in range(524, 572):
        if picture.getpixel((lip_area1, lip_area2))[0] in range(180, 220):
            if picture.getpixel((lip_area1, lip_area2))[1] in range(75, 120):
                if picture.getpixel((lip_area1, lip_area2))[2] in range(90, 120):
                    pix[lip_area1, lip_area2] = (255, 0, 0)
                
picture.show()

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
image = cv2.imread(args["nicolascage.jpg"])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)"""