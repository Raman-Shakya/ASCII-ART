import cv2
import os
import tkinter as tk


from GUI import GUI



setting = {
    "navBg": "#717171",
    "bg": "#D9D9D9"
}




def main():

    app = GUI(editingWindow)


    # name, typ = image.split(".")

    # # check for unsupported file type
    # if typ not in ["bmp","pbm","pgm","ppm","sr","ras","jpeg","jpg","jpe","tiff","tif","png"]:
    #     print(f"Cannot read {image} file")
    #     continue


    # img = cv2.imread("inputs\\"+image)  # reading image
    
    # # resizing image
    # width = 600
    # aspect = int(len(img[0]))/int(len(img))
    # img = cv2.resize(img, (width, int(width/aspect)))

    


def editingWindow(img):
    
    
    # editor = DrawingApp(600, 500)
    # self.image = editor.draw()

    cv2.namedWindow("frame")
    cv2.createTrackbar("threshold1", "frame", 1, 500, lambda a: 0)
    cv2.createTrackbar("threshold2", "frame", 1, 500, lambda a: 0)


    while True:
        threshold1 = cv2.getTrackbarPos("threshold1", "frame")
        threshold2 = cv2.getTrackbarPos("threshold2", "frame")
        canny = cv2.Canny(img, threshold1, threshold2)

        cv2.imshow("frame", canny)

        key = cv2.waitKey(1)
        if (key==27):
            break

    cv2.destroyWindow("frame")

    # editing image
    # editor = Editor(img, "outputs\\" + "test" + ".txt", TEXT_WIDTH, threshold1, threshold2)
    # editor.makeOutput()



if __name__=="__main__":
    main()