import cv2
from matplotlib import pyplot as plt
import numpy as np
print(cv2.__version__)


def imshow(title="",image=None,size=10):
    w, h = image.shape[0],image.shape[1]
    aspect_ratio=w/h
    plt.figure(figsize=(size*aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


image = cv2.imread("./images/rott.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_black = np.zeros((512,512,3),np.uint8)

#image,startign ,ending,colour,size
#cv2.line(image_blak,(0,0),(511,511),(255,255,255),5)
#image starting, ending, size
cv2.rectangle(image_black,(200,100),(300,250),(255,255,255),2)
#image, centre, radius, colr , fill
cv2.circle(image_black,(300,300),100,(255,255,255),-1)
our_string = "Hello World"
#image, text to display, bottom left starting point, Font,font size, Color, Thickness
cv2.putText(image_black,our_string,(155,290),cv2.FONT_HERSHEY_SIMPLEX,1,(40,200,0),4)


R, G, B= cv2.split(image)
print(f"shape of R :{R.shape}, shape of G :{G.shape}, shape of B:{B.shape}")

print(image.shape)
print(gray_image.shape)

imshow('rottwiller',image_black,6)



