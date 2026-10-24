from math import pi


class Circle:
    def __init__ (self, radius):
    self.r = radius

    def area (self):
        return pi * self. r ** 2


class Rectangle:
    def __init__ (self, a, b):
    self.a = a
    self.b = b

    def area (self):
        return self. a * self. b


class Shape:
    pass