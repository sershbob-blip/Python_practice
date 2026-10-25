#Напишите программу, которая с помощью цикла «переворачивает» строку. Например, из "привет" должно получиться "тевирп".
string = "привет"
string_reversed = ""
for i in string:
    string_reversed = i + string_reversed
print(string_reversed)


string = "привет"
string_reversed = ""
for i in range(len(string)-1, -1, -1):
    string_reversed += string[i]
print(string_reversed)

#Напишите программу, которая с помощью вложенных циклов выводит таблицу сложения для чисел от 1 до 5:

for i in range(0,6):
    for j in range(1,6):
        print(i + j, end ='\t')
    print()

# Напишите программу с циклом while, 
# которая запрашивает у пользователя пароль до тех пор, 
# пока он не введёт «qwerty123». После правильного ввода выведите «Доступ разрешён».

password = 'qwerty123'
while True:
    input_passw = input('Введите пароль ')
    if input_passw == password:
        print("Успешная авторизация")
        break
    else:
        print("Повторите попытку")