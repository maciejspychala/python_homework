from scipy import ndimage
import skimage
from skimage import data, io, filters, exposure, feature, morphology
from matplotlib import pylab as plt  
import numpy as np
from numpy import array


names = ['./samolot00.jpg', './samolot01.jpg', './samolot02.jpg', './samolot03.jpg', './samolot04.jpg', './samolot05.jpg', './samolot07.jpg', './samolot08.jpg', './samolot09.jpg', './samolot10.jpg', './samolot11.jpg', './samolot12.jpg', './samolot13.jpg', './samolot14.jpg', './samolot16.jpg', './samolot17.jpg', './samolot18.jpg', './samolot20.jpg']

def show(filename, *args):
    pl.figure(figsize=(20,12))
    for i,img in enumerate(args):
        pl.subplot(2, len(args)/2 + len(args)%2, i+1)
        io.imshow(img)
        pl.savefig(filename)



def get_objects(name):
    image = io.imread(name);
    true_color = np.copy(image)
    image = image[:,:,1]
    data = []
    sob = filters.sobel(image)**0.8
    for i in sob:
        tab = []
        for x in i:
            if x > 0.08:
                tab.append(1.0)
            else:
                tab.append(0.0)
        data.append(tab)
    datanp = np.array(data, dtype=np.float64)    
    filled_holes = ndimage.binary_fill_holes(datanp)
    without_dots = ndimage.binary_opening(filled_holes)
    without_small = morphology.remove_small_objects(without_dots, 900)
    return without_small, true_color

def show_all():
    fig = plt.figure(figsize=(72,36), frameon=False)
    print(len(names))
    for i, name in enumerate(names):
        print(i)
        plot = fig.add_subplot(3,6,i+1)
        objects, color = get_objects(name)
        plot.imshow(color)
        contours = skimage.measure.find_contours(objects, 0.2)
        plot.imshow(color)
        for n, contour in enumerate(contours):
            plot.plot(contour[:,1],contour[:,0],linewidth=2)
            plot.plot(np.mean(contour[:,1]), np.mean(contour[:,0]), 'ow')
        plt.axis('off')

    plt.savefig("allplanes.pdf")


def sh_im(name):
    ege = skimage.filters.sobel(lolol)
    gege = gege > 0.05

    contours = skimage.measure.find_contours(lolol, 0.2)
    fig, ax = plt.subplots()
    ax.imshow(heh2, interpolation='nearest', cmap=plt.cm.gray)
    print(len(contours))
    for n, contour in enumerate(contours):
            ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
    plt.show()

    show("edge" + name[9:11], heh2, heh2, heh2, heh2)

show_all()
