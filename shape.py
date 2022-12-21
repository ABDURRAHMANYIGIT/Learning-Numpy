# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((3,6)))

print(a)
print(a.shape)

#print(a.ravel()) #DÜZLEŞTİRİYOR

a = a.ravel()
print(a.shape)
#%%
a = a.reshape(2,9)
print(a)
print(a.T)#90 derece döndürüyor, çıktısını alırsan daha iyi anlayacaksın zaten
print(a.reshape(2,-1))# 2 tane satır oluştur gerisini sen istediğin gibi yap demek 
                      # istiyor, bunu da denersen daha iyi anlarsın, sürekli farklı değer döndürür.