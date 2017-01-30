from pylab import *
from scipy import *
from numpy import *
import numpy as np

T = 1
w = 20

signal = lambda t : sin(2*pi*t) + sin(4*pi*t)
N = T * w
original = list(map(signal, linspace(0, T, N)))
figure()
subplot(211)
plot(original)

fft_table = np.fft.fft(original)
freqs = np.fft.fftfreq(len(fft_table), d = 1.0/w)
for i in range(len(freqs)):
    if abs(freqs[i]) == 2:
        fft_table[i] = 0

without2 = ifft(fft_table)
subplot(212)
plot(without2)
show()
