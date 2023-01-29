import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

from edit import Editor
from DrawingApp import DrawingApp
from ShowOutput import showOutput

setting = {
    "navBg": "#717171",
    "bg": "#D9D9D9",
    "TEXT_WIDTH": 50        # increase this
}

class GUI:

    def __init__(self):
        # setting window
        self.root = tk.Tk()
        self.root.config(background=setting["bg"])
        self.root.geometry("760x400")
        self.root.minsize(760, 400)

        # some variables
        self.image = []
        self.output = []


        # setup
        self.initNavBar()
        self.initFileView()
        self.initEditorView()


        self.root.mainloop()

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

        # editorSettingLabel = tk.Label(frame, text="Editor Setting", bg=setting["bg"], fg=setting["navBg"], font=("Arial",17))
        # editorSettingLabel.pack(side=tk.LEFT, padx=50, pady=18)

        # cannyCheck = tk.IntVar()
        # penCheck   = tk.IntVar()
        # self.addCheckButton(frame, "Canny (c)", cannyCheck)
        # self.addCheckButton(frame,  "Pen (p)" ,  penCheck )

        # self.addButton(frame, "Undo")
        # self.addButton(frame, "Redo")

        self.addButton(frame, "cancel", command=self.root.destroy)
        self.addButton(frame, "ok"    , command=self.root.destroy)

    # =========================================================== #
    
    def addButton(self, frame, text, command=lambda: 0):
        button = tk.Button(frame, text=text, height=2, width=16, bg=setting["navBg"], fg=setting["bg"], font=("Arial",11), command=command)
        button.pack(padx=10, pady=10)
    

    def addCheckButton(self, frame, text, variable, command=lambda:0):
        c1 = tk.Checkbutton(frame, text=text,variable=variable, onvalue=1, offvalue=0, command=command)
        c1.pack()


    # ======================== LEFT BAR BUTTON ON CLICK =========================== #
    def getImage(self):
        name = filedialog.askopenfilename()
        if not name: return
        temp = cv2.imread(name)

        
        # resizing image
        width = 600
        aspect = int(len(temp[0]))/int(len(temp))
        self.image = cv2.resize(temp, (width, int(width/aspect)))

        self.editingImgWindow()

    # ===================================================================================== #


    def drawWindow(self):
        master = tk.Tk()
        master.geometry("400x300")
        master.minsize(200, 100)

        def destroy():

            self.image = np.zeros((master.winfo_height(), master.winfo_width(), 3), np.uint8)
            master.destroy()

            self.editingImgWindow()

        tk.Label(master, text="resize me, and goto edit").pack()
        tk.Button(master, text='OK', command=destroy).pack()

        tk.mainloop()

    # ===================================================================================== #

    def editingImgWindow(self):
        if (len(self.image)!=0):
            try:
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            except:
                pass

            temp = DrawingApp(self.image)
            self.output = temp.draw()
    
    # ===================================================================================== #

    def generateOutput(self):
        if len(self.output)==0: return

        editor = Editor(self.output, setting["TEXT_WIDTH"])
        showOutput(editor.makeOutput())

        

        # f = filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        # if not f: return
        
        # editing image
        # editor.makeOutput()

    # ===================================================================================== #