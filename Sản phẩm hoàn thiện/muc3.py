import sympy as sym
from tkinter import *
from tkinter import messagebox
import sympy.plotting as syp

win = Tk()
win.title('Muc 3')
win.geometry('400x300')
win.configure(bg = '#C4DFFF')

def sovle_equation():
    try:
        output.delete("1.0", "end")
        equation = expression_entry.get()
        x = sym.symbols('x')
        solutions = sym.solve(sym.Eq(sym.sympify(equation), 0), x)
        text="\n  Nghiệm của phương trình:\n " + str(solutions)
        output.insert(INSERT, text) 
    except:
        messagebox.showerror('Error', 'Kiểm tra lại đầu vào!')
def draw_graph():
    try:
        x = sym.symbols('x')
        syp.plot(expression_entry.get(), (x, -10, 10), title='Đồ thị hàm số f(x)')
    except:
        messagebox.showerror('Error', 'Kiểm tra lại đầu vào!')

Label(win, text = " Giải phương trình ", font = ('Times new roman', 15), bg = 'white', fg = 'Black', width = 23, height = 1, relief='solid', borderwidth = 2).place(x = 92, y = 1)

expression_label = Label(win, text = "Ptr", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, height = 1, relief='solid', borderwidth = 2)
expression_label.place(x = 40, y = 50)
expression_entry = Entry(win, font = ('Times new roman', 14), fg = 'Black', width = 25, relief='solid', borderwidth = 2)
expression_entry.place(x = 110, y = 50)

sovle_button = Button(win, text = " Giải \nptr",command = sovle_equation, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, relief='solid', borderwidth = 2)
sovle_button.place(x = 40, y = 110)

draw_button = Button(win, text = " Vẽ \nđồ thị ",command = draw_graph, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, relief='solid', borderwidth = 2)
draw_button.place(x = 40, y = 170)

exit_button = Button(win, text = " Thoát ",command = exit, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, relief='solid', borderwidth = 2)
exit_button.place(x = 40, y = 230)

output = Text(win,font = ('Times New Roman', 15), height = 4, width = 25, relief='solid', borderwidth = 2)
output.configure(fg = 'black', bg = "white")
output.place(x = 110, y = 110)

win.mainloop()


