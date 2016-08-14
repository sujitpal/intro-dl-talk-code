# -*- coding: utf-8 -*-
from __future__ import division, print_function
from scipy.signal import convolve, convolve2d
import numpy as np

input = np.array([
    [255, 7, 3],
    [212, 240, 4],
    [218, 216, 230]])
filter = np.array([
    [-1, 1],
    [2, 3]])
# convolutions are applied using mirror image of filter, ie:
# filter' = np.array([
#    [3, 2],
#    [1, -1]])
c = convolve(input, filter, mode="same")
print(input)
print(c)
