import cv2
import numpy as np




#1

#img = cv2.imread('lena_gray.jpg')

img = cv2.imread('easter-island-512x512.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imwrite('sift_keypoints.jpg',img)
cv2.imshow('sift_keypoints.jpg',img)




filename = 'easter-island-512x512.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)

img2 = cv2.pyrMeanShiftFiltering(img,30, 30)
cv2.imshow('mean shift', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()