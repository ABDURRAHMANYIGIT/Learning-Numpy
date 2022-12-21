# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:14:21 2020

@author: imran
"""

import numpy as np

sayilar = np.array([1,2,3,4,5,6,7,8,9])
print(sayilar[::-1])
print(sayilar[2])
print(sayilar[0:2])

sayilar2 = np.array([[1,2,3],[7,8,9]])
print(sayilar2[:,0:2])
print(sayilar2[-1,:])
print(sayilar2[:,-1])
