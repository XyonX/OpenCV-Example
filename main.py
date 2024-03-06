import cv2
from matplotlib import pyplot as plt
print(cv2.__version__)


image = cv2.imread("./images/rott.jpg")



def imshow(title="",image=None):
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

cv2.imwrite('output.jpg',image)
print(image.shape)
imshow('rottwiller',image)



