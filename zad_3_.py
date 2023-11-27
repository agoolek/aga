# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:28:27 2023

@author: student
"""


def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


liczba = int(input("Podaj liczbę: "))
wynik = czy_parzysta(liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
