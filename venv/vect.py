# -*- coding: utf-8 -*-
'''
>> Реализовать класс Vector на Python, реализующий работу с векторами на плоскости, поддерживающий следующие операции:
>>
>> * сложение и вычитание векторов
>> * вычисление модуля вектора
>> * умножение вектора на скаляр
>> * корректную репрезентацию вектора в виде строки
'''
import math

class Vector():
    def __init__(self, x, y):
        '''Constructor'''
        self.x = x
        self.y = y

    def value(self):
        '''Вернет значения X и Y'''
        return self.x, self.y

    def __add__(self, other):
        '''Слождение векторов'''
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''вычитание векторов'''
        return Vector(self.x - other.x, self.y - other.y)

    def module(self):
        '''Вычисление модуля'''
        # |a| = √ax2 + ay2 | Корень квадратный = z в степени 0.5
        return ((self.x**2) + (self.y**2))**0.5

    def scal(self):
        '''Умножение вектора на скаляр'''







#тесты
a = Vector(2, 4)
b = Vector(1, 3)
print(a)
c = a+b
print('valueeees', c.value())
print(c.x , c.y)
print('модуль' , a.module())
