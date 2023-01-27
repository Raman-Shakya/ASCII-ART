import cv2
import tkinter as tk

Window = tk.Tk()
Window.geometry("800x500")

greetings = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    height=10
)
greetings.pack()

Window.mainloop()