# -*- coding: utf-8 -*-

import numpy as np

#(5-15) arasındaki sayılarla numpy dizisi oluşturunuz
a = np.arange(5,16)
#(50-100) arasındaki sayılarla 5 er 5 er atlayarak numpy dizisi oluşturunuz
a = np.arange(50,100,5)
#(0-100) arasında eşit aralıklarla 6 tane sayı üretin
a = np.linspace(0,100,5)
#(10-30) arasında rastgele 5 tane tam sayı üretin
a = np.random.randint(10,30,5)
#(-1 ile 1 ) arasında 10 tane sayı üretin
a = np.random.randn(10)
#(3x5) boyutunda (10-50) arasında rastgele bir matris oluşturunuz
b = np.random.randint(10,50,15).reshape(3,5)
#üretilen matrisin satır ve sütün sayılarının toplamlarını bulunuz
b = np.random.randint(10,50,15).reshape(3,5)
rowTotal = b.sum(axis = 1)
colTotal = b.sum(axis = 0)    # sum = toplama
print(rowTotal)    
print(colTotal)
#üretilen matrisin en büyük, en küçük, ortalaması nedir ?
a = b.max()
a = b.min()
a = b.mean()

#üretilen matrisin en büyük değerinin indexi kaçtır ?
print(b)
a = b.argmax()

#(10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçin
c = np.arange(10,20)
a = c[0:3]
#üretilen dizinin elemanlarını tersten yazdırın
a = c[::-1]
#üretilen matrisin ilk satırını seçin
a = b[0]
#üretilen matrisin 2. satır 3. elemanı nedir ?
a = b[1,2]
#üretilen matrisin tüm satırlarındaki ilk elemanı seçiniz
a = b[:,0]
#üretilen matrisin her bir elemanının karesini alınız
a = b**2
#üretilen matrisin elemanlarının hangisi pozitif çift sayıdır?
#aralığı (-50 , 50) yapınız

print(a)