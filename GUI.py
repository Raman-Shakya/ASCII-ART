import tkinter as tk
from tkinter import filedialog
import cv2

from edit import Editor
from DrawingApp import DrawingApp

setting = {
    "navBg": "#717171",
    "bg": "#D9D9D9",
    "TEXT_WIDTH": 100
    # you might wanna play with this const
# TEXT_WIDTH = 100
# CANNY_CONSTANT = 150
}

class GUI:

    def __init__(self, editingWindow=0):
        # setting window
        root = tk.Tk()
        root.config(background=setting["bg"])
        root.geometry("760x400")
        root.minsize(760, 400)

        # functions
        self.editingWindow = editingWindow

        # some variables
        self.image = []
        self.output = []

        # setup
        self.initNavBar()
        self.initFileView()
        self.initEditorView()


        root.mainloop()

    # ==================== NAVBAR ============================== #
    def initNavBar(self):
        frame = tk.Frame(bg=setting["navBg"])
        frame.pack(fill='x')

        asciiArtLabel = tk.Label(frame, text="ASCII ART", bg=setting["navBg"], fg=setting["bg"], font=("Arial",17))
        asciiArtLabel.pack(side=tk.LEFT, padx=50, pady=18)
        
        helpButton = tk.Button(frame, text=" help ", command=self.printHelp, font=("Arial",12))
        helpButton.pack(side=tk.RIGHT, padx=10)
    # ========================================================== #

    def printHelp(self):
        print("helped")


    # ======================= FILE VIEW ========================= #
    def initFileView(self):
        print(self.editingWindow)
        frame2 = tk.Frame(bg=setting["bg"])
        frame2.pack(side=tk.LEFT)
        
        self.addButton(frame2, "Select File", command=self.getImage)
        self.addButton(frame2, "Draw", command=self.drawWindow)

        self.addButton(frame2, "Edit", command=self.editingImgWindow)

        self.addButton(frame2, "Generate", command=self.generateOutput)
    # =========================================================== #


    # ===================== Editor SETTINGS ===================== #
    def initEditorView(self):
        frame = tk.Frame(bg=setting["bg"])
        frame.pack(side=tk.RIGHT)

        editorSettingLabel = tk.Label(frame, text="Editor Setting", bg=setting["bg"], fg=setting["navBg"], font=("Arial",17))
        editorSettingLabel.pack(side=tk.LEFT, padx=50, pady=18)

        cannyCheck = tk.IntVar()
        penCheck   = tk.IntVar()
        self.addCheckButton(frame, "Canny (c)", cannyCheck)
        self.addCheckButton(frame,  "Pen (p)" ,  penCheck )

        self.addButton(frame, "Undo")
        self.addButton(frame, "Redo")

        self.addButton(frame, "cancel")
        self.addButton(frame, "ok")

    # =========================================================== #
    
    def addButton(self, frame, text, command=lambda: 0):
        button = tk.Button(frame, text=text, height=2, width=16, bg=setting["navBg"], fg=setting["bg"], font=("Arial",11), command=command)
        button.pack(padx=10, pady=10)
    

    def addCheckButton(self, frame, text, variable, command=lambda:0):
        c1 = tk.Checkbutton(frame, text=text,variable=variable, onvalue=1, offvalue=0, command=command)
        c1.pack()


    def getImage(self):
        name = filedialog.askopenfilename()
        if not name: return
        temp = cv2.imread(name)

        
        # resizing image
        width = 600
        aspect = int(len(temp[0]))/int(len(temp))
        self.image = cv2.resize(temp, (width, int(width/aspect)))



    def drawWindow(self):
        return



    def editingImgWindow(self):
        if (len(self.image)!=0):
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

            temp = DrawingApp(self.image)
            self.output = temp.draw()
            # self.editingWindow(self.image)
    

    def generateOutput(self):
        print("here")
        if len(self.output)==0: return


        # editing image
        editor = Editor(self.output, "outputs\\" + "test" + ".txt", setting["TEXT_WIDTH"])
        editor.makeOutput()
