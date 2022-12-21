# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((2,3)))
b = np.floor(10*np.random.random((2,3)))

print(a)
print("***********")

print(b)
print("***********")

c = np.vstack((a,b))  #sütun sayısını değiştirmek istemediğinse kullanılır
print(c)              # vertical = dikey

print("***********")

d=np.hstack((a,b))  #satır sayısını değiştirmek istemediğinse kullanılır
print(d)            # horizontal = yatay
