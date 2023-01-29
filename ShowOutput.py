import tkinter as tk
from tkinter import filedialog

def showOutput(text):
    master = tk.Tk()

    frame = tk.Frame(master)
    frame.pack()

    tk.Button(frame, text="saveAs", command=lambda: savefunc(text)).pack()
    # tk.Button(frame, text="copy").pack()

    textArea = tk.Text(master, wrap="char")
    textArea.pack(fill="both", expand=True)

    textArea.insert(tk.INSERT, text)

    tk.mainloop()


def savefunc(text):
    filename = filedialog.asksaveasfilename()
    output = open(filename, "w")

    output.write(text)
    
    output.close()

