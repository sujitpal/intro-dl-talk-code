# -*- coding: utf-8 -*-
from __future__ import division, print_function
from sklearn import datasets
from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt

def plot_data(dataset):
    X = dataset[0]
    y = dataset[1]
    Xred = X[y==0]
    Xblue = X[y==1]
    plt.scatter(Xred[:, 0], Xred[:, 1], color='r', marker='o')
    plt.scatter(Xblue[:, 0], Xblue[:, 1], color='b', marker='o')
    plt.xlabel("X[0]")
    plt.ylabel("X[1]")
    plt.show()

def write_data(dataset, ofile):
    X = dataset[0]
    y = dataset[1]
    fout = open(ofile, "wb")
    for i in range(X.shape[0]):
        fout.write("%d,%.5f,%.5f\n" % (y[i], X[i, 0], X[i, 1]))
    fout.close()
    
def make_linear():
    blobs = datasets.make_blobs(n_samples=2000, random_state=0)
    plot_data(blobs)
    write_data(blobs, "../data/linear.csv")
    
def make_moons():
    moons = datasets.make_moons(n_samples=2000, random_state=0, noise=0.05)  
    plot_data(moons)
    write_data(moons, "../data/moons.csv")

def make_saturn():
    saturn = datasets.make_circles(n_samples=2000, factor=0.45, noise=0.05)
    plot_data(saturn)
    write_data(saturn, "../data/saturn.csv")

####################### main #######################
np.random.seed(0)
make_linear()        
make_moons()
make_saturn()

