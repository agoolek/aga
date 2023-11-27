# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

    def __str__(self):
        return f'Czy {self.name} zdał/a? {self.is_passed()}'


Student1 = Student('Agata', [60, 60, 50, 60, 50])
Student2 = Student('Marta', [50, 40, 50, 40, 60])
print(Student1)
print(Student2)
