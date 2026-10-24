'''
from math import pi


class Circle:
    def __init__(self, radius):
        self.r = radius

        def area(self):
            return pi * self. r ** 2


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self. a * self. b


class Shape:
    pass
'''

# наследование

'''
class A:
    pass


class B (A):
    pass


class C:

    def foo(self):
        print('foo')


c = C()

c.foo()  # ok

c.bar()  # error
'''

'''
class BaseC:

    def bar(self):
        print('bar')


class C (BaseC):
    def foo(self):
        print('foo')


c = C()

c.foo()  # ok — этoт мeтoд ecть в пpoизвoднoм клacce

c.bar()  # ok — этoт мeтoд ecть в бaзoвoм клacce

c.baz()  # error
'''

class Shape:
    def describe(self):
# Aтpибyт __class__ coдepжит клacc или тип oбъeктa self    
# Aтpибyт __name__ coдepжит cтpoкy,
# в кoтopoй нaпиcaнo нaзвaниe клacca или типa
        print('Kлacc: {}'.format (self.__class__.__name__))


from math import pi


class Circle (Shape):

def __init__ (self, radius):

self. r = radius



def area (self):

return pi * self. r ** 2



class Rectangle (Shape):

def __init__ (self, a, b):

self. a = a

self. b = b



def area (self):

return self. a * self. b



shape = Shape ()

shape.describe ()



circle = Circle (1)

circle.describe ()



rectangle = Rectangle (1, 2)

rectangle.describe ()