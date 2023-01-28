import tkinter as tk

setting = {
    "navBg": "#717171",
    "bg": "#D9D9D9"
}

class GUI:

    def __init__(self):
        self.initNavBar()
        self.initFileView()
        self.initEditorView()


    def initNavBar(self):
        frame = tk.Frame(bg=setting["navBg"])
        frame.pack(fill='x')

        asciiArtLabel = tk.Label(frame, text="ASCII ART", bg=setting["navBg"], fg=setting["bg"], font=("Arial",17))
        asciiArtLabel.pack(side=tk.LEFT, padx=50, pady=18)
        
        helpButton = tk.Button(frame, text=" help ", command=self.printHelp, font=("Arial",12))
        helpButton.pack(side=tk.RIGHT, padx=10)

    def printHelp(self):
        print("helped")


    def initFileView(self):
        frame2 = tk.Frame(bg=setting["bg"])
        frame2.pack(side=tk.LEFT)
        
        self.addButton(frame2, "Select File")
        self.addButton(frame2, "Draw")

        self.addButton(frame2, "Edit")
        self.addButton(frame2, "Draw")

        self.addButton(frame2, "Generate")

    
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

    
    def addButton(self, frame, text):
        button = tk.Button(frame, text=text, height=2, width=16, bg=setting["navBg"], fg=setting["bg"], font=("Arial",11))
        button.pack(padx=10, pady=10)
    

    def addCheckButton(self, frame, text, variable, command=lambda:0):
        c1 = tk.Checkbutton(frame, text=text,variable=variable, onvalue=1, offvalue=0, command=command)
        c1.pack()


def main():

    root = tk.Tk()
    root.config(background=setting["bg"])
    root.geometry("760x400")
    root.minsize(760, 400)
    app = GUI()
    root.mainloop()


if __name__ == '__main__':
    main()