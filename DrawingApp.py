import cv2
import numpy as np


class DrawingApp:
    def __init__(self, canvas):
        self.canvas = canvas

        self.previous_x = 0
        self.previous_y = 0

        self.threshold1 = 0
        self.threshold2 = 0

        self.isDrawing  = False
        self.color = 255

        self.windowName = "drawBoard"
        cv2.namedWindow(self.windowName)
        cv2.createTrackbar("threshold1", self.windowName, 1, 500, lambda a: 0)
        cv2.createTrackbar("threshold2", self.windowName, 1, 500, lambda a: 0)
        cv2.createTrackbar("pensize"   , self.windowName, 1,  50, lambda a: 0)

    
        cv2.imshow(self.windowName, self.canvas)
        cv2.setMouseCallback(self.windowName, self.mouseActionCallBack)


    def mouseActionCallBack(self, event, current_x, current_y, *b):
        if self.isDrawing:
            cv2.line(self.canny, (current_x, current_y), (self.previous_x, self.previous_y), color=self.color, thickness=cv2.getTrackbarPos("pensize", self.windowName))

        if event == cv2.EVENT_LBUTTONDOWN:
            self.isDrawing = True
        elif event == cv2.EVENT_LBUTTONUP:
            self.isDrawing = False

        self.previous_x = current_x
        self.previous_y = current_y


    def draw(self):

        self.canny = cv2.Canny(self.canvas, self.threshold1, self.threshold2)
        while True:
            temp1 = cv2.getTrackbarPos("threshold1", self.windowName)
            temp2 = cv2.getTrackbarPos("threshold2", self.windowName)
            
            if temp1!=self.threshold1 or temp2!=self.threshold2:
                self.threshold1 = temp1
                self.threshold2 = temp2
                self.canny = cv2.Canny(self.canvas, self.threshold1, self.threshold2)

            cv2.imshow(self.windowName, self.canny)
            
            key = cv2.waitKey(1)
            if key==13:
                break
            if key==ord('z'):
                if self.color ==0 :
                    self.color = 255
                else:
                    self.color = 0
        cv2.destroyWindow(self.windowName)

        return self.canny
    