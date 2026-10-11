old_print = print


def print_upper_case(*args):
    argsUpcased = [str(arg).upper() for arg in args]
    old_print(*argsUpcased)


print = print_upper_case
print('Нeльзя ли пoтишe?')


def use_uppercased_arguments(old_func):
    def new_func(*args, **kwargs):
        argsUpcased = [str(arg).upper() for arg in args]
        old_func(*argsUpcased, **kwargs)
    return new_func


print = use_uppercased_arguments(print)
print('Нельзя ли потише?')


def logged(func):
    count = 0

    def decorated_func(*args, **kwargs):
        nonlocal count
        count += 1
        print(count, '>>', 'Arguments:', args,
              'Named arguments:', kwargs)
        result = func(*args, **kwargs)
        print(' - ', 'Result:', result)
        return result
    return decorated_func


@logged
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print('Булочка')
    if withOnion:
        print('Луковые колечки')
    if withTomato:
        print('Ломтик помидора')
    print('Котлета из ', typeOfMeat)
    print('Булочка')


@logged
def drinking_type(type):
    return 'У на есть только чай'


make_burger('говядина', withOnion=True, withTomato=False)
drinking_type('вода')


def logged(func):
    count = 0 
    def decorated_func(*args, **kwargs):
        nonlocal count
        count += 1
        current_index = count
        print(current_index, '>>', 'Arguments:', args,
        'Named arguments:', kwargs)
        result = func(*args, *kwargs)
        print(current_index, ' - ', 'Result:', result)
        return result
    return decorated_func


@logged
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(5)


def power(degree):
    def func(x):
        return x**degree
    return func

square = power(2)
cube = power(3)

print(square(5))


def send_invitation(city, date, text):
    def sender(email, name):
        return send_invitation(email, name, text, date, city)
    return sender


sendmail = invitation_sender('Mocквa', '1 aпpeля 2017 г',

'Пpиглaшaeм вac нa вcтpeчy')

sendmail('vasiliy-petrov@yandex.ru', 'Bacилий Пeтpoв')

sendmail('petr-alekseev@yandex.ru', 'Пeтp Aлeкceeв')

sendmail('vasiliy-vasilyev@yandex.ru', 'Bacилий Bacильeв')
