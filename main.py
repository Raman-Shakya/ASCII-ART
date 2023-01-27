import cv2
import os

from edit import Editor
from DrawingApp import DrawingApp

# you might wanna play with this const
TEXT_WIDTH = 100
CANNY_CONSTANT = 150


cv2.namedWindow("frame")
cv2.createTrackbar("threshold1", "frame", 1, 500, lambda a: 0)
cv2.createTrackbar("threshold2", "frame", 1, 500, lambda a: 0)


for image in os.listdir("inputs"):

    name, typ = image.split(".")

    # check for unsupported file type
    if typ not in ["bmp","pbm","pgm","ppm","sr","ras","jpeg","jpg","jpe","tiff","tif","png"]:
        print(f"Cannot read {image} file")
        continue
    
    img = cv2.imread("inputs\\"+image)  # reading image
    
    # resizing image
    width = 600
    aspect = int(len(img[0]))/int(len(img))
    img = cv2.resize(img, (width, int(width/aspect)))

    

    # editor = DrawingApp(600, 500)
    # img = editor.draw()


    while True:
        threshold1 = cv2.getTrackbarPos("threshold1", "frame")
        threshold2 = cv2.getTrackbarPos("threshold2", "frame")
        canny = cv2.Canny(img, threshold1, threshold2)

        cv2.imshow("frame", canny)

        key = cv2.waitKey(1)
        if (key==27):
            break

    
    # editing image
    editor = Editor(img, "outputs\\" + name + ".txt", TEXT_WIDTH, threshold1, threshold2)
    editor.makeOutput()