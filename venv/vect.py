# -*- coding: utf-8 -*-
'''
>> Реализовать класс Vector на Python, реализующий работу с векторами на плоскости, поддерживающий следующие операции:
>>
>> * сложение и вычитание векторов
>> * вычисление модуля вектора
>> * умножение вектора на скаляр
>> * корректную репрезентацию вектора в виде строки
'''

class Vector():
    '''
    Класс для работы с векторами. Имеет функции:
    value() - Отображает значения X, Y
    Сложения/Вычитания ( + / - ) - складывает и вычитае векторы
    module() - Вычисление модуля (длины) вектора
    scal (x)- Умножение вектора на скаляр. x - скаляр
    repr() - Репрезентация в виде строки
    '''
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
        '''Вычисление модуля (длина вектора)'''
        # |a| = √ax2 + ay2 | Корень квадратный = z в степени 0.5
        return ((self.x**2) + (self.y**2))**0.5

    def scal(self, scal):
        '''Умножение вектора на скаляр'''
        if scal < 0:
            scal = abs(scal)
        return self.module() * scal

    def repr(self):
        '''Репрезентация вектора в виде строки'''
        return str('x = {0}, y = {1}') .format(self.x, self.y)
