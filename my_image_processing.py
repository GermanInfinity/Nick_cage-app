#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:22:25 2019

@author: Akwarandu Ugo Nwachuku
Description: This module is responsible for applying makeup to an image passed
             in as an arguement. Specifically, this module applies makeup to 
             the image from the google drive folder. 
"""
from PIL import Image
from PIL import ImageFilter


class apply_makeup:
    def __init__(self, image):
        picture = Image.open(image)
        picture = picture.filter(ImageFilter.SHARPEN)
        pix = picture.load()
        self.left_eyebrow(picture, pix)
        self.right_eyebrow(picture, pix)
        self.left_eye(picture, pix)
        self.right_eye(picture, pix)
        self.earrings(pix)
        self.lips(picture, pix)
        picture = picture.filter(ImageFilter.BLUR)
        picture.show()
        
    """Iteratively changes the color of the left_eyebrow, pixel by pixel"""
    def left_eyebrow(self, image, pic):
        for eye_areax in range(192, 321):
            for eye_areay in range(304, 358):
                if image.getpixel((eye_areax, eye_areay))[0] in range(30, 150):
                    if image.getpixel((eye_areax, eye_areay))[1] in range(0, 102):
                        if image.getpixel((eye_areax, eye_areay))[2] in range(0, 100):
                            pic[eye_areax, eye_areay] = (46, 24, 3)
                            
                            
        for eye_areax in range(230, 293):
            for eye_areay in range(367, 383):
                if image.getpixel((eye_areax, eye_areay))[0] in range(160, 207):
                    if image.getpixel((eye_areax, eye_areay))[1] in range(90, 180):
                        if image.getpixel((eye_areax, eye_areay))[2] in range(75, 120):
                            pic[eye_areax, eye_areay] = (46, 24, 3)

    """Iteratively changes the color of the right_eyebrow, pixel by pixel"""
    def right_eyebrow(self, image, pic):
        for eye_areax in range(360, 460):
            for eye_areay in range(285, 330):
                if image.getpixel((eye_areax, eye_areay))[0] in range(30, 150):
                    if image.getpixel((eye_areax, eye_areay))[1] in range(0, 102):
                        if image.getpixel((eye_areax, eye_areay))[2] in range(0, 100):
                            pic[eye_areax, eye_areay] = (46, 24, 3)
                    
        for eye_areax in range(388, 446):
            for eye_areay in range(337, 355):
                if image.getpixel((eye_areax, eye_areay))[0] in range(150, 220):
                    if image.getpixel((eye_areax, eye_areay))[1] in range(60, 120):
                        if image.getpixel((eye_areax, eye_areay))[2] in range(60, 99):
                            pic[eye_areax, eye_areay] = (46, 24, 3)


    """Iteratively changes the color of the right_eye, pixel by pixel"""
    def right_eye(self, image, pic):
        for eye_areax in range(400, 427):
            for eye_areay in range(331, 349):
                if image.getpixel((eye_areax, eye_areay))[0] in range(60, 157):
                    if image.getpixel((eye_areax, eye_areay))[1] in range(60, 135):
                        if image.getpixel((eye_areax, eye_areay))[2] in range(60, 120):
                            pic[eye_areax, eye_areay] = (1, 2, 3)
                    
        for eye_areax in range(400, 427):
            for eye_areay in range(331, 349):
                if image.getpixel((eye_areax, eye_areay))[0] in range(40, 150):
                    if image.getpixel((eye_areax, eye_areay))[1] in range(40, 155):
                        if image.getpixel((eye_areax, eye_areay))[2] in range(0, 150):
                            pic[eye_areax, eye_areay] = (10, 20, 50)
     
    """Iteratively changes the color of the left_eye, pixel by pixel"""                       
    def left_eye(self, image, pic):
        for eye_areax in range(250, 277):
            for eye_areay in range(357, 376):
                if image.getpixel((eye_areax, eye_areay))[0] in range(60, 157):
                    if image.getpixel((eye_areax, eye_areay))[1] in range(60, 135):
                        if image.getpixel((eye_areax, eye_areay))[2] in  range(60, 120):
                            pic[eye_areax, eye_areay] = (1, 2, 3)
                    

        for eye_areax in range(250, 277):
            for eye_areay in range(357, 376):
                if image.getpixel((eye_areax, eye_areay))[0] in range(30, 170):
                    if image.getpixel((eye_areax, eye_areay))[1] in range(40, 150):
                        if image.getpixel((eye_areax, eye_areay))[2] in range(0, 153):
                            pic[eye_areax, eye_areay] = (10, 20, 50)
                 
    """Iteratively adds earrings to the image, pixel by pixel"""
    def earrings(self, pic):       
        """Left Earring"""
        for x in range(130, 140):
            for y in range(528, 538):
                pic[x, y] = (255, 204, 0)
       
        """Right Earring"""
        for x in range(501, 508):
            for y in range(470, 476):
                pic[x, y] = (255, 204, 0)
                
                
    """Iteratively changes the color of the lips, pixel by pixel"""
    def lips(self, image, pic):
        """Bottom left lip"""
        for lip_area1 in range(311, 345):
            for lip_area2 in range(553, 562):
                if image.getpixel((lip_area1, lip_area2))[0] in range(0, 220):
                    if image.getpixel((lip_area1, lip_area2))[1] in range(0, 103):
                        if image.getpixel((lip_area1, lip_area2))[2] in range(0, 103):
                            pic[lip_area1, lip_area2] = (255, 61, 113)
                
        """Top left lip"""
        for lip_area1 in range(311, 406): 
            for lip_area2 in range(518, 550): 
                if image.getpixel((lip_area1, lip_area2))[0] in range(0, 170): 
                    if image.getpixel((lip_area1, lip_area2))[1] in range(0, 100):
                        if image.getpixel((lip_area1, lip_area2))[2] in range(0, 100):
                            pic[lip_area1, lip_area2] = (255, 61, 74) 
                    
        for lip_area1 in range(311, 412): 
            for lip_area2 in range(514, 520): 
                if image.getpixel((lip_area1, lip_area2))[0] in range(0, 170): 
                    if image.getpixel((lip_area1, lip_area2))[1] in range(0, 100):
                        if image.getpixel((lip_area1, lip_area2))[2] in range(0, 100):
                            pic[lip_area1, lip_area2] = (255, 61, 113)
         
        for lip_area1 in range(412, 420): 
            for lip_area2 in range(513, 519): 
                if image.getpixel((lip_area1, lip_area2))[0] in range(0, 170): 
                    if image.getpixel((lip_area1, lip_area2))[1] in range(0, 100):
                        if image.getpixel((lip_area1, lip_area2))[2] in range(0, 100):
                            pic[lip_area1, lip_area2] = (255, 61, 74) 
          
        for lip_area1 in range(332, 346):
            for lip_area2 in range(555, 564):
                pic[lip_area1, lip_area2] = (255, 61, 74) 
        
        """Bottom right lip"""
        for lip_area1 in range(405, 435):
            for lip_area2 in range(522, 550):
                if image.getpixel((lip_area1, lip_area2))[0] in range(50, 210):
                    if image.getpixel((lip_area1, lip_area2))[1] in range(50, 103):
                        if image.getpixel((lip_area1, lip_area2))[2] in range(50, 109):
                            pic[lip_area1, lip_area2] = (255, 61, 113)

        for lip_area1 in range(389, 405):
            for lip_area2 in range(544, 560):
                if image.getpixel((lip_area1, lip_area2))[0] in range(50, 210):
                    if image.getpixel((lip_area1, lip_area2))[1] in range(50, 103):
                        if image.getpixel((lip_area1, lip_area2))[2] in range(50, 109):
                            pic[lip_area1, lip_area2] = (255, 61, 74) 
                    
        for lip_area1 in range(390, 400):
            for lip_area2 in range(555, 564):
                pic[lip_area1, lip_area2] = (255, 61, 74) 
                 
        for lip_area1 in range(382, 400):
            for lip_area2 in range(549, 555):
                pic[lip_area1, lip_area2] = (255, 61, 113) 
                         
        for lip_area1 in range(400, 410):
            for lip_area2 in range(549, 558):
                pic[lip_area1, lip_area2] = (255, 61, 74) 
        
        for lip_area1 in range(395, 405):
            for lip_area2 in range(549, 562):
                pic[lip_area1, lip_area2] = (255, 61, 113)
        
        for lip_area1 in range(373, 383):
            for lip_area2 in range(552, 568):
                pic[lip_area1, lip_area2] = (255, 61, 74) 
        
        for lip_area1 in range(390, 400):
            for lip_area2 in range(560, 565):
                pic[lip_area1, lip_area2] = (255, 61, 113) 
                    
        for lip_area1 in range(390, 403):
            for lip_area2 in range(545, 554):
                pic[lip_area1, lip_area2] = (255, 61, 74)            

        """Bottom middle lip"""
        for lip_area1 in range(345, 391):
            for lip_area2 in range(555, 568):
                if image.getpixel((lip_area1, lip_area2))[0] in range(160, 300):
                    if image.getpixel((lip_area1, lip_area2))[1] in range(100, 200):
                        if image.getpixel((lip_area1, lip_area2))[2] in range(100, 200):
                            pic[lip_area1, lip_area2] = (255, 61, 113)
    
 