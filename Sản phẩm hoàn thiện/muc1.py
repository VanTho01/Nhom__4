import sympy as sym
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#def Activate():
def on_radio_button_select():
    selected_value1 = radio_var1.get()
    print("Selected value:", selected_value1)
    return selected_value1

root = tk.Tk()
root.configure(bg = '#F0EEFF')
tk.Label(root, text = "Tính giới hạn hàm số", font = ('Times new roman', 15), bg = 'white', fg = 'Black', width = 20, height = 1, relief='solid', borderwidth = 2).place(x = 100, y = 2)
root.geometry('400x340')
selected_option = tk.StringVar()
selected_option.set('-')
options = ['-','+']
option_menu = tk.OptionMenu(root, selected_option, *options)
option_menu.place(x = 240, y = 180)

radio_var1 = tk.IntVar()

radio_button1 = tk.Radiobutton(root,font = ('Times New Roman', 15), width = 10, height=1, text="Cận 2 phía", variable=radio_var1, value=2, command=on_radio_button_select)
radio_button1.place(x = 80, y = 110)

radio_button2 = tk.Radiobutton(root,font = ('Times New Roman', 15), width = 10, height=1, text="Cận 1 phía", variable=radio_var1, value=1, command=on_radio_button_select)
radio_button2.place(x = 80, y = 150)

root.title("Mục 1")

expression_label = tk.Label(root, text = "f(x)", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, height = 1, relief='solid', borderwidth = 2)
expression_label.place(x = 60, y = 70)
expression_entry = tk.Entry(root, font = ('Times new roman', 12), fg = 'Black', width = 25, relief='solid', borderwidth = 2)
expression_entry.place(x = 130, y = 70)

output = tk.Text(root,font = ('Times New Roman', 15), height = 2, width = 25, relief='solid', borderwidth = 2)
output.configure(fg = 'black', bg = "white")
output.place(x = 130, y = 220)

#expression = expression_entry.get()
x0 = tk.StringVar()
tk.Label(root, text = " desti ", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, height = 1, relief='solid', borderwidth = 2).place(x = 60, y = 185)
tk.Entry(root, textvariable = x0, font = ('Times new roman', 11), fg = 'Black', width = 7, relief='solid', borderwidth = 2).place(x = 130, y = 185)
#type_can = on_radio_button_select()
def compute_Limit():
    try:
        output.delete("1.0", "end")
        type_can = on_radio_button_select()
        x = sym.symbols('x')
        expression = expression_entry.get()
        if (int(type_can) == 1):
            integral = sym.limit(expression, x, int(x0.get()), str(selected_option.get()))
            text="Giới hạn của hàm số: " + str(integral)
            output.insert(INSERT, text)
        if (int(type_can) == 2):
            integral = sym.limit(expression, x, int(x0.get()))
            text="Giới hạn của hàm số: " + str(integral)
            output.insert(INSERT, text)
    except:
        messagebox.showerror('Error', 'Kiểm tra lại đầu vào!')

limit_button = tk.Button(root, text = " Tích \n phân",command = compute_Limit, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, relief='solid', borderwidth = 2)
limit_button.place(x = 60, y = 220)
exit_button = tk.Button(root, text = " Thoát ",command = exit, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 6, relief='solid', borderwidth = 2)
exit_button.place(x = 60, y = 280)

root.mainloop()
