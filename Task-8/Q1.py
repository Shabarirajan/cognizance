# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:30:04 2022

@author: SHABARIRAJAN KJ
"""
import numpy as np
l = int(input("Enter the first number:"))
o = int(input("Enter the first number:"))
v = o + 1
nums = np.arange(l,v)
print("Original array:")
print(nums)
e = 5
new_nums = np.zeros(len(nums) + (len(nums)-1)*(e))
new_nums[::e+1] = nums
print("\nNew array:")
print(new_nums)
