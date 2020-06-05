# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:19:02 2020

@author: Vladimir
"""
from math import exp

def Hevi(t): #функция Хевисайда
    if t<0:
        return 0.0
    elif t==0:
        return 0.5
    else:
        return 1.0

def xi_hevi(t):#для диф уравнения 2-го порядка с коэффициентами a=[21, 10, 1] при поданной на вход функции Хевисайда
    c1 = 5.0
    c2 = 2.0
    y_til = 1.0/7.0
    if t>0:
        y_til = 2.0/7.0 
    print(y_til)
    return c1*exp(-3*t)+c2*exp(-7*t)+y_til

def H(t_i, t, cs):#функция Соболева
    return 0

def k_s(t_i, t, cs, ki):#Вычисление переходной характеристики
    return 0

def x(t, dtau, tau, cs, ki):#Вычисление значений выхода модели
    return 0
