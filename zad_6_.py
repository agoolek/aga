# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:48:23 2023

@author: student
"""

def przekształcenie(lista1, lista2):

    połączona_lista = list(set(lista1 + lista2))
    wynikowa_lista = [x**3 for x in połączona_lista]
    
    return wynikowa_lista

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

wynik = przekształcenie(lista1, lista2)
print(wynik)