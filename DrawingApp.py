import cv2
import numpy as np


class DrawingApp:
    def __init__(self, widht, height):
        self.canvas = np.zeros((300, 400, 1), np.uint8)
        self.canvas.fill(255)
        self.isDrawing = True

        self.previous_x = 0
        self.previous_y = 0
        self.isDrawing  = False

        self.color = 0

        self.windowName = "drawBoard"
        cv2.namedWindow(self.windowName)
        cv2.imshow(self.windowName, self.canvas)
        cv2.setMouseCallback(self.windowName, self.mouseActionCallBack)


    def mouseActionCallBack(self, event, current_x, current_y, *b):
        if self.isDrawing:
            cv2.line(self.canvas, (current_x, current_y), (self.previous_x, self.previous_y), color=self.color, thickness=2)

        if event == cv2.EVENT_LBUTTONDOWN:
            self.isDrawing = True
        elif event == cv2.EVENT_LBUTTONUP:
            self.isDrawing = False

        self.previous_x = current_x
        self.previous_y = current_y

    def draw(self):
        while True:
            cv2.imshow(self.windowName, self.canvas)
            
            key = cv2.waitKey(1)
            if key==27:
                break
            if key==ord('z'):
                if self.color ==0 :
                    self.color = 255
                else:
                    self.color = 0

        return self.canvas
    