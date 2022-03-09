# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:49:41 2022

@author: SHABARIRAJAN KJ
"""

import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
y = ""
o = ser.str.title()
v = 0
while v < len(ser):
    y = y + o[v]
    y = y + " "
    v = v + 1
print(y)