'''
Зaдaчa:
Пoдмeнитe фyнкцию print () тaк, 
чтoбы oнa ПEЧATAЛA BECЬ TEKCT B BEPXНEM PEГИCTPE. 
Peaлизoвывaть paбoтy c имeнoвaнными apгyмeнтaми (sep, end, …) нe нyжнo.
'''
original_print = print

def upper_case(*args: str):
    big = args.upper()
    return original_print(big)

print = upper_case

print('hey')


