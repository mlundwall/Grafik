# Test interaktiv grafik med Tkinter
# Mads Lundwall 2022
from tkinter import *
import sys


def drawline(event):
    # Vi har modtaget et musetryk
    # print(event.type)
    if str(event.type) == '4':  # 'ButtonPress':
        # Når vi trykker husker vi positonen
        canvas.old_coords = event.x, event.y
    elif str(event.type) == '5':  # 'ButtonRelease':
        # Når vi løfter, tegner vi linjen
        x, y = event.x, event.y
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)


def knaptryk():
    label.config(text="Grafik - nu med tryk")
    original_stdout = sys.stdout        # SReference til standard output

    with open('tekstfil.txt', 'w') as f:
        sys.stdout = f                  # Flyt stdout til filen.
        print(label.cget("text") +
              " og output til fil")     # cget == hent config-variabel, her text
        sys.stdout = original_stdout    # Reset the standard output to its original value


if __name__ == '__main__':
    # Vi kører det som "hovedprogram", dvs eksekverer dette skript - ie. vi importerer det ikke
    # Opret et tkinter-rodvindue
    root = Tk()

    # Vi sætter hovedvinduets størrelse
    root.geometry("700x550")

    # Vi laver en overskrift
    label = Label(root, text="Grafik")
    label.pack()

    # Vi laver et område at tegne på
    canvas = Canvas(root, width=600, height=450)
    canvas.pack()

    knap = Button(root, command=knaptryk, text="    Knap    ")
    knap.pack()

    # Vi binder to events til musetryk/løft:
    root.bind('<ButtonPress-1>', drawline)
    root.bind('<ButtonRelease-1>', drawline)

    # Hoved - eventloop:
    root.mainloop()
