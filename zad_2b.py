# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:53:05 2023

@author: student
"""

#pętla for

import random

l = [random.randint(0,100) for x in range(5)]
print('Wylosowane liczby:')
print(l)
for x in l:
    a=x*2
    m=[a]
    print(m)

lista1 = []
for liczba in lista1:
    nowalista1.append(liczba*2)
print(nowalista)

#lista składana

lista = [random.random() for x in range(5)]
print(l)
nowalista = [liczba * 2 for liczba in lista]
print(nowalista)