# -*- coding: utf-8 -*-
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

xs = np.arange(-6, 7, 0.1)
ys = 1 / (1 + np.exp(-xs))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_yticks([0, 0.5, 1.0])
ax.set_xticks([-6, -4, -2, 0, 2, 4, 6])
ax.set_ylabel(r"$\sigma(x)$")
ax.set_xlabel("x")
ax.grid(True)
ax.plot(xs, ys, linewidth=4)
plt.show()
