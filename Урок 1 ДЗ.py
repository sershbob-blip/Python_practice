# ДЗ
# Используя вложенные циклы for, выведите все возможные комбинации из двух букв русского алфавита (от «аа» до «яы»). 
# Ограничьтесь первыми 5 буквами («а», «б», «в», «г», «д») для упрощения.

# letters = ['а', 'б', 'в', 'г', 'д']
# for i in letters:
#     for j in letters:
#         print(i + j, end="  ")
        


# ДЗ
# Проверка пароля
# Напишите программу с циклом while, которая запрашивает у пользователя пароль до тех пор, пока он не введёт «qwerty123». 
# После правильного ввода выведите «Доступ разрешён».
# Счётчик попыток

# Модифицируйте предыдущую задачу: дайте пользователю только 3 попытки ввести пароль. 
# Если за 3 попытки пароль не угадан, выведите «Доступ запрещён». Используйте счётчик и break.


# password = 'qwerty123'
# count = 0
# while True:
#     input_passw = input('Введите пароль ')
#     if input_passw == password:
#         print("Доступ разрешен")
#         break
#     else:
#         count += 1
#         print(f"Повторите попытку. Осталось попыток: {3 - count}")
#         if count == 3:
#             print('Доступ запрещен')
#             break


# ДЗ
# Игра «Угадай число»
# Компьютер «загадывает» число от 1 до 20. С помощью цикла while дайте пользователю 5 попыток угадать это число. 
# После каждой попытки сообщайте, больше или меньше загаданное число. При успехе выводите «Вы угадали!» и прерывайте цикл с помощью break.


# import random

# number = random.randint(0, 20)
# count = 0

# while True:
#     input_num = int(input('Введите число '))
#     if number == input_num:
#         print("Вы угадали!")
#         break
#     elif input_num < number:
#             count += 1
#             print(f'Число больше. Осталось попыток: {5 - count}')
#             if count == 5:
#                 print ('Вы не угадали')
#                 break
#     elif input_num > number:
#             count += 1
#             print(f'Число меньше. Осталось попыток: {5 - count}')
#     elif count == 5:
#         print ('Вы не угадали')
#         break

    

# ДЗ
# Генератор паролей
# Напишите программу, которая генерирует 10 случайных паролей длиной 8 символов каждый. 
# Используйте цикл и модуль random. Пароли должны содержать буквы и цифры.

#ВАРИАНТ 1

# import random

# def passw_gen():
#     symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z',
#             'A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','U','W','X','Y','Z',
#                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     passw = ''
#     count_letters = 0
#     while count_letters < 8:
#         passw += random.choice(symbols)
#         count_letters +=1
#     print(passw)
#     return passw

# count_passw = 0

# while count_passw < 10:
#     password = passw_gen()
#     count_passw +=1


# ВАРИАНТ 2

# print(ord('['))

# import random

# def passw_gen():
#     low_letters = chr(random.randint(97, 122))
#     upper_letters = chr(random.randint(65, 90))
#     digits = random.randint(0, 10)
#     list_symbols = [str(low_letters), str(upper_letters), str(digits)]
#     random.shuffle(list_symbols)
#     passw = ''
#     count_letters = 0
#     while count_letters < 8:
#         passw += random.choice(list_symbols)
#         count_letters +=1
#     return passw



# passwords = []
# count_passw = 0

# while count_passw < 10:
#     password = passw_gen()
#     passwords.append(password)
#     count_passw +=1
# print(passwords)


# Напишите программу, в которой в бексонечном цикле пользователь вводит два числа, 
# а программа выводит их сумму. Затем программа запрашивает, надо ли завершить ввод. 
# И если пользователь вводит букву "Y" или "y", то происходит выход из бесконечного цикла, 
# и программа завершается. При нажатии любой другой клавиши, программа продолжает работу.

while True:
    num_1 = int(input("Первое число "))
    num_2 = int(input("Второе число "))
    print(f'Сумма: {num_1 + num_2}')
    print('Завершить программу? ')
    answ = input()
    if answ == 'y' or answ == 'Y':
        break


# Используя циклы, проверьте при помощи оператора in наличие символов строки 'abcde123' 
# в строке 'bad_cat_23', выводя результаты проверки на экран в виде «Символ "a" есть в "bad_cat_23".» 
# или «Символа "n" нет в "bad_cat_23".».

# string = 'abcde123'
# chk_string = 'bad_cat_23'

# for i in string:
#     if i in chk_string:
#         print(f'Символ "{i}" есть в "{chk_string}"')
#         print()
#     else:
#         print(f'Символа "{i}" нет в "{chk_string}"')
#         print()
      