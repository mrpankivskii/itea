from tkinter import *


def output(output):
    root = Tk()
    root.title("Your output is:")
    text = Label(root, text=output)
    text.pack()
    root.mainloop()

