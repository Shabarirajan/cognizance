# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:43:01 2022

@author: SHABARIRAJAN KJ
"""
import numpy as np
print()
print("Enter the number of elements in array 1:")
v = int(input())
print()
print("Enter the inputs for array 1:")
arr1 = input()
i = list(map(int,arr1.split(' ')))
print()
print("First array:")
print()
print(i)
print()
print("Enter the number of elements in array 2:")
f = int(input())
print()
print("Enter the inputs for array 2:")
arr2 = input()
e = list(map(int,arr2.split(' ')))
print()
print("Second array:")
print()
print(e)
print()
t = np.allclose(i, e)
print(t)
