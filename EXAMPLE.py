import numpy as np
import cv2


img = cv2.imread('lena_gray.jpg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imwrite('sift_keypoints.jpg',img)




#img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv2.imwrite('sift_keypoints.jpg',img)



#sift = cv2.SIFT()
#kp, des = sift.detectAndCompute(gray,None)

#cv2.imshow('pic', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
