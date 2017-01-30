from pylab import *
from scipy import *
from numpy import *
import numpy as np

T = 1
w = 20
N = T * w
signal1 = lambda t : sin(2*pi*t) + sin(4*pi*t)
signal2 = lambda t : sin(2*pi*t) + cos(4*pi*t)


def show_signal(signal):
    original = list(map(signal, linspace(0, T, N)))
    figure()
    subplot(411)
    plot(original)

    fft_table = np.fft.fft(original)
    freqs = np.fft.fftfreq(len(fft_table), d = 1.0/w)

    fft_table = fft_table[0:len(fft_table)/2]
    freqs = freqs[0:len(freqs)/2]

    subplot(412)
    stem(freqs, fft_table)

    subplot(413)
    stem(freqs, abs(fft_table))

    subplot(414)
    stem(freqs, arctan2(fft_table.imag, fft_table.real))
    show()

show_signal(signal1)
show_signal(signal2)

