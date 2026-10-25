'''
Социальная сеть

В социальной сети есть два вида пользователей: люди и сообщества.
Все пользователи должны указывать свое имя.
Люди могут также указывать свою дату рождения, а сообщества — своё краткое описание.
Все пользователи (и люди, и сообщества) могут отправлять сообщения друг другу, 
а также выкладывать посты на своей стене.
Люди могут подписываться на других людей и на сообщества.
Реализуйте иерархию классов в соответствии с этим описанием.

User — базовый класс. Его конструктор должен принимать один аргумент — имя. 
Также этот класс должен предоставлять методы

send_message(user, message) — отправить сообщение message пользователю user

post(message) — отправить сообщение message себе на стену

info() — вернуть строку с дополнительной информацией о пользователе. 
Для класса User это пустая строка, метод info() будет переопределяться в производных классах

describe() — напечатать имя пользователя и дополнительную информацию о нем 
(т.е. результат работы метода info())

Person — производный от класса User. Его конструктор должен принимать на вход два аргумента — 
имя и дату рождения. Метод info() класса Person должен возвращать строку вида «Дата рождения:…» 
Также у Person должен быть реализован дополнительный метод subscribe (user), 
где user — объект класса User.

Community — производный от класса User. Его конструктор должен принимать на вход два аргумента — 
имя и краткое описание. Метод info() класса Community должен возвращать строку вида «Описание:…»
'''


class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        print(f'Отправить пользователю {user.name} сообщение: \"{message}\"')

    def post(self, message):
        print(f'Отправить сообщение на стену:\"{message}\"')

    def info(self):
        return ''

    def describe(self):
        print(f'{self.name}: {self.info()}')


class Person(User):
    def __init__(self, name, birthdate):
        super().__init__(name)
        self.birthdate = birthdate

    def info(self):
        return f'Дата рождения: {self.birthdate}'

    def subscribe(self, user):
        print(f'Подписан на пользователя {user.name}')


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f'Описание: {self.description}'


user_1 = User('Катя')

user_2 = Person('Ваня', '1996-01-02')

comm = Community('Котики', 'группа о милых котятах')

user_1.send_message(user_2, "привет!")

user_1.post("только зарегистрировалась")

user_1.describe()

print(user_2.info())

user_2.describe()

user_2.subscribe(user_1)

print(comm.info())

comm.describe()

user_1.send_message(comm, 'хочу на вас подписаться')
