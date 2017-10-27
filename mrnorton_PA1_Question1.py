#Programming Assignment 1 Question 1

import numpy as np
import cv2

#Original Image G
G = cv2.imread('lena_gray.jpg', 0)/255.0
cv2.imshow('Original', G)

#Creates padding around the original image
bordersize=2
border=cv2.copyMakeBorder(G,top=bordersize, bottom=bordersize, left=bordersize, right=bordersize,  borderType= cv2.BORDER_CONSTANT)
#cv2.imshow('b',border)

#
#Problem 1 Part A
#

#Gx 2D Filter Applied to Image G
Xkernel = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]])
#Gy 2D FIlter Applied to Image G
Ykernel = np.array([[-1,-2,-1],
                   [0,0,0],
                   [1,2,1]])

#Function to filter the image G with a 2D kernel
def TwoDConv(image, imgKernel):
    
    #Variable creation for kernel, image and kernel height and width
    kernel = imgKernel
    imageHeight = G.shape[1]
    imageWidth = G.shape[0] 
    kernelHeight = kernel.shape[1]
    kernelWidth = kernel.shape[0] 
    
    #sets new image to all zeroes when initialized 
    filtered_G = np.zeros_like(G)
    
    #Loops over the pixels of the image to filter it
    for y in range(imageHeight):
        for x in range(imageWidth):
            pixel_sum = 0
            for kernelY in range(-(kernelHeight / 2), kernelHeight - 1):
                for kernelX in range(-(kernelWidth / 2), kernelWidth - 1):
                    pixel = 0
                    Ypixel = y - kernelY
                    Xpixel = x - kernelX
                    if (Ypixel >= 0) and (Ypixel < imageHeight) and (Xpixel >= 0) and (Xpixel < imageWidth):
                        pixel = G[Ypixel, Xpixel]
    
                    weight = kernel[kernelY + (kernelHeight / 2), kernelX + (kernelWidth / 2)]
                    pixel_sum += pixel * weight
            filtered_G[y, x] = pixel_sum
     
    #Determines which filtered image to show
    if(np.array_equal(kernel, Xkernel) == True):        
        cv2.imshow('Gx 2D Convolution', filtered_G)
    elif(np.array_equal(kernel, Ykernel) == True):
        cv2.imshow('Gy 2D Convolution', filtered_G)

#Calls the function to perform the convolutions
TwoDConv(G, Ykernel)    
TwoDConv(G, Xkernel)

  
#Problem 1 Part B

#Seperable arrays for image filters of Gx and Gy
X1 = np.array([1,2,1])
X2 = np.array([-1,0,1])
Y1 = np.array([-1,0,1])
Y2 = np.array([1,2,1])

def OneDConv(image, imgKernel1, imgKernel2):
######################
##REDONE VARIABLES
#Variable creation for kernel, image and kernel height and width
    kernel1 = imgKernel1
    kernel2 = imgKernel2
    imageHeight = G.shape[1]
    imageWidth = G.shape[0] 
    
    
    #X FILTER COMPLETE (works when manually entered kernel values)
    if(np.array_equal(kernel1, X1) == True):
        filtered_G = np.zeros_like(G)
        for i in range(imageHeight):
            for j in range(imageWidth):
                upperleft = 0
                left = 0
                lowerleft = 0
                upperright = 0
                right = 0
                lowerright =0
                if j > 0: 
                    if i > 0:
                        upperleft = G[i - 1][j - 1] * 1 #kernel1[0]
                    left = G[i][j - 1] * 2 #kernel1[1]
                    if i < imageHeight - 1:
                        lowerleft = G[i + 1][j - 1] * 1 #kernel1[2]
                if j < imageWidth - 1: 
                    if i > 0:
                        upperright = G[i - 1][j + 1] * -1 #kernel2[0]
                    right = G[i][j + 1] * -2 #kernel2[1]
                    if i < imageHeight - 1:
                        lowerright = G[i + 1][j + 1] * -1 #kernel2[2]
                val = upperleft + left + lowerleft + upperright + right + lowerright
                filtered_G[i][j] = val
        cv2.imshow('Gx 1D Convolution', filtered_G)
    
    #Y FILTER INCOMPLETE (giving issues)
    elif(np.array_equal(kernel1, Y1) == True):
        filtered_G = np.zeros_like(G) 
        for i in range(imageHeight):
            for j in range(imageWidth):
                upperleft = 0
                left = 0
                lowerleft = 0
                upperright = 0
                right = 0
                lowerright =0
                if i > 0: 
                    if j > 0:
                        upperleft = G[i - 1][j - 1] * -1 #kernel1[0]
                    left = G[i -1 ][j] * 0 #kernel1[1]
                    if i < imageHeight - 1:
                        lowerleft = G[i - 1][j - 1] * 1 #kernel1[2]
                if i < imageHeight - 1: 
                    if i > 0:
                        upperright = G[i + 1][j + 1] * 1 #kernel2[0]
                    right = G[i + 1][j] * 2 #kernel2[1]
                    if i < imageHeight - 1:
                        lowerright = G[i + 1][j - 1] * 1 #kernel2[2]
                val = upperleft + left + lowerleft + upperright + right + lowerright
                filtered_G[i][j] = val
        cv2.imshow('Gy 1D Convolution', filtered_G) 
     
    

#Calls the function to perform the convolutions  
OneDConv(G, X1, X2)
OneDConv(G, Y1, Y2)    

#Sets Key to Close Windows to '0'
cv2.waitKey(0)
cv2.destroyAllWindows()
