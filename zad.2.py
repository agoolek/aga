# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:53:47 2023

@author: student
"""

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\n" \
               f"Open hours: {self.open_hours}\n" \
               f"Phone: {self.phone}"
class Employee:
    def __init__ (self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):      
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
            return f"Employee: {self.first_name} {self.last_name}\n" \
                   f"Hire date: {self.hire_date}\n" \
                   f"Birth date: {self.birth_date}\n" \
                   f"Address: {self.city}, {self.street}, {self.zip_code}\n" \
                   f"Phone: {self.phone}"
class Book:
    def __init__ (self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
            return f"Book: {self.author_name} {self.author_surname}\n" \
                   f"Publication date: {self.publication_date}\n" \
                   f"Number of pages: {self.number_of_pages}\n" \
                   f"Library: {self.library}"
class Order:
    def __init__ (self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
            return f"Employee: {self.employee}\n" \
                   f"Student: {self.student}\n" \
                   f"Books:\n{', '.join(str(book) for book in self.books)}\n" \
                   f"Order Date: {self.order_date}"
                   
Library1 = Library("Tarnowskie Gory", "Miętowa", "17635", "9:00  - 17:00", "123-456-789")
Library2 = Library("Wrocław", "Słoneczna", "57632", "10:00 - 18:00", "784-345-122")

employee1 = Employee("Kamil", "Lech", "2022-04-23", "1988-04-01", "Łodź", "Lawendowa", "15677", "177-542-333")
employee2 = Employee("Justyna", "Marek", "2022-04-02", "1995-07-08", "Warszawa", "3 Maja", "54321", "484-875-606")
employee3 = Employee("Amelia", "Podsiadło", "2021-09-23", "1982-09-07", "Wrocław", "Lesna", "17645", "987-848-903")

book1 = Book(Library1, "1940-01-01", "Adam", "Mickiewicz", 270)
book2 = Book(Library1, "1845-02-01", "Juliusz", "Slowacki", 890)
book3 = Book(Library2, "2000-03-01", "Wislawa", "Szymborska", 360)
book4 = Book(Library2, "20205-04-01", "Jaroslaw", "SBorszewicz", 300)
book5 = Book(Library1, "1994-05-01", "Julian", "Tuwim", 18)

order1 = Order(employee1, "Adrian", [book1, book2, book3], "2022-02-01")
order2 = Order(employee2, "Janusz", [book4, book5], "2022-02-02")


print(order1)
print("\n---------------------\n")
print(order2)