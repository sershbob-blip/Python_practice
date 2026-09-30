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
# from urllib.parse import urlencode, quote
# params = {
#     'search': 'значение',
#     'page': 2,
#     'tags': ['python', 'programming'],
#     'sort': 'asc'
# }

# def clean_params(params:dict):
#   return {
#     k:v
#     for k,v in params.items()
#     if v is not None and v != '' and v != [] and v != {}
#   }

# def format_query(params: dict, 
#                  sort: bool = True, 
#                  skip_empty: bool = True):

#     if skip_empty:
#         params = clean_params(params)
    
#     if sort:
#         params = dict(sorted(params.items()))
    
#     return urlencode(params, doseq=True, quote_via=quote)

# query = format_query(params, sort = True, skip_empty = True)

# print(query)


'''
ДЗ
Строка JSON → словарь и обратно
Дана строка в формате JSON:

python
json_str = '{"name": "Alice", "age": 30, "city": "Moscow"}'
Преобразуй строку в словарь с помощью json.loads().
Добавь в словарь новое поле "country": "Russia".
Преобразуй словарь обратно в JSON‑строку (с отступами для читаемости) через json.dumps().
Выведи результат.
'''
# import json

# json_str = '{"name": "Alice", "age": 30, "city": "Moscow"}'

# dict_1 = json.loads(json_str)

# dict_1['country'] = 'Russia'

# result = json.dumps(dict_1, sort_keys=True, indent=4)

# print(result)

'''
ДЗ
 urllib.parse + JSON
Задача 3. Разбор URL и формирование JSON с параметрами
Дан URL:

python
url = "https://api.example.com/search?q=python&lang=ru&page=2&sort=desc"
С помощью urllib.parse.urlparse() разбери URL на части.
С помощью urllib.parse.parse_qs() извлеки query‑параметры в словарь.
Создай новый словарь, где:
base_url — схема + netloc + path,
params — словарь параметров,
raw_query — исходная query‑строка.
Преобразуй этот словарь в JSON‑строку и выведи.
'''
# import urllib.parse
# import json

# url = "https://api.example.com/search?q=python&lang=ru&page=2&sort=desc"
# sep_url = urllib.parse.urlparse(url)
# params = urllib.parse.parse_qs(sep_url.query)
# result = {
#   'base_url':f'{sep_url.scheme}://{sep_url.netloc}{sep_url.path}' ,
#   'params': params,
#   'raw_query': sep_url.query
# }

# result_json = json.dumps(result, ensure_ascii=False, indent=2)

# print(result_json)
'''
ДЗ
Чтение JSON из файла и вывод полей
Есть файл data.json (создай его вручную) с содержимым:

json
{
  "user": {
    "name": "Bob",
    "roles": ["admin", "editor"],
    "active": true
  },
  "version": 1
}
Прочитай файл и распарси его в словарь через json.load().
Выведи: имя пользователя, количество ролей, статус active.
Если ключа нет — выведи понятное сообщение, а не ошибку.
'''
# import json

# with open('instance.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# try:
#   for k, v in data['user'].items(): 
#     print(k, v)
# except:
#   print('Ошибка:ключ не найден')