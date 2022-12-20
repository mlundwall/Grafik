# This is a sample Python script.
import tkinter
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *


def drawline(event):
    print(event.type)
    if str(event.type) == '4':  # 'ButtonPress':
        canvas.old_coords = event.x, event.y

    elif str(event.type) == '5':  #'ButtonRelease':
        x, y = event.x, event.y
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()

    label = Label(root, text="Grafik")
    label.pack()

    # Set the size of the tkinter window
    root.geometry("700x350")

    # Create a canvas widget
    canvas = Canvas(root, width=500, height=300)
    canvas.pack()

    # Add a line in canvas widget
    canvas.create_line(100, 200, 200, 35, fill="black", width=1)
    root.bind('<ButtonPress-1>', drawline)
    root.bind('<ButtonRelease-1>', drawline)

    root.mainloop()
