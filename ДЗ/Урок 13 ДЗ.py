'''
Напишите класс Selector.
Экземпляр этого класса при инициализации получает список чисел. 
Вызов метода get_odds возвращает нечётные числа из первоначального списка, 
вызов get_evens — чётные.
'''

class Selector:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_odds(self):
        odds = []
        for i in self.numbers:
            if i%2==1:
                odds.append(i)
        return odds

    def get_evens(self):
        evens = []
        for i in self.numbers:
            if i%2==0:
                evens.append(i)
        return evens

numbers = Selector([1,2,3,4,5,7,8,9,10])

print(numbers.get_odds())

print(numbers.get_evens())
        
