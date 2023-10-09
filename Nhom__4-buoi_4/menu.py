from tkinter import *
from tkinter.constants import BOTH
import muc1_2_3
import muc1
import muc3
import muc4_5

gui_menu = Tk()
# gui_menu.geometry('150x180')
gui_menu.title('Menu')
gui_menu.resizable(True, True)
frame_menu = Frame(gui_menu, highlightbackground='black', highlightthickness=1)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

class Menu:
    def __init__(self):
        label = Label(frame_menu, text="Choose Operation:", pady=10, font=('arial', 10, 'bold'))

        inv = Button(frame_menu, text="muc1,2,3", padx=30, pady=5, command=muc1_2_3)
        ad = Button(frame_menu, text="muc1", padx=40, pady=5, command=muc1)
        tran = Button(frame_menu, text="muc3", padx=22, pady=5, command=muc3)
        mlt = Button(frame_menu, text="muc4,5", padx=28, pady=5, command=muc4_5)
        Exit = Button(frame_menu, text="Exit", padx=15, pady=5, command=exit) 

        label.pack()
        inv.pack()
        mlt.pack()
        ad.pack()
        tran.pack()
        Exit.pack()

        gui_menu.mainloop()
