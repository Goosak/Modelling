# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:06:22 2020

@author: Vladimir
"""

import numpy as np
import pandas as pd
from convert import convert

class NBClassifier:
    def __init__(self):
        self.all_var = 0
        self.freq_tabs = {}
        self.y_unique = []
        
    def fit(self, x, y): 
        self.y_unique = y.iloc[:, 0].unique()
        for c in x.columns:
            tab = game_train[[y.columns[0], c]].groupby([y.columns[0], c]).groups
            self.freq_tabs[c]={}
            for v in game_train[c].unique():
                self.freq_tabs[c][v]=list()
                for i in range(0,len(self.y_unique)):
                    if (self.y_unique[i], v) in tab:
                        self.freq_tabs[c][v].append(len(tab[(self.y_unique[i], v)]))
                    else:
                        self.freq_tabs[c][v].append(0)
            self.freq_tabs[c]["итого"]=list()
            for i in range(0,len(self.y_unique)):
                self.freq_tabs[c]["итого"].append(0)
                for j in game_train[c].unique():
                    self.freq_tabs[c]["итого"][i]+=self.freq_tabs[c][j][i]
    
        self.all_var = y.size
        
    def predict(self, x):
        normalize_confidences = list()
        for n in range(0, len(game_score)):
            game_str = game_score.iloc[n, :]
            normalize_confidences.append(list())
            confidences = list()
            for i in range(0,len(self.freq_tabs[next(iter(self.freq_tabs))]['итого'])):
                confidence = 1
                for c in game_score.columns:
                    confidence *= self.freq_tabs[c][game_str.get(c)][i]/self.freq_tabs[c]['итого'][i]
                confidence*=self.freq_tabs[next(iter(self.freq_tabs))]['итого'][i]/self.all_var
                confidences.append(confidence)

            for j in range(0, len(confidences)):
                normalize_confidences[n].append(confidences[j]/sum(confidences))
        game_column = list()
        for i in range(0,len(normalize_confidences)):
            ind =np.argmax(normalize_confidences[i])
            game_column.append(self.y_unique[int(ind)])
        return game_column
    
path = "datasets\\"
dataset_train="Irisy.xlsx"
dataset_score="Irisy2.xlsx"

game_train=pd.read_excel(path+dataset_train, id_column="ИД").iloc[:,1:]
game_score = pd.read_excel(path+dataset_score, id_column="ИД").iloc[:,1:]

x = game_train.loc[:, game_train.columns!="Название цвета"]
y = game_train.loc[:, game_train.columns=="Название цвета"]

nb = NBClassifier()
nb.fit(x,y)

print(nb.predict(game_score))