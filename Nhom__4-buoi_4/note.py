import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ gốc
root = tk.Tk()
root.title("OptionMenu Example")

# Tạo biến StringVar để lưu giá trị được chọn
selected_option = tk.StringVar()

# Danh sách các tùy chọn
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Tạo OptionMenu và liên kết với biến StringVar
option_menu = tk.OptionMenu(root, selected_option, *options)
option_menu.pack()

# Hàm xử lý khi người dùng chọn tùy chọn mới
def on_option_select():
    selected_value = selected_option.get()
    print(f"Selected option: {selected_value}")



# Khởi chạy ứng dụng
root.mainloop()