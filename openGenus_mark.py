import numpy as np
import cv2

img = cv2.imread("input.jpg", cv2.IMREAD_UNCHANGED)

#print('Original Dimensions : ',img.shape) 

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#print('New Dimensions : ',img.shape) 

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomRightCornerOfText = (220,440)
fontScale              = 1
fontColor              = (0,255,255)
lineType               = 2

cv2.putText(img,'OpenGenus.org', 
    bottomRightCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)

cv2.imshow("img",img)

cv2.imwrite("dst.jpg", img)

cv2.waitKey(0)
