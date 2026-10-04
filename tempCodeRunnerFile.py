old_print = print

def print_upper_case (*args):

    argsUpcased = [str (arg).upper () for arg in args]

    old_print(*argsUpcased)

print = print_upper_case

print ('Нeльзя ли пoтишe?')