from skimage import data,  morphology, measure
from matplotlib import pyplot as plt
import numpy as np
from skimage.morphology import disk
from skimage import filters
from scipy import ndimage as ndi



def centroid(contour):
    height = len(contour)
    xs = 0
    ys =0
    for i in range(height):
        xs+=contour[i][0]
        ys+=contour[i][1]

    return xs/height,ys/height

filenames = []

for i in range(21):
    if i>9:
        filenames.append("samolot" + str(i) + ".jpg")
    else:
        filenames.append("samolot0" + str(i) + ".jpg")


fig = plt.figure(figsize=(84,36))

for n,filename in enumerate(filenames):
    plot = fig.add_subplot(3, 7, n + 1)
    color_image = data.imread(filename)
    image = data.imread(filename)[:,:,0]

    image = filters.sobel(image)
    image = morphology.dilation(image, disk(3))

    thresh = filters.threshold_li(image)
    image = image > thresh

    label_objects, nb_labels = ndi.label(image)
    sizes = np.bincount(label_objects.ravel())
    mask_sizes = sizes > 2500
    mask_sizes[0] = 0
    image = mask_sizes[label_objects]

    image = ndi.binary_fill_holes(image)


    plot.imshow(color_image, interpolation='nearest', cmap=plt.cm.gray)
    contours = measure.find_contours(image, 0.8)

    for n, contour in enumerate(contours):
        if len(contour) > 325 and len(contour) != 1281 and len(contour) != 625 :
            print(filename + " " + str(len(contour)))
            y0, x0 = centroid(contour)
            plot.plot(x0, y0, '.w', markersize=15)
            plot.plot(contour[:, 1], contour[:, 0], linewidth=4)

    plot.set_xticks([])
    plot.set_yticks([])

plt.savefig("planes")























