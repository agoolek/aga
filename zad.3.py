# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:55:36 2023

@author: student
"""

class Property: 
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    
    def __str__(self):
        return f"Property:{self.area} m2, {self.rooms} rooms\n" \
                f"Price: {self.price} zl\n" \
                f"Adress: {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    
    def __str__(self):
        return f"House - {super().__str__()}\n" \
    
class FLat(Property):
    def __init__(self, area, rooms, price, address, floor):
            super().__init__(area, rooms, price, address)
            self.floor = floor
            
house1 = House(area=200, rooms=5, price=4000000, address="Miętowa 4", plot = 500)
flat1=  Flat(area=40, rooms=3, price=200000, address = "Lawendowa 5", floor = 3)

print(house1)
print(flat1)