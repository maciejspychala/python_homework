from pylab import *
import skimage
from skimage import data, io, filters, exposure, feature, morphology
from skimage.filters import rank
from skimage.util.dtype import convert
from skimage import img_as_float, img_as_ubyte
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
from skimage.filters.edges import convolve
from matplotlib import pylab as pl  
import numpy as np
from numpy import array
from IPython.display import display
from ipywidgets import interact, interactive, fixed
from IPython.core.display import clear_output


names = ['./samolot00.jpg', './samolot01.jpg', './samolot02.jpg', './samolot03.jpg', './samolot04.jpg', './samolot05.jpg']

def show(filename, *args):
    pl.figure(figsize=(20,12))
    for i,img in enumerate(args):
        pl.subplot(1, len(args), i+1)
        io.imshow(img)
        pl.savefig(filename)


def sh_im(name):
    image = io.imread(name, as_grey=True)
    sob = filters.sobel(image)**0.5
    data = []
    for i in sob:
        tab = []
        for x in i:
            if x > 0.25:
                tab.append(1.0)
            else:
                tab.append(0.0)
        data.append(tab)
    datanp = np.array(data, dtype=np.float64)    
    binary = datanp > 40
    show("edge" + name[9:11], sob, datanp) 

for i in range(6):
    sh_im(names[i])
