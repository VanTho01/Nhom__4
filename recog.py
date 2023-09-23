from pydub import AudioSegment
import numpy as np
import soundfile as sfile
import time

#xu ly am thanh
def convert_to_decibel(arr):
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
        samples = np.array(audio.get_array_of_samples())
        signal, sr = sfile.read(file)
        samples_sf = 0
        try:
            samples_sf = signal[:, 0]  
        except:
            samples_sf = signal

        data=[convert_to_decibel(i) for i in samples_sf]
        data_train.append(round(np.mean(data), 2)) #trung binh
        data_train.append(round(np.median(data), 2))#trung vi
        data_train.append(round(np.std(data), 2))#Do lech chuan
        data_train.append(round(np.var(data), 2))# Phuong sai
        x_input.append(data_train)
    return x_input

#mo hinh no-ron
def hard_lim(x):
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
    return w_new
def update_bias(b_old, error):
    b_new = b_old + error
    return b_new

def TEST(file, w_weight, bias):
    file_n = []
    try:
        file_n.append(file)
        ex = data_process(file_n)
        neural = Neural(ex[0], w_weight, bias)
        result = neural.output()
    except:
        result = -1
    if result == 0:
        print(file, '==> ĐÂY LÀ CON MÈO')
    elif result == 1:
        print(file, '==> ĐÂY LÀ CON CHÓ')
    else:
        print(file, "==> KHÔNG NHẬN DẠNG ĐƯỢC ĐÂY LÀ CON GÌ!")
def check_input(file, file_train, x_inputs):
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
        print("Cac file test khac voi du lieu huan luyen!")
    else:
        print("Bi trung voi du lieu huan luyen!")

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
    file_test = ['soundtest1.wav', 'soundtest11.wav', 'soundtest3.wav', 'soundtest4.wav', 
                 'soundtest5.wav', 'soundtest15.wav', 'soundtest7.wav', 'soundtest8.wav', 
                 'soundtest13.wav', 'soundtest10.wav']
    epoch = 1000000000000
    print("Start processing data..........")
    x_inputs = data_process(file_train)
    print("x_inputs = ", x_inputs)
    print("Complete.")
    print()
    w_weights = [0.5, 0.6, -1, 1]
    bias = 0.7
    t1 = time.time()
    print('Start training .............')
    for i in range(0, epoch + 1):
        Y = []
        for x, t in zip(x_inputs, target):
            neural = Neural(x, w_weights, bias)
            output = neural.output()
            error = cal_error(output, t)
            Y.append(output)
            if output != t:
                w_new = update_weight(w_weights, x, error)
                b_new = update_bias(bias, error)
                w_weights = w_new
                bias = b_new
        if (Y == target):
            t2 = time.time()
            print("Processing to train complete in epoch ",i + 1)
            print(f"After {round((t2 - t1), 2)}s")
            print('Y = ',Y)
            print("Updated weight: ", w_weights)
            print("Updated bias: ", bias)
            print()
            break
    
    file = input('Nhập vào file muốn test: ')
    print('start checking input data.........')
    check_input(file, file_train, x_inputs)
    print('Complete!')
    print()
    print('Start testing process........')
    TEST(file, w_weights, bias)
    print('Nhập sai vui lòng nhập lại!')
    """ for file in file_test:
        TEST(file, w_weights, bias) """
    print('Complete testing!')