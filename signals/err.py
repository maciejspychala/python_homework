from pylab import *
import scipy.io.wavfile
import numpy as np
from scipy import *

w, sig = scipy.io.wavfile.read('err.wav')
sig = [s[0] for s in sig]
fourier = abs(np.fft.fft(sig))
freqs = np.fft.fftfreq(len(fourier), d = 1.0/w)

fig = plt.figure()
ax = fig.add_subplot(121)
ax.stem(freqs[0:len(freqs)/2:10], fourier[0:len(fourier)/2:10])

ax = fig.add_subplot(122)
ax.set_yscale('log')
ax.stem(freqs[0:len(freqs)/2:10], fourier[0:len(fourier)/2:10])
plt.show()
