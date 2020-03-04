# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:06:22 2020

@author: Vladimir
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB

def convert(data, columns):
    number=LabelEncoder()
    d = data.copy()
    for c in columns:
        d[c] = number.fit_transform(d[c])
    return d

path = "C:\\Users\\Vladimir\\Desktop\\datamining data\\"
dataset = "crx.data"

column_names=["a"+str(i) for i in range(0,16)]
crx = pd.read_csv(path+dataset, names=column_names)

print(crx.head())

cn=["a0", "a3", "a4", "a5", "a6", "a8", "a9", "a11", "a12"]
crx_conv = crx.copy()
crx_conv = convert(crx_conv, column_names)

print(crx_conv.head())