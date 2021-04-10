import cv2
import numpy as np

read_img=cv2.imread(file="baby_Pic1.jpg")
img=cv2.resize(read_img,(450,450))

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_img=cv2.medianBlur(gray_img,1)
edges=cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,7)

color=cv2.bilateralFilter(img,65,100,100)
cartoon=cv2.bitwise_and(color,color,mask=edges)


# Displaying the image
cv2.imshow("Original Image",img)
cv2.imshow("Sketch Portrait",cartoon)
cv2.waitKey(0)
