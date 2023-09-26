import numpy as np

def Input3(sopt, soan):
        A = np.zeros((sopt, soan), dtype = float)
        B = np.zeros((sopt, 1), dtype = float)
        for pt in range(0, sopt):
            print(f"Nhap he so cua phuong trinh thu {pt + 1}: ")
            for an in range(0, sopt):
                A[pt, an] = float(input(f"----he so thu {an + 1}: "))
            B[pt, 0] = float(input("----he so cuoi: "))
        print (A)
        print (B)
        return A, B
def calculate(A, B):
    try:
        if (np.linalg.det(A) != 0):
            X = np.dot(np.linalg.inv(A), B)
            return X
        else: 
            calculate(A, B)
    except:
        print("Error!!")
        Input3(A, B)
        calculate()

def selection():
    opinion = input("Nhap vao lua chon: Continue or Exit? ")
    if (opinion == "Continue"):
        sopt = Input1()
        soan = Input2()
        sopt, soan = test_input(sopt, soan)
        A, B = Input3(sopt, soan)
        X = calculate(A, B)
        print('Nghiem cua he:',X)
        print("=====================")
        selection()
    elif (opinion == "Exit"): 
        print("Thank for using!")
        exit()
    else: 
        print("Ban da nhap sai lua chon, vui long nhap lai!")
        selection()
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("giai he co n phuong trinh va n an")
win.geometry('900x700')
win.configure(bg = 'purple')

Label(win, text = 'Giai he phuong trinh n an', font = ('Arial', 13), bg = 'yellow', fg = 'black', height=2, relief='solid', borderwidth = 2, width = 40).place(x = 250, y = 0)

sopt = IntVar()
Label(win, text = 'Nhap so phuong trinh', font = ('Arial', 9), bg = 'yellow', fg = 'black', height=1, relief='solid', borderwidth = 2, width = 30).place(x = 250, y = 60)
Entry(win, textvariable = sopt, font = ('Arial', 13), bg = 'yellow', fg = 'black', relief='solid', borderwidth = 2, width = 5).place(x = 485, y = 60)

def create():
    A = []
    entries_A = []
    B = []
    entries_B = []
    soan = sopt.get()

    matrix_A = []
    matrix_B = []

    a = 'abcdefghijklmnopqrstuvwxyz'
    a1 = list(a)
    for i in range(sopt.get()):
        A.append([])
        entries_A.append([])
        B.append([])
        entries_B.append([])
        matrix_A.append([])
        matrix_B.append([])
        for j in range(soan):
            A[i].append(DoubleVar())
            if (i > 0):
                Label(win,background = 'purple', text = ' + '+a1[j]+f'{i}', width = 3).place(x = 250 + 80*i, y = 110 + 30*j)#grid(row = i, column = j+2)
            else:
                Label(win,background = 'purple', text = a1[j]+f'{i}', width = 3).place(x = 250 + 80*i, y = 110 + 30*j)#grid(row = i, column = j+2)
            entries_A[i].append(Entry(win, textvariable = A[i][j], width=3))
            entries_A[i][j].place(x =280 + 83*j, y = 110 + 30*i)#grid(row=i, column=j+4)
            matrix_A[i].append(A[i][j].get())
        B[i].append(DoubleVar())
        Label(win,background = 'purple', text = f' = ', width = 3).place( x = 310 + 83*(soan-1), y = 110 + 30*i)#grid(row = i, column = 4)
        entries_B[i].append(Entry(win, textvariable = B[i][0], width=3))
        entries_B[i][0].place( x = (soan+1)*128, y = 110 + 30*i)#grid(row= i, column= 5)
        matrix_B[i].append(B[i][0].get())

    matrix_A = np.array(matrix_A)
    matrix_B = np.array(matrix_B)
    print(matrix_A)
    return matrix_A, matrix_B
    
def clear():
    Label(win,background = 'purple', width = 180*sopt.get(), height = 20).place( x = 240, y = 100)
A, B = create()
def calculate():
    if (np.linalg.det(A) != 0):
        X = np.dot(np.linalg.inv(A), B)
        for i in range(sopt.get()):
            Label(win,background = 'purple', text = f'x{i} = ', width = 3).place( x = 50 + 83*i, y = 450)#grid(row = i, column = 4)
            Label(win,background = 'purple', text = f'{X[i][0]} ', width = 3).place( x = 100 + 83*i, y = 450)#grid(row = i, column = 4)

Button(win, text = 'Create', command = create, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 280, y = 510)
Button(win, text = 'Exit', command = exit, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 350, y = 510)
Button(win, text = 'Clear', command = clear, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 420, y = 510)
Button(win, text = 'Calculate', command = calculate, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 490, y = 510)

win.mainloop()
#selection()

