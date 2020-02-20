# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:24:29 2019

@author: Vladimir
"""
import numpy as np
import math
import matplotlib.pyplot as plt

numMeasures = 100

degree = 5 #порядок полинома

def generateMeasures():
    measures = []
    r = np.random
    for i in range(0, numMeasures):
        ra = 50-r.randint(100)
        measures.append(ra)
    
    return measures

'''def divideMeasures(measures, ratio):
    r = np.random()
    train = []
    test = []
    numtest = len(measures)/ratio
    for i in range(1,numtest):
        pass
    indexes = []
    for i in range(1, len(measures)):
        pass
    return train, test'''

def generateFi(X):
    FI = []
    for j in X:
        strFi=[]
        for i in range(0,degree+1):
           strFi.append(math.pow(j, i)) 
        FI.append(strFi)
    return FI

def calculatePolynom(alpha, FI):
    return np.dot(alpha.transpose(), FI)


source = generateMeasures()
'''sTrain, sTest = divideMeasures(source, 0.7)
print(sTrain)
print(sTest)'''
x = range(100,len(source)+100)

#Вычислениёе коэффициентов полинома
FI = np.array(generateFi(x))
FIT = FI.transpose()
FIInv = np.linalg.inv(np.dot(FIT, FI))
alpha = np.dot(FIInv, FIT)
alpha = np.dot(alpha, source)

#Вычисление значений полинома
Y = calculatePolynom(alpha, FIT)

#Рисуем график
fig = plt.figure()
plt.scatter(x, source)
plt.plot(x, Y)
plt.show()

