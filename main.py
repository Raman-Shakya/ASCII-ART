import cv2
import os
from edit import Editor

# you might wanna play with this const
TEXT_WIDTH = 100
CANNY_CONSTANT = 150


for image in os.listdir("inputs"):
    name, typ = image.split(".")

    # check for unsupported file type
    if typ not in ["bmp","pbm","pgm","ppm","sr","ras","jpeg","jpg","jpe","tiff","tif","png"]:
        print(f"Cannot read {image} file")
        continue
    
    img = cv2.imread("inputs\\"+image)  # reading image
    
    # resizing image
    width = 500
    aspect = int(len(img[0]))/int(len(img))
    img = cv2.resize(img, (width, int(width/aspect)))
    
    # editing image
    editor = Editor(img, "outputs\\" + name + ".txt", TEXT_WIDTH, CANNY_CONSTANT)
    editor.makeOutput()