# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:38:11 2023

@author: student
"""
def sprawdź_sumę(a, b, c):
    suma_dwoch_pierwszych = a + b
    return suma_dwoch_pierwszych >= c

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))

wynik = sprawdź_sumę(liczba1, liczba2, liczba3)

if wynik:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej.")
else:
    print("Suma dwóch pierwszych liczb nie jest większa lub równa trzeciej.")