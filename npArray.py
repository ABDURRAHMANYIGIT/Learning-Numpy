# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1,2,5,6,8,9,7,3])
a = a.reshape(2,2,2)
print(a)
print(a.dtype)
print(a.ndim)

b = np.array([[3,2,3],[5,4,5],[7,8,4],[4,6,5]])
b = b.reshape(3,2,2)
print(b)
print(b.ndim)