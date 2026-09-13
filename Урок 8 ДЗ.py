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

!!!!!#написать функцию

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