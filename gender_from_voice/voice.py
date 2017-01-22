import matplotlib.pyplot as plt
import wave
import struct
from scipy import stats
import numpy as np
import sys


def get_data_and_framerate(filename):
    wav_file = wave.open(filename)
    (channels_numbers, _, frame_rate, frames_number, _, _) = wav_file.getparams()
    frames = wav_file.readframes(frames_number * channels_numbers)
    wav_file.close()
    data = struct.unpack_from("%dh" % frames_number * channels_numbers, frames)
    data = np.array(data)
    return data, frame_rate
    

def get_start_and_end(freqs, start_freq, end_freq):
    start_i = 0
    end_i = 0
    
    for i in range(len(freqs)):
        if freqs[i] > start_freq:
            start_i = i
            break
    for i in range(len(freqs)):
        if freqs[i] > end_freq:
            end_i = i
            break
    return start_i, end_i

def get_fft_and_freqs(data, frame_rate):
    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w), d = 1.0/frame_rate)
    return w, freqs

def get_fft_one_for_hz(w, freqs):

    start_i, end_i = get_start_and_end(freqs, start_freq, end_freq)

    freqs = freqs[start_i:end_i]
    w = w[start_i:end_i]
    w = np.abs(w)
    
    k = 0
    w2 = []

    for j in range(start_freq + 1, end_freq + 1):
        x = []
        while ((k < len(freqs)) and freqs[k] < j) :
            x.append(w[k])
            k = k + 1
        w2.append(np.mean(x))
    return w2


start_freq = 60
end_freq = 650

def smooth_array(array, margin, mode):
    array_smooth = []
    for i in range(len(array)):
        x = array[max(0, i-margin): min(len(array)-1, i+margin)]
        x = np.sort(x)
        array_smooth.append(np.mean(x[margin-mode : margin+mode]))
    return np.array(array_smooth)

def start(filename):
    data, frame_rate = get_data_and_framerate(filename)
    w, freqs = get_fft_and_freqs(data, frame_rate)
    w2 = get_fft_one_for_hz(w, freqs) 
    w_smooth = smooth_array(w2, 10, 2)
    stamp = w_smooth[0:200]
    index = 200
    maks = sum(stamp)
    for i in range(50, 250):
        suma = 0
        for j in range(200):
            suma += abs(stamp[j] - w_smooth[j+i])
        if suma < maks:
            index = i
            maks = suma
    gender = 'K'
    if (index) < 145:
        gender = 'M'
    print gender

def main():
    filename = sys.argv[1]
    start(filename)



if __name__ == '__main__':
    main()
