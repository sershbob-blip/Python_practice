'''
Пароль для Фибоначчи

Напишите декоратор check_password, который запрашивает пароль,
прежде чем вызвать функцию,
и если он неверный — возвращает None и печатает «В доступе отказано».

Запарольте этим декоратором функцию вычисления числа Фибоначчи.
'''


def check_password(func):
    authorized = False

    def wrapper(*args, **kwargs):
        nonlocal authorized
        password = 'begin'

        if not authorized:
            input_passw = input('Введите пароль: ')
            if input_passw != password:
                print('В доступе отказано')
                return None
            authorized = True

        result = func(*args, **kwargs)
        return result
    return wrapper

# функция Фибонначчи


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


@check_password
@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(60))
