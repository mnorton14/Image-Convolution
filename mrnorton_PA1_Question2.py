#Programming Assignment 1 Question 2

import numpy as np
import cv2
from matplotlib import pyplot as plt

#Reads in and shows the original RGB image and converts to grayscale
GrayImage = cv2.imread('easter-island-512x512.jpg', 0)
cv2.imshow('GrayScale', GrayImage)

#Creates an array of zeroes that is of size 256
imgArray = [0] * 256
m, n = GrayImage.shape
pixelSum = 0
for i in range (m) :
    for j in range (n): 
        imgArray[GrayImage[i][j]] += 1
        pixelSum+=1

#Creates image histogram
plt.figure(0)
x = np.array(range(256))
y = imgArray
plt.title('Image Histogram')
plt.ylabel('Number of Pixels')
plt.xlabel('Intensity Value')
plt.bar(x,y)

#Creates the cumulative historam
cumY = [0]*256
for i in range(len(imgArray)):
        if i == 0:
            cumY[i] = imgArray[i]
        else:
            cumY[i] = cumY[i-1] + imgArray[i]
plt.figure(1)
plt.title('Image Cumulative Histogram')
plt.ylabel('Number of Pixels')
plt.xlabel('Intensity Value')
plt.bar(x, cumY)

#Creates the transformation function
transArray = [0] * 256
##########        
cdf = cumY
cdf_normalized = cdf *(cumY[255]/ cdf[255])
transArray = cdf_normalized
######################
plt.figure(3)
plt.title('Transformation Function')
plt.ylabel('New Intensity Value')
plt.xlabel('Original Intensity Value')

plt.plot(x, transArray)

#Shows all of the plots created
plt.show()
#Sets Key to Close Windows to '0'
cv2.waitKey(0)
cv2.destroyAllWindows()