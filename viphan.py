import tkinter as tk
import sympy as sp

def calculate_derivative():
    expression = expression_entry.get()
    variable = variable_entry.get()
    
    try:
        x = sp.symbols(variable)
        derivative = sp.diff(expression, x)
        result_label.config(text=f"Phương trình vi phân: {derivative}")
    except Exception as e:
        result_label.config(text="Lỗi: " + str(e))

# Tạo cửa sổ
window = tk.Tk()
window.title("Tính Phương Trình Vi Phân")

# Tính phương trình vi phân
frame = tk.Frame(window)
frame.pack()

expression_label = tk.Label(frame, text="Nhập biểu thức:")
expression_label.pack()
expression_entry = tk.Entry(frame)
expression_entry.pack()

variable_label = tk.Label(frame, text="Biến của biểu thức:")
variable_label.pack()
variable_entry = tk.Entry(frame)
variable_entry.pack()

calculate_button = tk.Button(frame, text="Tính Toán", command=calculate_derivative)
calculate_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

# Bắt đầu vòng lặp chính
window.mainloop()
