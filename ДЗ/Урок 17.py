from math import pi
from math import tan



class Shape:
    def describe(self):
        print(
            "Класс: {}\nПериметр: {}\nПлощадь: {}".format(
                self.__class__.__name__,
                self.perimeter(),
                self.area()
            )
        )


class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    def __init__(self, size):
        print("Создаём квадрат")
        super().__init__(size, size)


sq = Square(3)
sq.describe()

class Base1:
    def tic(self):
        print("tic")


class Base2:
    def tac(self):
        print("tac")


class Derived(Base1, Base2):
    pass


d = Derived()

d.tic()  # Метод, унаследованный от Base1
d.tac()  # Метод, унаследованный от Base2


class RegularPolygon:
    def __init__(self, side, n):
        self.side = side  # Длина стороны
        self.n = n  # Число сторон

    def inscribed_circle_radius(self):
        """Радиус вписанной окружности."""
        return self.side / (2 * tan(pi / self.n))


class Square(Rectangle, RegularPolygon):
    def __init__(self, a):
        # Явно вызываем конструкторы родительских классов
        Rectangle.__init__(self, a, a)
        RegularPolygon.__init__(self, a, 4)


s = Square(5)

s.describe()  # Метод, унаследованный от Shape через Rectangle
print(s.inscribed_circle_radius())  # Метод класса RegularPolygon