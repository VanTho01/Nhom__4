from pydub import AudioSegment
import numpy as np
import soundfile as sfile
from pydub.playback import play
import time
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Sound Recognition")
win.geometry('600x607')
win.config(bg = '#9C61CC')

#thiet ke UI
Label(win, text = "Phần mềm nhận dạng \nchó và mèo", font = ('Times new roman', 15), bg = 'white', fg = 'Black', width = 20, height = 2, relief='solid', borderwidth = 2).place(x = 200, y = 2)

Label(win, text = "Nhập file \nâm thanh", font = ('Times new roman', 13), bg = 'white', fg = 'Black', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 140, y = 60)
input = Text(win,font = ('Times New Roman', 13), height = 2, width = 16, relief='solid', borderwidth = 2)
input.configure(fg = 'black', bg = "white")
input.place(x = 320, y = 60)

Label(win, text = "Kết quả \nnhận dạng", font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 11, height = 2, relief='solid', borderwidth = 2).place(x = 240, y = 150)
output = Text(win,font = ('Times New Roman', 13), height = 15, width = 45, relief='solid', borderwidth = 2)
output.configure(fg = 'black', bg = "white")
output.place(x = 90, y = 210)

Button(win, text = 'Recog', command = "", font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 160, y = 520)
Button(win, text = 'Play', command = "", font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 260, y = 520)
Button(win, text = 'Exit', command = exit, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 360, y = 520)


#xu ly tep am thanh
""" def convert_to_decibel(arr):
            ref = 1
            if arr != 0:
                return 20 * np.log10(np.abs(arr) / ref)
            else:
                return -60
def data_process(filename):
    x_input = []
    for file in filename:
        data_train = []
        audio = AudioSegment.from_wav(file)
        signal, sr = sfile.read(file)
        samples_sf = 0
        try:
            samples_sf = signal[:, 0]  
        except:
            samples_sf = signal
        data=[convert_to_decibel(i) for i in samples_sf]
        data_train.append(round(np.mean(data), 2)) # trung binh
        data_train.append(round(np.median(data), 2))# trung vi
        data_train.append(round(np.std(data), 2))# Do lech chuan
        data_train.append(round(np.var(data), 2))# Phuong sai
        x_input.append(data_train)
    return x_input """

#mo hinh no-ron
""" def hard_lim(x):
    if x >= 0:
        return 1
    else:
        return 0
class Neural:
    def __init__(self, x_inputs, w_weight, bias):
        self.x_inputs = x_inputs
        self.w_weight = w_weight
        self.bias = bias
    def Sum_function(self):
        n = self.bias
        for x, w in zip(self.x_inputs, self.w_weight):
            n += x*w
        return n
    def output(self):
        a = hard_lim(Neural.Sum_function(self))
        return a
def cal_error(a, target):
    error = target - a
    return error
def update_weight(w_old, X, error):
    w_new = []
    for w, x in zip(w_old, X):
        if error == 1:
            i = w + x
            w_new.append(i)
        elif error == -1:
            i = w - x
            w_new.append(i)
        elif error == 0:
            i = w
            w_new.append(i)
    return w_new
def update_bias(b_old, error):
    b_new = b_old + error
    return b_new

def TEST(file, w_weight, bias):
    print('Start testing process........')
    file_n = []
    try:
        file_n.append(file)
        ex = data_process(file_n)
        print("ex = ", ex)
        neural = Neural(ex[0], w_weight, bias)
        result = neural.output()
    except:
        result = -1
    if result == 0:
        print(file, '==> THIS IS A CAT!')
    elif result == 1:
        print(file, '==> THIS IS A DOG!')
    else:
        print(file, "==> SORRY, I DON'T KNOW WHAT IT IS!")
    print('Complete testing!')
    print("===============***================")
    #print('What do you want in the next time?')

def check_input(file, file_train, x_inputs):
    print('Start checking input..........')
    file_ = [] 
    file_.append(file)
    test = data_process(file_)
    count = 0
    for t in test:
        for tr, f_tr in zip(x_inputs, file_train):
            if t == tr:
                count = count + 1
                print(t, tr)
                print(file, f_tr)
    if count == 0:
        print("Your file isn't on the data train!")
    else:
        print("Your file test appeared on the data train!")
    print('Complete!')
    print()

def Selection(file_train, x_inputs, w_weights, bias):
    try:
        selection = input('Enter your selection: ')
                
        if selection == 'cnt' or selection == 'exit':
            if selection == 'cnt':
                file = input('Enter your file: ')
                check_input(file, file_train, x_inputs)
                TEST(file, w_weights, bias)
                selection2 = input(f'--Do you want to play {file}? Yes or No? ')
                if selection2 == 'Yes':
                    sound = AudioSegment.from_file(file, format="wav")
                    play(sound)
                    print('End sound.')
                    print()
                    print('What do you want in the next time?')
                    Selection(file_train, x_inputs, w_weights, bias)
                elif selection2 == 'No':
                    print()
                    print('What do you want in the next time?')
                    Selection(file_train, x_inputs, w_weights, bias)
            elif selection == 'exit':
                print('Thank you for attention!')
                exit()
        else:
            print('Try one more time!')
            Selection(file_train, x_inputs, w_weights, bias)
    except FileNotFoundError:
        print('File non-existing! Try again!')
        Selection(file_train, x_inputs, w_weights, bias)  
#thuat toan lan truyen thang
if __name__ == "__main__":
    file_train = ['dog1.wav', 'dog2.wav', 'dog3.wav', 'dog4.wav', 'dog5.wav', 
                  'dog6.wav', 'dog7.wav', 'dog8.wav', 'dog9.wav', 'dog10.wav',
                  'dog11.wav',
                  'cat1.wav', 'cat2.wav', 'cat3.wav', 'cat4.wav', 'cat5.wav', 
                  'cat6.wav', 'cat7.wav', 'cat8.wav', 'cat9.wav', 'cat10.wav',
                  'cat11.wav']
    target = [1, 1, 1, 1, 1,
              1, 1, 1, 1, 1,
              1,
              0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 
              0]
    epoch = 100000000000000000
    print("Start processing data..........")
    x_inputs = data_process(file_train)
    print("x_inputs = ", x_inputs)
    print("Complete.")
    print()
    w_weights = [0.5, 0.6, -1, 1]
    bias = 0.9
    t1 = time.time()
    print('Start training .............')
    for i in range(0, epoch + 1):
        Y = []
        for x, t in zip(x_inputs, target):
            neural = Neural(x, w_weights, bias)
            output = neural.output()
            if output != t:
                error = cal_error(output, t)
                w_new = update_weight(w_weights, x, error)
                b_new = update_bias(bias, error)
                w_weights = w_new
                bias = b_new
            else:
                Y.append(output)
        if (Y == target):
            t2 = time.time()
            print("Processing to train complete in epoch ",i + 1)
            print(f"After {round((t2 - t1), 2)}s")
            print('Y = ',Y)
            print("Updated weight: ", w_weights)
            print("Updated bias: ", bias)
            print('Training success.')
            print()
            break
    print("=========*=============")
    print("--Enter: 'cnt' if you want to check and test file test\n--Enter: 'exit' if you want to get out of here")
    Selection(file_train, x_inputs, w_weights, bias)  """

win.mainloop()