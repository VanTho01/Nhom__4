import thong_ke as tk
import pandas as pd
from numpy import array
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

win = Tk()
win.title('Make report 2.0')
win.geometry('800x700')
win.resizable(False, False)
win.configure(bg = 'Indigo')

def xu_ly_du_lieu():
    file_name = input4.get("1.0", "end").strip()
    if file_name != "":
        try:
            df=pd.read_csv(file_name,index_col=0,header = 0)
            in_data = array(df.iloc[:,:])
            return in_data
        except FileNotFoundError:
            messagebox.showwarning("Lỗi file", "File không hợp lệ hoặc file không tồn tại.")
    else: 
        messagebox.showwarning('Cảnh báo','Chưa nhập file')
#title
Label(win, text = "Phần mềm xuất báo cáo", font = ('Times new roman', 14), bg = 'white', fg = 'Black', width = 40, height = 2, relief='solid', borderwidth = 2).place(x = 200, y = 2)


#tên giảng viên
Label(win, text = "Tên giảng viên", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 130, y = 70)
input1 = Text(win,font = ('Times New Roman', 13), height = 2, width = 23, relief='solid', borderwidth = 2)
input1.configure(fg = 'black', bg = "white")
input1.place(x = 270, y = 70)

#tên học phần
Label(win, text = "Tên tên học phần", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 130, y = 130)
input2 = Text(win,font = ('Times New Roman', 13), height = 2, width = 23, relief='solid', borderwidth = 2)
input2.configure(fg = 'black', bg = "white")
input2.place(x = 270, y = 130)

#nhập tên khoa
Label(win, text = "Tên khoa", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 130, y = 190)
input3 = Text(win,font = ('Times New Roman', 13), height = 2, width = 23, relief='solid', borderwidth = 2)
input3.configure(fg = 'black', bg = "white")
input3.place(x = 270, y = 190)

#Nhập file điểm
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Lấy tên tệp từ đường dẫn và hiển thị lên nhãn (Label)
        file_name = file_path.split("/")[-1]  # Lấy tên tệp từ đường dẫn
        input4.delete("1.0", "end")
        input4.insert(INSERT, file_name)
Button(win, text = "Nhập file", command = open_file_dialog, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 130, y = 250)
input4 = Text(win,font = ('Times New Roman', 13), height = 2, width = 20, relief='solid', borderwidth = 2)
input4.configure(fg = 'black', bg = "white")
input4.place(x = 270, y = 250)

#nhập tên file muốn lưu
Label(win, text = "Tên file lưu", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 130, y = 310)
input6 = Text(win,font = ('Times New Roman', 13), height = 2, width = 23, relief='solid', borderwidth = 2)
input6.configure(fg = 'black', bg = "white")
input6.place(x = 270, y = 310)

#lưu ý
note = '*Lưu ý: \n- Nhập tên giảng viên phải nhập cả học hàm học vị \n- File điểm được nhập là file dưới định dạng csv \n- Các mục của file bao gồm STT, tên lớp, Sĩ số, loại A+ => loại F, chuẩn L1, l2, Cuối kỳ'
input5 = Text(win,font = ('Times New Roman', 13), height = 5, width = 50, relief='solid', borderwidth = 2)
input5.configure(fg = 'black', bg = "white")
input5.place(x = 270, y = 370)
input5.insert(INSERT, note)

def export_report():
    teacher_name = input1.get("1.0", "end").strip()
    subject_name = input2.get("1.0", "end").strip()
    faculty_name = input3.get("1.0", "end").strip()
    filesave = input6.get("1.0", "end").strip()
    if (teacher_name != "" or subject_name != "" or faculty_name != "" or filesave != ""):
        data = xu_ly_du_lieu()
        tk.xuat_report(data, teacher_name, subject_name, faculty_name, filesave)
    else:
        messagebox.showwarning('Cảnh báo','Hãy nhập đầy đủ thông tin')
Button(win, text = 'Xuất report', command = export_report, font = ('Times new roman', 15), fg = 'black', bg = 'orange', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 170, y = 530)
Button(win, text = 'Thoát', command = exit, font = ('Times new roman', 15), fg = 'black', bg = 'orange', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 340, y = 530)

win.mainloop()
