from pydub import AudioSegment
import numpy as np
import soundfile as sfile
import time
from pydub.playback import play

#xu ly am thanh
def convert_to_decibel(arr): #tính giá trị decibel tương ứng với mẫu âm thanh
            ref = 1
            if arr != 0:
                return 20 * np.log10(np.abs(arr) / ref) #chuyển đổi từ dạng tuyệt đối của một số sang đơn vị Decibel 
            else:
                return -60
def data_process(filename):
    x_input = []
    for file in filename:
        sound = AudioSegment.from_file(file, format="wav")
        play(sound)
        data_train = []
        signal, sr = sfile.read(file) #đọc dữ liệu âm thanh bằng cách sử dụng thư viện 'soundfile', dòng này đọc dữ liệu âm thanh và tần số lấy mẫu
        samples_sf = 0 #khởi tạo biến samplerate = 0
        try:#kiểm tra xem âm thanh có nhiều kênh hay không
            samples_sf = signal[:, 0] #nếu có nhiều kênh thì được định dạng như một mảng 2 chiều, dòng này sẽ trích xuất âm thanh từ kênh đầu tiên 
        except:
            samples_sf = signal #nếu không có nhiều kênh, dữ liệu sẽ được trích xuất từ âm thanh đơn kênh

        data=[convert_to_decibel(i) for i in samples_sf] #thực hiện chuyển âm thanh sang đơn vị decibel bằng cách dùng hàm 'convert...' trên từng mẫu âm thanh trong 'sample_sf'
        #tính toán các giá trị thống kê và thêm vào list data_train
        data_train.append(round(np.mean(data), 2)) #trung binh
        data_train.append(round(np.median(data), 2))#trung vi
        data_train.append(round(np.std(data), 2))#Do lech chuan
        data_train.append(round(np.var(data), 2))# Phuong sai
        x_input.append(data_train) #thêm list data_train vào x_input ta được dữ liệu đầu vào cho mạng nơ - ron
    return x_input

#mo hinh no-ron
def hard_lim(x):
    if x >= 0:
        return 1
    else:
        return 0
class Neural: #xây dựng lớp nơ - ron
    def __init__(self, x_inputs, w_weight, bias): #thuộc tính của nơ - ron
        self.x_inputs = x_inputs
        self.w_weight = w_weight
        self.bias = bias
    def Sum_function(self): # phương thức tính tổng
        n = self.bias
        for x, w in zip(self.x_inputs, self.w_weight):
            n += x*w
        return n
    def output(self): #phương thức tính đầu ra
        a = hard_lim(Neural.Sum_function(self))
        return a
def cal_error(a, target): #hàm tính toán lỗi
    error = target - a
    return error
def update_weight(w_old, X, error): #hàm cập nhật trọng số
    w_new = []
    for w, x in zip(w_old, X):
        if error == 1:
            i = w + x
            w_new.append(i)
        elif error == -1:
            i = w - x
            w_new.append(i)
    return w_new
def update_bias(b_old, error): #hàm cập nhật bias
    b_new = b_old + error
    return b_new

def TEST(file, w_weight, bias):
    print('Start testing process........')
    file_n = []
    try:
        file_n.append(file)
        ex = data_process(file_n)
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
    print()
    print('What do you want in the next time?')

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
            print('Training success.')
            print()
            break
    print("=========*=============")
    print("--Enter: 'cnt' if you want to check and test file test\n--Enter: 'exit' if you want to get out of here")
    Selection(file_train, x_inputs, w_weights, bias) 
    
    