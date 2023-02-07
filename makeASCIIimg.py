import cv2
import numpy

WIDTH = 12
HEIGHT = WIDTH*2

img = numpy.zeros((2*WIDTH, 242*WIDTH, 1), numpy.uint8)

cnt = 0
for i in range(2,256):
    if not chr(i).isspace():
        cv2.putText(img, chr(i), (cnt*WIDTH, HEIGHT), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255)
        cnt+=1

cv2.imshow('win', img)
cv2.waitKey(0)