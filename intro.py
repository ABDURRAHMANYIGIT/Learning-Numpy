# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(9).reshape(3,3)#boyutlara bölüyor.
print(a)
print(type(a))
print(a.ndim)

b = np.arange(10)
print(b.shape)
print(b.ndim)#kaç boyutlu olduğunu gösteriyor.