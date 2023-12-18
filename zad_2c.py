# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:05:18 2023

@author: student
"""
import random
list = [random.randint(0, 100) for x in range(10)]
print(list)
parzyste = []
for el in list:
    if el % 2 == 0:
        parzyste.append(el)


print(parzyste)
