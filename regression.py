# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:28:57 2020

@author: Vladimir
"""

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def K(x, xi, cs):
    if abs(x-xi)<=cs:
        return 3/4*(1-((x-xi)**2/cs))
    return 0

minX = -100
maxX = 100
x1 = np.array([i for i in range(minX, maxX)])
x2 = np.array([i for i in range(minX, maxX)])
x1 = x1/50.0
x2 = x2/50.0
y = []
ykt=[]
for i in range(0,len(x1)):    
    y.append((x1[i]+x2[i])**2+(rand.random()/2-0.5))
    #y.append((x1[i]+x2[i])**2+(rand.random()/2-0.5))



fig = plt.figure(0)
ax = fig.add_subplot(111,projection="3d")
ax.scatter(xs=x1, ys=x2, zs=y)  

#plt.figure(1)
 

print("Выборка:")
print("x1||x2||y")
for i in range(0,len(x1)):
    print("{0:.2f}||{1:.2f}||{2:.2f}".format(x1[i], x2[i], y[i]))
    
print("Настройка параметра размытия: {0}")

print("Параметр размытия: {0}".format(0))

print("Ядро: {0}".format(""))

print("Полученные значения:\nx1||x2||y")

print("Ошибка: {0}".format(0))