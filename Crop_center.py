#!/usr/bin/env python
# coding: utf-8

# In[28]:


import image_slicer
import glob
from PIL import Image
import glob
import cv2 as cv
import numpy as np
from scipy import misc
import math


# In[29]:


#image_slicer.slice('I10.png',10)


# In[30]:


import glob
img = []
for i in glob.glob('C:/Users/malin/OneDrive/Desktop/Robotics/ADV_ROBOTICS/png/Carpet/rotate/457x650/r0/*.png'):
    n= cv.imread(i)
    img.append(n)
cv.imshow("img",img[1])
cv.waitKey(0)


# In[31]:


w = img[0].shape[0] 
h = img[0].shape[1]

new_w = math.floor(w/math.sqrt(2))
new_h = math.floor(h/math.sqrt(2))
print(w)

left = math.floor((w - new_w)/2)
top = math.floor((h - new_h)/2)
right = math.floor((w + new_w)/2)
bottom = math.floor((h + new_h)/2)
test=img[0]

crop=test[top:bottom, left:right]
cv.imshow("crop",crop)
cv.waitKey(0)


# In[34]:


for i in range(361): #361 item in folder
    t=img[i]
    crop=t[top:bottom, left:right]
    cv.imwrite("c"+ str(i) + ".png", crop)


# In[ ]:




