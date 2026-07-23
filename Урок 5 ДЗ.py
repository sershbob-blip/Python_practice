'''
ДЗ
Пересечение и разность множеств
Цель: операции над множествами: &, -, | и т.п.

Даны два списка пользователей (логины):

python
list_a = ["alice", "bob", "charlie", "dave"]
list_b = ["bob", "dave", "eve", "frank"]
Преобразуй их в множества.

Найди пользователей, которые есть в обоих списках (пересечение).

Найди тех, кто есть только в list_a, но не в list_b (разность).

Выведи результаты как списки (отсортируй для наглядности).
'''
# list_a = ["alice", "bob", "charlie", "dave"]
# list_b = ["bob", "dave", "eve", "frank"]

# set_a = set(list_a)
# set_b = set(list_b)

# print(sorted(list(set_a & set_b)))
# print(sorted(list(set_a - set_b)))


'''
ДЗ
 List comprehension с условием и преобразованием
Цель: list comprehension с if и трансформацией значений.

Дан список температур в градусах Цельсия. Создай список температур в Фаренгейтах только для значений выше 0°C. 
Формула: F = C * 9/5 + 32.
'''
# temp_celsius = [-3.5, 0.0, 12.8, -7.2, 22.1, -1.5, 5.3, -10.0, 18.6, 6.7]

# temp_fahrenheit = [x*9/5 + 32 for x in temp_celsius if x > 0]

# print(temp_fahrenheit)

'''
ДЗ
Уникализация с сохранением порядка и подсчётом
Цель: убрать дубликаты, сохранив порядок первого появления, 
и посчитать, сколько раз каждый элемент встречался.

Дан список строк.

Верни список уникальных элементов в порядке первого появления.

Отдельно верни словарь: {элемент: количество}.

Пример:

python
data = ["A", "B", "A", "C", "B", "A"]
Результаты:

Уникальные по порядку: ["A", "B", "C"]

Счётчик: {"A": 3, "B": 2, "C": 1}

Можно сделать за один проход по списку.
'''
# data = ["B", "B", "A", "C", "B", "A"]
# unique_list = list()
# unique_dict = dict()
# for item in data:
#     if item not in unique_dict:
#         unique_dict[item] = 1
#     else:
#         unique_dict[item] += 1
#     if item not in unique_list:
#         unique_list.append(item)
    
# print(unique_list)
# print(unique_dict)
    

'''
ДЗ
Словарь через dict comprehension + фильтрация
Цель: dict comprehension и фильтрация по условию.

Дан список чисел. Создай словарь {число: квадрат числа} только для чётных чисел.

Пример:

python
nums = [1, 2, 3, 4, 5, 6]
Результат: {2: 4, 4: 16, 6: 36}
'''
# nums = [1, 2, 3, 4, 5, 6]
# result = {x:x**2 for x in nums if x%2 == 0}

# print(result)
'''
ДЗ
List comprehension со вложенными списками (flatten)
Цель: «расплющить» вложенный список в один плоский список.

Дан вложенный список:

python
nested = [[1, 2], [3, 4, 5], [6]]
С помощью list comprehension создай плоский список: [1, 2, 3, 4, 5, 6].

Подсказка: два for в одном comprehension.
'''
# nested = [[1, 2], [3, 4, 5], [6]]
# # result = []
# # for item in nested:
# #     for i in item:
# #         result.append(i)
# result = [x for item in nested for x in item]
# print(result)
'''
ДЗ
Словарь: ключи из одного списка, значения — списки из другого по правилу
Цель: сложная сборка словаря с группировкой.

Даны:

python
categories = ["fruit", "vegetable"]
items = [
    {"name": "яблоко", "category": "fruit"},
    {"name": "морковь", "category": "vegetable"},
    {"name": "банан", "category": "fruit"},
]
Создай словарь, где:

ключи — из categories,

значения — списки имён товаров соответствующей категории.
Если для какой-то категории товаров нет — значение должно быть пустым списком [].
'''

# categories = ["fruit", "vegetable", "berries"]
# items = [
#     {"name": "яблоко", "category": "fruit"},
#     {"name": "морковь", "category": "vegetable"},
#     {"name": "банан", "category": "fruit"},
#     {'name': None, 'category': 'berries'}
# ]
# result = dict()
# for cat in categories:
#     if cat not in result:
#         result[cat] = []
#     for item in items:
#         c = item.get('category')
#         i = item.get('name')
#         if i is not None and i not in result[cat] and c == cat: 
#             result[cat].append(i)
# print(result)







