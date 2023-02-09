import cv2

characterMap = cv2.imread("characters.png")


class Editor:
    def __init__(self, img, width):
        # self.file = open(outputFileName, "w")
        self.img  = img
        self.canny = img
        self.imgWidth = len(img[0])
        self.imgHeight = len(img)
        self.aspect = self.imgWidth / self.imgHeight
        self.width = width
        self.height = int((width / self.aspect) / 2)


    def makeOutput(self):
        output = [[' ' for i in range(self.width)] for _ in range(self.height)] # text output

        for i in range(self.height):
            for j in range(self.width):
                output[i][j] = self.getChar(i, j, int(self.imgWidth/self.width), int(self.imgHeight/self.height*2))
        
        parsed = '\n'.join(''.join(output[i][j] for j in range(self.width)) for i in range(self.height))
        
        return parsed



    def getChar(self, i, j, w, h):
        temp = cv2.resize(characterMap, ((257*w, h)))

        scI = i*h # sc = StartCoordinate
        scJ = j*w
        # hw  = int(w/2) # h for half
        # hh  = int(h/2)

        return self.getBestChar(temp, scI, scJ, w, h)


        # topLeft    = self.activate(self.getAvg(scI, scJ, scI+hh, scJ+hw))
        # topRight   = self.activate(self.getAvg(scI, scJ+hw, scI+hh, scJ+w))
        # bottomLeft = self.activate(self.getAvg(scI+hh, scJ, scI+h, scJ+hw))
        # bottomRight= self.activate(self.getAvg(scI+hh, scJ+hw, scI+h, scJ+w))

        # if topLeft and topRight and bottomLeft and bottomRight:
        #     return "#"
        # if topLeft and bottomRight:
        #     return "\\"
        # if topRight and bottomLeft:
        #     return "/"
        # if (topLeft and bottomLeft) or (topRight and bottomRight):
        #     return "|"
        # if (topLeft and topRight):
        #     return "-"
        # if (bottomLeft and bottomRight):
        #     return "_"
        # return " "


    def getAvg(self, stI, stJ, enI, enJ):
        s = 0
        for i in range(stI, enI):     # vertical component
            for j in range(stJ, enJ): # horizontal component
                s += self.canny[i][j]
        s /= (enI-stI) * (enJ-stJ)

        return round(s)

    def activate(self, avg):
        return avg > 0


    def getBestChar(self, temp, scI, scJ, w, h):
        cv2.imshow("temp",temp[scI:scI+h, scJ:scJ+w])
        cv2.waitKey(0)

        def compare(char):
            count = 0
            for i in range(h):
                for j in range(w):
                    if self.activate(self.canny[scI + i][scJ + j]) == self.activate(temp[i][char*w + j][0]):
                        count += 1
            return count

        bestScore = 0
        bestChar = ' '
        for i in range(257):
            try:
                temp1 = compare(i)
            except:
                return ' '
            if temp1 >= bestScore:
                bestScore = temp1
                bestChar = chr(i)

        return bestChar
