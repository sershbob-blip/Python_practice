# class Fruit:
#     pass

# a = Fruit()
# b = Fruit()

# a.name = 'apple'
# a.weight = 120

# b.name = 'orange'
# b.weight = 150

# print (a.name, a.weight)
# print (b.name, b.weight)

# b.weight -= 10
# print (b.name, b.weight)

# c = Fruit()
# c.name = 'lemon'
# c.color = 'yellow'

# print(c.name, c.weight)

# class Greeter:
#     def hello_world (self):
#         print ('Привет, Мир')

#     def greeting (self,name):
#         '''Поприветствовать человека с именем name.'''
#         print ('Привет, {}!'.format(name))

#     def start_talking (self, name, weather_is_good):
#         '''Поприветствовать и начать разговор с вопроса о погоде.'''
#         print ('Привет, {}'.format(name))
#         if weather_is_good:
#             print ("Хорошая погода, не так ли?")
#         else:
#             print ("Отвратительная погода, не так ли?")

# greet = Greeter()
# # greet.hello_world()
# # greet.greeting('Петя')

# greet.start_talking('Саша', True)

class Car:
    def __init__ (self, color):
        self.engine_on = False
        self.color = color

    def start_engine(self):
        self.engine_on = True

    def drive_to (self, city):
        if self.engine_on:
            print ('{} car drive to city {}.'.format(self.color, city))
        else:
            print ('{} car isn`t started, so we`re not going anywhere'.format(self.color))

car1 = Car('red')

car2 = Car('blue')

car1.start_engine()

car1.drive_to ('Vladivostok')

car2.drive_to ('Lissabohn')