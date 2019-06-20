#!/usr/bin/env python
# coding: utf-8

import image_slicer
import glob
from PIL import Image
import glob
import cv2 as cv
import numpy as np
from scipy import misc
import math
import glob

#image_slicer.slice('I10.png',10)

img = []
for i in glob.glob('../*.png'): #Enter the path of the images
    n= cv.imread(i)
    img.append(n)

w = img[0].shape[0] 
h = img[0].shape[1]
new_w = math.floor(w/math.sqrt(2))
new_h = math.floor(h/math.sqrt(2))
left = math.floor((w - new_w)/2)
top = math.floor((h - new_h)/2)
right = math.floor((w + new_w)/2)
bottom = math.floor((h + new_h)/2)


for i in range(361): #361 item in folder
    t=img[i]
    crop=t[top:bottom, left:right]
    cv.imwrite("c"+ str(i) + ".png", crop)
