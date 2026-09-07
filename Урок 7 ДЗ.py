'''
ДЗ
Парсинг CSV строк
Задача:
Разработать функции для работы с CSV-строками:

Разбить строку на столбцы

Обработать кавычки внутри значений

Обработать разделители внутри кавычек

Преобразовать в словарь

Исходные данные:

python
csv_line = 'Имя,"Фамилия, Отчество",Возраст,Город'
values = 'Иван,"Петров, Сергеевич",25,"Москва, центр"'
Требования:

Разделитель — запятая

Кавычки экранируют специальные символы

Обработать пустые значения
'''

# csv_line = 'Имя,"Фамилия, Отчество",Возраст,Город'
# values = 'Иван,"Петров, Сергеевич",25,"Москва, центр"'

# def prepare_line(line:str) -> list[str]:
#     result = []
#     current = [] 
#     inside_quotes = False

#     for char in line:
#         if char == '"':
#             inside_quotes = not inside_quotes
#         elif char == ',' and not inside_quotes:
#             result.append(''.join(current).strip())
#             current  = []
#         else:
#             current.append(char)
#     result.append(''.join(current).strip())
#     return result

# def parsing_csv (csv_line:str, values:str) -> dict:
#     fst_column = prepare_line(csv_line)
#     snd_column = prepare_line(values)
#     if len(csv_line) < len(values):
#         snd_column.extend(['']*(len(fst_column) - len(snd_column)))
#     result = dict(zip(fst_column,snd_column))
#     return result

# print(parsing_csv(csv_line, values)) 
   

'''
ДЗ
Задача:
Разработать функции для работы с query-параметрами URL:

Извлечение параметров из строки

Преобразование в словарь

Обработка множественных значений

Декодирование URL-encoded символов

Исходные данные:

python
url = 'https://example.com?param1=value1&param2=value2&param1=value3'
encoded_url = 'https://example.com?param=%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5'
'''
# url = 'https://example.com?param1=value1&param2=value2&param1=value3'
# encoded_url = 'https://example.com?param=%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5'

# def url_params(url:str):
#     if '?' not in url:
#         return {}
    
#     query = url.split('?',1)[1]

#     params = {}
    
#     for pair in query.split('&'):
#         if '=' in pair:
#             key, value = pair.split('=',1)
#         else:
#             key, value = pair, ''
#         params.setdefault(key,[]).append(value)
    
#     return params

# from urllib.parse import urlparse, parse_qs, unquote
# decoded = unquote(encoded_url) #https://example.com?param=значение
# parsed = urlparse(url)
# params = parse_qs(decoded.query) #{'param1': ['value1', 'value3'], 'param2': ['value2']}

# print(params)

'''
ДЗ
 Формирование URL параметров
Задача:
Создать функции для формирования query-строки:

Кодирование специальных символов

Обработка списков значений

Сортировка параметров

Удаление пустых значений

Исходные данные:

'''
# from urllib.parse import urlencode
# params = {
#     'search': 'значение',
#     'page': 2,
#     'tags': ['python', 'programming'],
#     'sort': 'asc'
# }

# query = urlencode(params, doseq=True)

# print(query)

# #написать функцию

'''
ДЗ
Задача:
Создайте JSON-объекты для следующих сценариев:

Информация о студенте

Данные о книге

Простой список покупок

Пример:

python
'''

import json

# Создайте JSON-объект студента
student = {
    "name": "Иван",
    "age": 20,
    "courses": ["Математика", "Физика"],
    "average_grade": 4.5
}

# Создайте JSON-объект книги
book = {
    "title": "Война и мир",
    "author": "Л.Н. Толстой",
    "year": 1869,
    "pages": 1225
}
data = {
    "name": "Анна",
    "age": 21,
    "courses": ["Python", "SQL"],
    "active": True
}

book_jsn = json.dumps(book, ensure_ascii=False)
print(book_jsn)


credentials = json.loads(os.getenv("gs_key"))