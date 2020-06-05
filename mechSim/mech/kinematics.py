# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:59:20 2020

@author: Vladimir
"""

import math

class MaterialPoint_Linear():
    def __init__(self, pos, acc, direct):
        self.position = pos
        self.acceleration = acc
        self.direction = direct
        self.step_num = 1
        self.average_speed = math.sqrt(direct[0]**2+direct[1]**2)/self.step_num
        
    
    def setDirection(self, vec, dir_changed):
        if dir_changed == True:
            self.acceleration = vec-self.direction 
        self.direction = vec
        avg_s = math.sqrt(vec[0]**2+vec[1]**2)
        self.average_speed = (self.average_speed*self.step_num+avg_s)/(self.step_num+1)
        self.step_num+=1
        
    def setAcceleration(self, acc):
        self.acceleration = acc
    
    def move(self):
        self.position +=self.direction
        
        
                