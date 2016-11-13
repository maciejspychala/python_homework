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


names = ['./samolot00.jpg', './samolot01.jpg', './samolot02.jpg', './samolot03.jpg', './samolot04.jpg', './samolot05.jpg', './samolot06.jpg', './samolot07.jpg', './samolot08.jpg', './samolot09.jpg', './samolot10.jpg', './samolot11.jpg', './samolot12.jpg', './samolot13.jpg', './samolot14.jpg', './samolot15.jpg', './samolot16.jpg', './samolot16.jpg', './samolot17.jpg', './samolot18.jpg', './samolot19.jpg', './samolot20.jpg']

def show(filename, *args):
    pl.figure(figsize=(40,12))
    for i,img in enumerate(args):
        pl.subplot(1, len(args), i+1)
        io.imshow(img)
        pl.savefig(filename)


def sh_im(name):
    image = io.imread(name);
    heh = image
    heh2 = np.copy(image)
    image = image[:,:,1]
  
    data = []
    sob = filters.sobel(image)**0.7
    for i in sob:
        tab = []
        for x in i:
            if x > 0.1:
                tab.append(1.0)
            else:
                tab.append(0.0)
        data.append(tab)
    datanp = np.array(data, dtype=np.float64)    
    #edges2 = feature.canny(blured, sigma=3) 
    for i in range(len(heh)):
        for j in range(len(heh[0])):
            if datanp[i][j] == True:
                heh[i][j] = [255, 0, 0]
    xd = ndimage.binary_fill_holes(datanp)
    without_dots = ndimage.binary_opening(xd)
    xd = ndimage.binary_fill_holes(without_dots)
    without_dots = ndimage.binary_opening(xd)
    lolol = morphology.remove_small_objects(without_dots, 300)
    gege = skimage.filters.sobel(lolol)
    gege = gege > 0.05
    for i in range(len(heh2)):
        for j in range(len(heh2[0])):
            if gege[i][j] == True:
                heh2[i][j] = [255, 0, 0]
    
    show("edge" + name[9:11], heh, gege, heh2)

for i in range(len(names)):
    sh_im(names[i])
