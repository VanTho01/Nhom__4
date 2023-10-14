from tkinter import *
from tkinter.constants import BOTH
import subprocess

win = Tk()
win.geometry('500x350')
win.title('Menu')
win.resizable(True, True)
#win.configure(bg = '#FFF4D3')
frame_menu = Frame(win, highlightbackground='#FFF4D3', highlightthickness=2)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)
def Muc1():
    file= 'muc1.py'
    subprocess.call(['python', file])
def Muc2():
    file= 'muc2.py'
    subprocess.call(['python', file])
def Muc3():
    file= 'muc3.py'
    subprocess.call(['python', file])
def Muc4():
    file= 'muc4.py'
    subprocess.call(['python', file])

Label(win, text = "Hỗ trợ bạn môn giải tích", font = ('Times new roman', 15), bg = 'white', fg = 'Black', width = 20, height = 1, relief='solid', borderwidth = 2).place(x = 140, y = 2)

limit_button = Button(win,height = 4, text = " Tính giới hạn ",command = Muc1, font = ('Times new roman', 13), bg = '#45C3A4', fg = 'Black', width = 20, relief='solid', borderwidth = 2)
limit_button.place(x = 60, y = 70)
integral_button = Button(win,height = 4, text = " Tính tích phân \n đạo hàm",command = Muc2, font = ('Times new roman', 13), bg = '#45C3A4', fg = 'Black', width = 20, relief='solid', borderwidth = 2)
integral_button.place(x = 260, y = 70)
sovle_button = Button(win,height = 4, text = " Giải phương trình \nn bậc",command = Muc3, font = ('Times new roman', 13), bg = '#45C3A4', fg = 'Black', width = 20, relief='solid', borderwidth = 2)
sovle_button.place(x = 60, y = 170)
sovle_linear_button = Button(win,height = 4, text = " Giải hệ phương trình\n với n phương trình \nn ẩn",command = Muc4, font = ('Times new roman', 13), bg = '#45C3A4', fg = 'Black', width = 20, relief='solid', borderwidth = 2)
sovle_linear_button.place(x = 260, y = 170)
exit_button = Button(win,height = 2, text = " Thoát ",command = exit, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 10, relief='solid', borderwidth = 2)
exit_button.place(x = 200, y = 280)

win.mainloop()

""" class Menu:
    def __init__(self):
        label = Label(frame_menu, text="Choose Operation:", pady=10, font=('arial', 10, 'bold'))

        inv = Button(frame_menu, text="muc1", padx=22, pady=5, command=Muc1)
        ad = Button(frame_menu, text="muc2", padx=22, pady=5, command=Muc2)
        tran = Button(frame_menu, text="muc3", padx=22, pady=5, command=Muc3)
        mlt = Button(frame_menu, text="muc4", padx=22, pady=5, command=Muc4 )
        Exit = Button(frame_menu, text="Exit", padx=22, pady=5, command=exit) 

        label.pack()
        inv.pack()
        ad.pack()
        tran.pack()
        mlt.pack()        
        Exit.pack()

        gui_menu.mainloop() """
