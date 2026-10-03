'''
Маленький колокольчик
Напишите класс LittleBell, который при вызове метода sound печатает слово «ding».
'''
class LittleBell:

    def sound(self):
        print('ding')

bell = LittleBell()

# bell.sound()

'''
Большой колокольчик
Напишите класс BigBell, который при вызове метода sound печатает попеременно 
слова ding и dong, начиная c ding.
'''

class BigBell:

    def __init__(self):
        self.word = 'ding'

    def sound(self):
        if self.word == 'ding':
            print('ding')
            self.word = 'dong'
        else:
            print ('dong')
            self.word = 'ding'

bigbell = BigBell()

bigbell.sound()
bigbell.sound()
bigbell.sound()
bigbell.sound()