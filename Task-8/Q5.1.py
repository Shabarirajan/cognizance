# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:50:22 2022

@author: SHABARIRAJAN KJ
"""
# addition of 2 numpy arrays

import numpy as np
 
a = np.array([4, 2, 4])
b = np.array([2, 4, 2])
   
print ("1st array : ", a)  
print ("2nd array : ", b)  
   
c = np.add(a, b)  
print ("added array : ", c)