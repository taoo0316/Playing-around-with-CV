#!/usr/bin/env python
# coding: utf-8




import cv2 as cv

# read images

img_1 = cv.imread("/Users/zwt2000/Desktop/cute/timg.jpeg")

cv.imshow("Dream",img_1)
cv.waitKey(0)

#read videos

capture = cv.VideoCapture("/Users/zwt2000/Downloads/Several Days Later _ SpongeBob Time Card #36.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
        
capture.realease()
cv.destroyAllWindows()






