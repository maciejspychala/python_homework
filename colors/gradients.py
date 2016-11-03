#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

from matplotlib import colors

def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True) 
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')

def hsv2rgb(h, s, v): 
    c = v*s
    m = v-c
    h2 = h*6
    x = c*(1 - abs(h2 % 2 - 1))
    if h2 < 1:
        rgb = [c, x, 0]
    elif h2 < 2:
        rgb = [x, c, 0]
    elif h2 < 3:
        rgb = [0, c, x]
    elif h2 < 4:
        rgb = [0, x, c]
    elif h2 < 5:
        rgb = [x, 0, c]
    elif h2 < 6:
        rgb = [c, 0, x]
    else:
        rgb = [0, 0, 0]
    return(rgb[0] + m, rgb[1] + m, rgb[2] + m)

def gradient_rgb_bw(v):
    return (v, v, v)


def gradient_rgb_gbr(v):
    if v < 0.5:
        return (0, 1 - (v * 2), v * 2)
    else:
        return((v - 0.5) * 2, 0, (1-v) * 2)


def gradient_rgb_gbr_full(v):
    if v<1/4 :
        return(0,1,v*4)
    elif v<1/2:
        return(0,2 -(v*4),1)
    elif v<3/4:
        return((v*4)-2,0,1)
    else:
        return (1,0,4-(v*4))


def gradient_rgb_wb_custom(v):
    if v<1/7:
        return(1,1,1-(v*7))
    elif v<2/7:
        return(2-(v*7),1,0)
    elif v<3/7:
        return(0,1,(v*7)-2)
    elif v<4/7:
        return(0,4-(v*7),1)
    elif v<5/7:
        return((v*7)-4,0,1)
    elif v<6/7:
        return(1,0,6-(v*7))
    else:
        return(7-(v*7),0,0)


def gradient_hsv_bw(v):
    return hsv2rgb(0, 0, v)

def gradient_hsv_gbr(v):
    return hsv2rgb(v*(2/3)+(1/3), 1, 1)

def gradient_hsv_unknown(v):
    return hsv2rgb((1/3)-(v*(1/3)), 0.5, 1)

def gradient_hsv_map(v, value):
    return hsv2rgb((1/3)-(v*(1/3)), 0.9, value)

def gradient_hsv_custom(v):
    return hsv2rgb(v, 1-v, 1)

def display_map():
    width, height, distance, data = read_file()
    minimum, maximum = map_min_and_max(data)
    
    colored_map = []
    vectors = []
    for r in range(len(data)):
        color_tab = []
        vector_tab = []
        row = data[r]
        for i in range(len(row)):
            c = 0
            if (r < (height - 1)) and (i < (width - 1)):
                vec1=[distance, row[i+1]-row[i], 0]
                vec2=[0,data[r+1][i]-row[i],distance]
                normal = np.cross(vec1, vec2)
                light = [1,-1,-1]
                cosang = np.dot(normal, light)
                sinang = np.linalg.norm(np.cross(normal, light))
                c = np.cos(np.arctan2(sinang, cosang))
                c = (c+1)/2
            color_tab.append(gradient_hsv_map((float(row[i]-minimum)/(maximum-minimum)), c))
        colored_map.append(color_tab)
    plt.figure(figsize=(10, 10))
    plt.imshow(colored_map)

    plt.savefig('map.pdf')  


def map_min_and_max(data):
    minimum = data[1][1]
    maximum = data[1][1]
    for row in data:
        temp_min = min(row)
        temp_max = max(row)

        if temp_min < minimum:
            minimum = temp_min
        if temp_max > maximum:
            maximum = temp_max
    return minimum, maximum
    
    
    
def read_file():
    data = []
    with open('./big.dem') as f:
        for x in f.readlines():
            data.append(x.split())
    width = float(data[0][0])
    height = float(data[0][1])
    distance = float(data[0][2])
    distance = distance/100
    distance = 1
    data_float = []
    for row in data:
        data_float.append([float(i) for i in row])
    return width, height, distance, data_float[1:]

if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
    display_map()
