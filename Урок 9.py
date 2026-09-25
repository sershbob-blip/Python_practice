"""Цезарь 

Напишите функцию encrypt_caesar (msg, shift), 
которая кодирует сообщение шифром Цезаря и возвращает его. 
Шифр Цезаря заменяет каждую букву в тексте на букву с двигом по алфавиту (shift). 

Если сдвиг не указан, то пусть ваша функция кодирует сдвиг алфавита на 3 позиции: 
А →Г, Б →Д, В →Е, … Э →А, Ю →Б, Я →В
"""
def encrypt_caesar (msg, shift=3):

    msg = msg.upper()
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    letters = []
    for letter in msg:
        position = alphabet.find(letter)
        if position != -1:
            new_position = (position + shift) % len(alphabet)
            letters.append(alphabet[new_position])
        else:
            letters.append(letter)
    return ''.join(letters)

print(encrypt_caesar('Привет, мир!'))
