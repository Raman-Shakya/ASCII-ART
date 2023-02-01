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
    "TEXT_WIDTH": 75        # Quality
}

class GUI:

    def __init__(self):
        # setting window
        self.root = tk.Tk()
        self.root.config(background=setting["bg"])
        self.root.geometry("760x400")
        self.root.title("ASCII-ART : Raman Shakya")
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

    # ====================== HELP TAB ========================= #
    def printHelp(self):
        window = tk.Tk()
        window.geometry("300x300")
        window.title("help")

        tk.Label(window, text="1. select a image first by 'Select File' button \nor make a new image by 'Draw' button").pack()
        tk.Label(window, text="2. an editor window will popup where you can edit\n or draw your image").pack()
        tk.Label(window, text="3. click on 'Generate' button to generate ASCII art\n and create a new window").pack()
        tk.Label(window, text="4. you can save or copy the output using the buttons\n\n").pack()



        tk.Label(window, text="these shortcuts are for editor window").pack()

        tk.Label(window, text="SHORTCUTS:").pack(pady=20)

        tk.Label(window, text="( z )\t:\tpen/eraser").pack()
        tk.Label(window, text="( enter )\t:\tdone").pack()

        window.mainloop()
    # ========================================================+


    # ======================= FILE VIEW ========================= #
    def initFileView(self):
        frame2 = tk.Frame(bg=setting["bg"])
        frame2.pack(side=tk.LEFT)
        
        self.addButton(frame2, "Select File", command=self.getImage)

        self.addButton(frame2, "Draw", command=self.drawWindow)

        # is image selected? label for that
        self.imageSelectedLabel = tk.Label(frame2, text="image not selected")
        self.imageSelectedLabel.pack()

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

        self.addButton(frame, "cancel", command=self.cancelImage)
        self.addButton(frame, "ok"    , command=self.root.destroy)

    # =========================================================== #

    def cancelImage(self):
        self.image = []
        self.output = []
        self.imageSelectedLabel.config(text="Image not selected")

        
    
    def addButton(self, frame, text, command=lambda: 0):
        button = tk.Button(frame, text=text, height=2, width=16, bg=setting["navBg"], fg=setting["bg"], font=("Arial",11), command=command)
        button.pack(padx=10, pady=10)
    

    def addCheckButton(self, frame, text, variable, command=lambda:0):
        c1 = tk.Checkbutton(frame, text=text,variable=variable, onvalue=1, offvalue=0, command=command)
        c1.pack()


    # ======================== LEFT BAR BUTTON ON CLICK =========================== #
    def getImage(self):
        name = filedialog.askopenfilename(filetypes=[
                        ("image", ".jpeg"),
                        ("image", ".png"),
                        ("image", ".jpg"),
                    ]
                )
        if not name: return

        self.imageSelectedLabel.config( text="image selected" )
        temp = cv2.imread(name)

        
        # resizing image
        width = 600
        aspect = int(len(temp[0]))/int(len(temp))
        self.image = cv2.resize(temp, (width, int(width/aspect)))

        self.editingImgWindow()

    # ---------------------------------------------------------------------------- #


    def drawWindow(self):
        master = tk.Tk()
        master.geometry("500x400")
        master.minsize(200, 100)
        master.title("Image Size Selector")

        self.imageSelectedLabel.config( text="image selected" )

        def destroy():

            self.image = np.zeros((master.winfo_height(), master.winfo_width(), 3), np.uint8)
            master.destroy()

            self.editingImgWindow()

        tk.Label(master, text="resize me").pack()
        tk.Button(master, text='OK', width=10, height=5, command=destroy).pack(expand=True)

        tk.mainloop()

    # ---------------------------------------------------------------------------- #

    def editingImgWindow(self):
        if (len(self.image)!=0):
            try:
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            except:
                pass

            temp = DrawingApp(self.image)
            self.output = temp.draw()
    
    # ---------------------------------------------------------------------------- #

    def generateOutput(self):
        if len(self.output)==0: return

        editor = Editor(self.output, setting["TEXT_WIDTH"])
        showOutput(editor.makeOutput())

        

        # f = filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        # if not f: return
        
        # editing image
        # editor.makeOutput()

    # ===================================================================================== #