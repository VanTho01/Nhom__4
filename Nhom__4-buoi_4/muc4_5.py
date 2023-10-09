import tkinter as tk
from tkinter import messagebox, Entry, Label, Button, Scrollbar, Text

from sympy import symbols, integrate, diff, Eq, solve

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Ứng dụng Giải tích và Hệ phương trình")
root.geometry('800x600')

# Tạo khung chứa giao diện
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Tạo thanh trượt dọc cho khung giao diện
scrollbar = Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Tạo Text Widget để hiển thị kết quả
result_text = Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
result_text.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=result_text.yview)

# Bổ sung các thành phần giao diện khác vào Text Widget
result_text.insert(tk.END, "Kết quả sẽ được hiển thị ở đây...\n")

# Tạo và định vị các thành phần giao diện cho tích phân và đạo hàm
label_expression = Label(root, text="Nhập biểu thức:")
label_expression.pack(pady=5)

entry_expression = Entry(root)
entry_expression.pack(pady=5)

label_variable = Label(root, text="Biến ký hiệu:")
label_variable.pack(pady=5)

entry_variable = Entry(root)
entry_variable.pack(pady=5)

def integrate_single():
    expression = entry_expression.get()
    variable = entry_variable.get()
    
    x = symbols(variable)
    result = integrate(expression, x)
    
    result_text.insert(tk.END, f"Kết quả tích phân: {result}\n")

integrate_single_button = Button(root, text="Tích phân 1 lớp", command=integrate_single)
integrate_single_button.pack(pady=5)

def differentiate():
    expression = entry_expression.get()
    variable = entry_variable.get()
    
    x = symbols(variable)
    result = diff(expression, x)
    
    result_text.insert(tk.END, f"Kết quả đạo hàm: {result}\n")

differentiate_button = Button(root, text="Đạo hàm", command=differentiate)
differentiate_button.pack(pady=5)

# Tạo và định vị các thành phần giao diện cho tích phân 2 lớp
label_variable1 = Label(root, text="Biến ký hiệu 1:")
label_variable1.pack(pady=5)

entry_variable1 = Entry(root)
entry_variable1.pack(pady=5)

label_variable2 = Label(root, text="Biến ký hiệu 2:")
label_variable2.pack(pady=5)

entry_variable2 = Entry(root)
entry_variable2.pack(pady=5)

label_variable1_min = Label(root, text="Biến 1 tối thiểu:")
label_variable1_min.pack(pady=5)

entry_variable1_min = Entry(root)
entry_variable1_min.pack(pady=5)

label_variable1_max = Label(root, text="Biến 1 tối đa:")
label_variable1_max.pack(pady=5)

entry_variable1_max = Entry(root)
entry_variable1_max.pack(pady=5)

label_variable2_min = Label(root, text="Biến 2 tối thiểu:")
label_variable2_min.pack(pady=5)

entry_variable2_min = Entry(root)
entry_variable2_min.pack(pady=5)

label_variable2_max = Label(root, text="Biến 2 tối đa:")
label_variable2_max.pack(pady=5)

entry_variable2_max = Entry(root)
entry_variable2_max.pack(pady=5)

def integrate_double():
    expression = entry_expression.get()
    variable1 = entry_variable1.get()
    variable2 = entry_variable2.get()
    
    x = symbols(variable1)
    y = symbols(variable2)
    
    variable1_min = float(entry_variable1_min.get())
    variable1_max = float(entry_variable1_max.get())
    variable2_min = float(entry_variable2_min.get())
    variable2_max = float(entry_variable2_max.get())
    
    result = integrate(expression, (x, variable1_min, variable1_max), (y, variable2_min, variable2_max))
    
    result_text.insert(tk.END, f"Kết quả tích phân 2 lớp: {result}\n")

integrate_double_button = Button(root, text="Tích phân 2 lớp", command=integrate_double)
integrate_double_button.pack(pady=5)

# Tạo và định vị các thành phần giao diện cho giải hệ phương trình
label_a11 = Label(root, text="A11:")
label_a11.pack(pady=5)

entry_a11 = Entry(root)
entry_a11.pack(pady=5)

label_a12 = Label(root, text="A12:")
label_a12.pack(pady=5)

entry_a12 = Entry(root)
entry_a12.pack(pady=5)

label_a13 = Label(root, text="A13:")
label_a13.pack(pady=5)

entry_a13 = Entry(root)
entry_a13.pack(pady=5)

label_a21 = Label(root, text="A21:")
label_a21.pack(pady=5)

entry_a21 = Entry(root)
entry_a21.pack(pady=5)

label_a22 = Label(root, text="A22:")
label_a22.pack(pady=5)

entry_a22 = Entry(root)
entry_a22.pack(pady=5)

label_a23 = Label(root, text="A23:")
label_a23.pack(pady=5)

entry_a23 = Entry(root)
entry_a23.pack(pady=5)

label_a31 = Label(root, text="A31:")
label_a31.pack(pady=5)

entry_a31 = Entry(root)
entry_a31.pack(pady=5)

label_a32 = Label(root, text="A32:")
label_a32.pack(pady=5)

entry_a32 = Entry(root)
entry_a32.pack(pady=5)

label_a33 = Label(root, text="A33:")
label_a33.pack(pady=5)

entry_a33 = Entry(root)
entry_a33.pack(pady=5)

label_b1 = Label(root, text="B1:")
label_b1.pack(pady=5)

entry_b1 = Entry(root)
entry_b1.pack(pady=5)

label_b2 = Label(root, text="B2:")
label_b2.pack(pady=5)

entry_b2 = Entry(root)
entry_b2.pack(pady=5)

label_b3 = Label(root, text="B3:")
label_b3.pack(pady=5)

entry_b3 = Entry(root)
entry_b3.pack(pady=5)

def solve_linear_system():
    A = [[float(entry_a11.get()), float(entry_a12.get()), float(entry_a13.get())],
         [float(entry_a21.get()), float(entry_a22.get()), float(entry_a23.get())],
         [float(entry_a31.get()), float(entry_a32.get()), float(entry_a33.get())]]
    
    B = [float(entry_b1.get()), float(entry_b2.get()), float(entry_b3.get())]
    
    x, y, z = symbols('x y z')
    eq1 = Eq(A[0][0]*x + A[0][1]*y + A[0][2]*z, B[0])
    eq2 = Eq(A[1][0]*x + A[1][1]*y + A[1][2]*z, B[1])
    eq3 = Eq(A[2][0]*x + A[2][1]*y + A[2][2]*z, B[2])
    
    solution = solve((eq1, eq2, eq3), (x, y, z))
    
    result_text.insert(tk.END, f"Kết quả giải hệ phương trình: {solution}\n")

solve_button = Button(root, text="Giải hệ phương trình", command=solve_linear_system)
solve_button.pack(pady=5)

# Label để hiển thị kết quả
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
