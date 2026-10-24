def cached(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
        return result
    return wrapper


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(60))

'''
Векторы
Реализуйте класс Vector, который будет иметь 2 поля: x, y.
А также добавьте функции v.get () — возращает (x, y),
v1.sum (v2) — возращает сумму векторов.
'''


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def sum(self, v2):
        return (self.x + v2.x, self.y + v2.y)


v1 = Vector(2, 3)

v2 = Vector(4, 5)

print(v1.sum(v2))
