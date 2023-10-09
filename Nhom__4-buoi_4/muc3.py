import sympy as sym
import tkinter as tk
from tkinter import ttk


def compute_integral():
    expression = expression_entry.get()
    x = sym.symbols('x')

    if integration_type.get() == "indefinite":
        integral = sym.integrate(expression, x)
    else:
        a = float(lower_limit_entry.get())
        b = float(upper_limit_entry.get())
        integral = sym.integrate(expression, (x, a, b))

    result_label.config(text="Tích phân của hàm số: " + str(integral))


def compute_derivative():
    expression = expression_entry.get()
    x = sym.symbols('x')
    derivative = sym.diff(expression, x)
    result_label.config(text="Đạo hàm của hàm số: " + str(derivative))


def compute_limit():
    expression = expression_entry.get()
    x = sym.symbols('x')
    x0 = float(limit_value_entry.get())
    limit = sym.limit(expression, x, x0)
    result_label.config(text="Giới hạn của hàm số tại x = {}: {}".format(x0, limit))


root = tk.Tk()
root.title("Chương trình tính toán giải tích")

frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)

expression_label = ttk.Label(frame, text="Nhập hàm số:")
expression_label.grid(column=0, row=0)

expression_entry = ttk.Entry(frame)
expression_entry.grid(column=1, row=0)

integral_type_label = ttk.Label(frame, text="Loại tích phân:")
integral_type_label.grid(column=0, row=1)

integration_type = tk.StringVar(value="indefinite")

indefinite_radio = ttk.Radiobutton(frame, text="Không xác định", variable=integration_type, value="indefinite")
indefinite_radio.grid(column=1, row=1)

definite_radio = ttk.Radiobutton(frame, text="Xác định", variable=integration_type, value="definite")
definite_radio.grid(column=1, row=2)

lower_limit_label = ttk.Label(frame, text="Giới hạn dưới (a):")
lower_limit_label.grid(column=0, row=3)

lower_limit_entry = ttk.Entry(frame)
lower_limit_entry.grid(column=1, row=3)

upper_limit_label = ttk.Label(frame, text="Giới hạn trên (b):")
upper_limit_label.grid(column=0, row=4)

upper_limit_entry = ttk.Entry(frame)
upper_limit_entry.grid(column=1, row=4)

integral_button = ttk.Button(frame, text="Tích phân", command=compute_integral)
integral_button.grid(column=0, row=5, columnspan=2)

derivative_button = ttk.Button(frame, text="Đạo hàm", command=compute_derivative)
derivative_button.grid(column=0, row=6, columnspan=2)

limit_value_label = ttk.Label(frame, text="Giá trị x:")
limit_value_label.grid(column=0, row=7)

limit_value_entry = ttk.Entry(frame)
limit_value_entry.grid(column=1, row=7)

limit_button = ttk.Button(frame, text="Tính giới hạn", command=compute_limit)
limit_button.grid(column=0, row=8, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=9, columnspan=2)

root.mainloop()
