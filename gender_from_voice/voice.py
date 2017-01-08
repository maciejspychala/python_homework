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
end_freq = 350

def smooth_array(array, margin, mode):
    array_smooth = []
    for i in range(len(array)):
        x = array[max(0, i-margin): min(len(array)-1, i+margin)]
        x = np.sort(x)
        array_smooth.append(np.mean(x[margin-mode : margin+mode]))
    return np.array(array_smooth)

def open_file(filename):
    data, frame_rate = get_data_and_framerate(filename)
    w, freqs = get_fft_and_freqs(data, frame_rate)
    w2 = get_fft_one_for_hz(w, freqs) 
    fig = plt.figure()
    graph = fig.add_subplot(311)
    graph.plot(data)


    graph = fig.add_subplot(312)
    graph.bar(range(start_freq,end_freq), w2)

    w_mode = smooth_array(w2, 3, 1)

    graph = fig.add_subplot(313)
    graph.bar(range(start_freq,end_freq), w_mode)
    xx = 'K'
    xd = np.argmax(w_mode)
    print (xd + start_freq)
    if (xd+start_freq) < 140:
        xx = 'M'
    if xx in filename:
        print filename, 1
    else:
        print filename, 0
    plt.show()

def main():
    filename = sys.argv[1]
    open_file(filename)



if __name__ == '__main__':
    main()
