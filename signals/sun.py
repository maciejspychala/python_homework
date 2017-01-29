from pylab import *
from scipy import *
import numpy as np

w = 12
T = 1
plt.figure()
array = genfromtxt('spots.txt')
signal = abs(np.fft.fft(array))
freqs = np.fft.fftfreq(len(signal), d = 1.0/w)
signal[0] = 0
max_signal = argmax(signal)

subplot(211)
plot(array)

subplot(212)
stem(freqs[0:len(freqs)/2], signal[0:len(signal)/2], 'r')

print(freqs[max_signal])
show()
