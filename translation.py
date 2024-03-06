import cv2 
from matplotlib import pyplot as plt
import numpy as np

def imshow(title="",image=None,size=10):
    w, h = image.shape[0],image.shape[1]
    aspect_ratio=w/h
    plt.figure(figsize=(size*aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


image = np.zeros((1024,1024,3),np.uint8)
height, width = image.shape[:2]
quarter_height,quarter_width = height/4, width/4
cv2.line(image,(0,0),(511,511),(255,255,255),5)
T =np.float32([[1,0,quarter_height],[0,1,quarter_width]])
image_translation = cv2.warpAffine(image,T,(width,height))
imshow("Image",image_translation,6)