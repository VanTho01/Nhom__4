from pydub import AudioSegment
import numpy as np
import soundfile as sfile
import matplotlib.pyplot as plt

#filename = ['dog1.wav','cat2.wav', 'dog2.wav',
            #'cat1.wav', 'dog4.wav']
filename = ['cat2.wav']
mean = []
median = []
devitation = []
variance = []

x_inputs = []
def convert_to_decibel(arr):
        ref = 1
        if arr != 0:
            return 20 * np.log10(np.abs(arr) / ref)
        else:
            return -60
def average(a):
    return sum(a)/len(a)
for file in filename:
    x = []
    audio = AudioSegment.from_wav(file)
    samples = np.array(audio.get_array_of_samples())
    print(samples)
    signal, sr = sfile.read(file)
    samples_sf = 0
    try:
        samples_sf = signal[:, 0]  
    except:
        samples_sf = signal
    #print(samples_sf)

    print("Data of {}".format(file))
    data=[convert_to_decibel(i) for i in samples_sf]
    
    print(f"Mean : {np.mean(data)}") #phan vi 
    x.append(round(np.mean(data), 2))
    print(f"Median : {np.median(data)}") #trung vi
    x.append(round(np.median(data), 2))
    print(f"Standard Deviation : {np.std(data)}") # Do lech chuan
    x.append(round(np.std(data), 2))
    print(f"Variance : {np.var(data)}") # Phuong sai
    x.append(round(np.var(data), 2))
    x_inputs.append(x)
    print('========================================')

print("x_inputs = ", x_inputs)

plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(samples)
plt.xlabel('Samples')
plt.ylabel('Data: AudioSegment')

plt.subplot(3, 1, 2)
plt.plot(samples_sf)
plt.xlabel('Samples')
plt.ylabel('Data: Soundfile')

plt.subplot(3, 1, 3)
plt.plot(data)
plt.xlabel('Samples')
plt.ylabel('dB Full Scale (dB)')

plt.tight_layout()
plt.show()