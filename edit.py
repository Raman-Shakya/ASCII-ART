import cv2

class Editor:
    def __init__(self, img, outputFileName, width):
        self.file = open(outputFileName, "w")
        self.img  = img
        self.canny = img
        self.imgWidth = len(img[0])
        self.imgHeight = len(img)
        self.aspect = self.imgWidth / self.imgHeight
        self.width = width
        self.height = int(width / self.aspect)

    def makeOutput(self):
        output = [[' ' for i in range(self.width)] for _ in range(self.height)] # text output

        for i in range(self.height):
            for j in range(self.width):
                output[i][j] = self.getChar(i, j, int(self.imgWidth/self.width), int(self.imgHeight/self.height))
        
        for i in output:
            self.file.write(' '.join(i)+'\n')
        self.file.close()

    def getChar(self, i, j, w, h):
        scI = i*h # sc = StartCoordinate
        scJ = j*w
        hw  = int(w/2) # h for half
        hh  = int(h/2)
        topLeft    = self.activate(self.getAvg(scI, scJ, scI+hh, scJ+hw))
        topRight   = self.activate(self.getAvg(scI, scJ+hw, scI+hh, scJ+w))
        bottomLeft = self.activate(self.getAvg(scI+hh, scJ, scI+h, scJ+hw))
        bottomRight= self.activate(self.getAvg(scI+hh, scJ+hw, scI+h, scJ+w))

        if topLeft and topRight and bottomLeft and bottomRight:
            return "#"
        if topLeft and bottomRight:
            return "\\"
        if topRight and bottomLeft:
            return "/"
        if (topLeft and bottomLeft) or (topRight and bottomRight):
            return "|"
        if (topLeft and topRight):
            return "-"
        if (bottomLeft and bottomRight):
            return "_"
        return " "


    def getAvg(self, stI, stJ, enI, enJ):
        s = 0
        for i in range(stI, enI):     # vertical component
            for j in range(stJ, enJ): # horizontal component
                s += self.canny[i][j]
        s /= (enI-stI) * (enJ-stJ)

        return round(s)

    def activate(self, avg):
        return avg > 0