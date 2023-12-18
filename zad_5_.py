# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:44:00 2023

@author: student
"""


def sprawdz_czy_zawiera(lista, szukana_wartosc):
    return szukana_wartosc in lista


moja_lista = [3, 7, 1, 8, 9, 2]
szukana = int(input("Podaj liczbę: "))

wynik = sprawdz_czy_zawiera(moja_lista, szukana)

if wynik:
    print(f"Lista zawiera wartość {szukana}.")
else:
    print(f"Lista nie zawiera wartości {szukana}.")
