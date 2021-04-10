import cv2
import numpy as np

# Reading the image
read_img=cv2.imread(file="baby_Pic1.jpg")
#print(img.shape)
img=cv2.resize(read_img,(300,300))
# Converting the image to grayscale
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Converting the image to inverted grayscale
inv_gray_img=255-gray_img

# Blurring the image
blur_img=cv2.GaussianBlur(inv_gray_img,(15,15),0)

# Inverting the blurred Image
inv_blur_img=255-blur_img

# Pencil Sketch Image
pencil_sketch=cv2.divide(gray_img,inv_blur_img,scale=250)

# Displaying the image

cv2.resize(pencil_sketch,(50,100))
cv2.imshow("Original Image",img)
cv2.imshow("Pencil Sketch Image",pencil_sketch)
cv2.waitKey(0)
