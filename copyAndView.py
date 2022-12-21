# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10)

b = a.copy()
print(a)
print(b)
b[0] = 1500
print(a)
print(b)

d = a.view()
print(a)
print(d)
d[0]=123
print(a)
print(d)
d.shape = 2,5
print(a)
print(d)
