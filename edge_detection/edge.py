from pylab import *
from scipy import ndimage
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
    pl.figure(figsize=(30,14))
    for i,img in enumerate(args):
        pl.subplot(1, len(args), i+1)
        io.imshow(img, interpolation="Gaussian")
        pl.savefig(filename)


def sh_im(name):
    image = io.imread(name);
    heh = image
    image = image[:,:,2]
    data = []
    sob = filters.sobel(image)**0.5
    for i in sob:
        tab = []
        for x in i:
            if x > 0.35:
                tab.append(1.0)
            else:
                tab.append(0.0)
        data.append(tab)
    datanp = np.array(data, dtype=np.float64)    
 
    edge_horizont = ndimage.sobel(datanp, 0)
    edge_vertical = ndimage.sobel(datanp, 1)
    magnitude = np.hypot(edge_horizont, edge_vertical)
    magnitude = magnitude > 0.95
    eroded_square = ndimage.binary_erosion(magnitude)
    reconstruction = ndimage.binary_propagation(eroded_square, mask=magnitude)
    magnitude2 = ndimage.binary_closing(magnitude)
    sob = filters.sobel(magnitude2)**0.5
    for i in range(len(heh)):
        for j in range(len(heh[0])):
            if datanp[i][j] == True:
                heh[i][j] = [255, 0, 0]
    show("edge" + name[9:11], datanp, magnitude2, heh)

for i in range(6):
    sh_im(names[i])
