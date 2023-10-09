import sympy as sym
import tkinter as tk

def compute_integral():
    expression = expression_entry.get()
    x = sym.symbols('x')
    integral = sym.integrate(expression, x)
    result_label.config(text="Tích phân của hàm số: " + str(integral))

def compute_derivative():
    expression = expression_entry.get()
    x = sym.symbols('x')
    derivative = sym.diff(expression, x)
    result_label.config(text="Đạo hàm của hàm số: " + str(derivative))

def compute_equation():
    equation = equation_entry.get()
    x = sym.symbols('x')
    solutions = sym.solve(sym.Eq(sym.sympify(equation), 0), x)
    result_label.config(text="Nghiệm của phương trình: " + str(solutions))

root = tk.Tk()
root.title("Chương trình tính toán giải tích")

expression_label = tk.Label(root, text="Nhập hàm số:")
expression_label.pack()

expression_entry = tk.Entry(root)
expression_entry.pack()

integral_button = tk.Button(root, text="Tích phân", command=compute_integral)
integral_button.pack()

derivative_button = tk.Button(root, text="Đạo hàm", command=compute_derivative)
derivative_button.pack()

equation_label = tk.Label(root, text="Nhập phương trình:")
equation_label.pack()

equation_entry = tk.Entry(root)
equation_entry.pack()

equation_button = tk.Button(root, text="Giải phương trình", command=compute_equation)
equation_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
