import sympy as sym
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('Muc 2')
win.geometry('400x500')
win.configure(bg = '#C4DFFF')

def compute_integral():
    try:
        output.delete("1.0", "end")
        expression = expression_entry.get()
        x = sym.symbols('x')
        if integration_type.get() == "indefinite":
            integral = sym.integrate(expression, x)
            text = "\n  Tích phân của hàm số:\n    " + str(integral)
            output.insert(INSERT, text)
        else:
            a = float(lower_limit_entry.get())
            b = float(upper_limit_entry.get())
            integral = sym.integrate(expression, (x, a, b))
            text = "\n  Tích phân của hàm số:\n    " + str(integral)
            output.insert(INSERT, text)
    except:
        messagebox.showerror('Error', 'Kiểm tra lại đầu vào!')
    
def compute_derivative():
    try:
        output.delete("1.0", "end")
        expression = expression_entry.get()
        x = sym.symbols('x')
        derivative = sym.diff(expression, x)
        text="\n  Đạo hàm của hàm số:\n     " + str(derivative)
        output.insert(INSERT, text)
    except:
        messagebox.showerror('Error', 'Kiểm tra lại đầu vào!')

Label(win, text = "Tính tích phân, tính đạo hàm", font = ('Times new roman', 15), bg = 'white', fg = 'Black', width = 23, height = 1, relief='solid', borderwidth = 2).place(x = 92, y = 1)

expression_label = Label(win, text = "f(x)", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, height = 1, relief='solid', borderwidth = 2)
expression_label.place(x = 40, y = 50)
expression_entry = Entry(win, font = ('Times new roman', 14), fg = 'Black', width = 25, relief='solid', borderwidth = 2)
expression_entry.place(x = 110, y = 50)

integral_type_label = Label(win, text = "Type", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, height = 1, relief='solid', borderwidth = 2)
integral_type_label.place(x=110, y = 100)
#----
integration_type = StringVar(value="indefinite")
#-----
indefinite_radio = Radiobutton(win, text="Không xác định", font = ('Times new roman', 10), fg = 'Black', width = 17, relief='solid', borderwidth = 2, variable=integration_type, value="indefinite")
indefinite_radio.place(x=200, y = 100)
#------
definite_radio = Radiobutton(win, text="Xác định            ", font = ('Times new roman', 10), fg = 'Black', width = 17, relief='solid', borderwidth = 2, variable=integration_type, value="definite")
definite_radio.place(x=200, y = 128)

upper_limit_label = Label(win, text="Cận trên", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 8, height = 1, relief='solid', borderwidth = 2)
upper_limit_label.place(x=40, y = 160)

upper_limit_entry = Entry(win, font = ('Times new roman', 14), fg = 'Black', width = 17, relief='solid', borderwidth = 2)
upper_limit_entry.place(x=140, y = 160)

lower_limit_label = Label(win, text="Cận dưới", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 8, height = 1, relief='solid', borderwidth = 2)
lower_limit_label.place(x=40, y = 190)

lower_limit_entry = Entry(win, font = ('Times new roman', 14), fg = 'Black', width = 17, relief='solid', borderwidth = 2)
lower_limit_entry.place(x=140, y = 190)


integral_button = Button(win, text = " Tích \n phân",command = compute_integral, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, relief='solid', borderwidth = 2)
integral_button.place(x = 40, y = 240)

integral_button = Button(win, text = " Đạo \n hàm",command = compute_derivative, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, relief='solid', borderwidth = 2)
integral_button.place(x = 40, y = 300)

exit_button = Button(win, text = " Thoát ",command = exit, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, relief='solid', borderwidth = 2)
exit_button.place(x = 40, y = 380)

output = Text(win,font = ('Times New Roman', 15), height = 5, width = 25, relief='solid', borderwidth = 2)
output.configure(fg = 'black', bg = "white")
output.place(x = 110, y = 240)

win.mainloop()

