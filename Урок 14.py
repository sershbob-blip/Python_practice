# 1. Переопределение функций
def main_answer_in_the_universe():
    return 42

input = main_answer_in_the_universe
x = input()
print(x)

# теперь метод input() будет всегда автоматически выводить 42

# 2. Подменяем функцию print()
def nop(*rest, **kwargs):
    pass

print = nop

print('(whispering) Quiet, please!', end='')

# 3. Инструкция через def
def input():
    return 4

x = input()
print(x)


language = 'ru'

if language == 'ru':
    def hello(name):
        print('Привет,', name)
else:
    def hello(name):
        print('Hi,', name)

hello("Joe")

# 4. Локальная подмена функции

def answer (question):
    return 'in development'

def dialog():
    def answer(question):
        if question.lower().startswith('when'):
            return 'Never!'
        else:
            return 'They exposed me.'

    question = input()
    while question != '':
        print(answer(question))
        question = input()

dialog()