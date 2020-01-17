# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:12:42 2019

@author: Marcin
"""

from fractions import Fraction
dec = "t"
ulamki=[]
while dec=='t':
    a = input ('Podaj  ułamek w postaci a/b: ')
    a,b = a.split('/')
    a=int(a)
    b=int(b)
    ulamki.append((a,b))
    dec = input("czy chcesz podać kolejny ułamek? t/n: ")


suma=0
for a,b in ulamki:
    suma += Fraction(a,b)

    
print('Suma wynosi {}'.format(suma))