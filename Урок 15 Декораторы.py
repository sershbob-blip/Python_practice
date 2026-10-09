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
