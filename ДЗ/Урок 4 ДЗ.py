'''
Написать функцию, которая принимает на вход натуральное число N
и возвращает список простых чисел от 1 до N.
'''
# def primes (n):
#     pr_list = []
#     for i in range (2, n+1):
#         is_prime = True
#         for j in range (2, int(i**0.5)+1):
#             if i%j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             pr_list.append(i)
#     if n > 0:
#         return pr_list
#     else:
#         print('Число не натуральное')

# print(primes(30))


'''
ДЗ
Слияние словарей
Есть два словаря с одинаковыми или разными ключами. Создай третий словарь, в котором:

если ключ есть только в одном словаре — бери его как есть;

если ключ встречается в обоих — в качестве значения возьми сумму значений.
'''
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
dict3 = {}

# for key1 in dict1:
#     if key1 not in dict2:
#         dict3[key1] = dict1[key1]

# for key2 in dict2:
#     if key2 not in dict1:
#         dict3[key2] = dict2[key2]

# for key1 in dict1:
#     if key1 in dict2:
#         dict3[key1] = dict1[key1] + dict2[key1]

d1 = {k:v for k, v in dict1.items() if k not in dict2} 
d2 = {k:v for k, v in dict2.items() if k not in dict1}
d3 = {k:dict1[k] + dict2[k] for k in dict1 if k in dict2}
# dict3.update(d1)
# dict3.update(d2)
# dict3.update(d3)
dict3 = {**d1,**d2,**d3}

sorted_dict3 = dict(sorted(dict3.items()))
print(sorted_dict3)  

'''
ДЗ
Словарь из двух списков
Даны два списка одинаковой длины: keys = ["a", "b", "c"], values = [1, 2, 3]. 
Создай словарь, где ключи — из первого списка, значения — из второго. 
Если длины не совпадают — выведи ошибку и не создавай словарь.
Что тренируется: zip, проверка длин, создание словаря.
'''
# keys = ["a", "b", "c", "d"]
# values = [1, 2, 3]
# def make_dict(keys: list, values:list):
#     if len(keys) == len(values):
#         dict_1 = dict(zip(keys, values))
#         return dict_1
#     else:
#         return 'Ошибка, длины списков не совпадают'
# print(make_dict(keys, values))

'''
ДЗ
 Отчёт по категориям с фильтрацией
Есть список транзакций:

python
transactions = [
    {"category": "еда", "amount": 300},
    {"category": "транспорт", "amount": 150},
    {"category": "еда", "amount": 200},
    {"category": "развлечения", "amount": 500},
]
Сгруппируй по category, посчитай сумму и количество транзакций. Верни словарь:

python
{
  "еда": {"total": 500, "count": 2},
  "транспорт": {"total": 150, "count": 1},
  ...
}
'''
# transactions = [
#     {"category": "еда", "amount": 300},
#     {"category": "транспорт", "amount": 150},
#     {"category": "еда", "amount": 200},
#     {"category": "развлечения", "amount": 500},
# ]

# def report_by_category(transactions):
#     result = dict()
#     for transaction in transactions:
#         category = transaction['category']
#         if category not in result:
#             result[category] = {'total' : 0, 'count' : 0}
#         result[category]['count'] += 1
#         result[category]['total'] += transaction['amount']
#     return result
# result = report_by_category(transactions)
# for key, value in result.items():
#     print(f"{key}: {value}")
        


 
'''
ДЗ
Условие.
У тебя есть список товаров (словари), у каждого есть поля: 
    name (название), category (категория), price (цена). 
Нужно построить «умный» прайс: сгруппировать товары по категориям, 
внутри каждой категории оставить только самый дешёвый товар, 
а также посчитать общее количество уникальных категорий и суммарную стоимость «самых дешёвых» товаров.

Входные данные:

python
products = [
    {"name": "Чай зелёный", "category": "напитки", "price": 250},
    {"name": "Кофе в зёрнах", "category": "напитки", "price": 400},
    {"name": "Батон нарезной", "category": "хлеб", "price": 60},
    {"name": "Хлеб цельнозерновой", "category": "хлеб", "price": 120},
    {"name": "Молоко 3.2%", "category": "молочка", "price": 90},
]
Требуемый результат:

Словарь best_in_category: ключ — категория, значение — словарь товара с минимальной ценой в этой категории.

Целое число total_categories — количество уникальных категорий.

Число total_cheapest_sum — сумма цен самых дешёвых товаров по всем категориям.
'''
from functools import reduce

products = [
    {"name": "Чай зелёный", "category": "напитки", "price": 250},
    {"name": "Кофе в зёрнах", "category": "напитки", "price": 400},
    {"name": "Батон нарезной", "category": "хлеб", "price": 60},
    {"name": "Хлеб цельнозерновой", "category": "хлеб", "price": 120},
    {"name": "Молоко 3.2%", "category": "молочка", "price": 90},
]
best_in_category = dict()

for dictionary in products:
    category = dictionary['category']
    if category not in best_in_category:
        category_products = [p for p in products if p['category'] == category] #фильтр по категориям не вставил
        min_price = reduce(lambda a, b: a if a['price'] < b['price'] else b, category_products)
        best_in_category[category] = min_price

total_cheapest_sum = 0
for p in best_in_category.values():
    total_cheapest_sum += p['price']


total_categories = 0
repeat_list = []
for dictionary in products:
    if dictionary['category'] not in repeat_list:
        repeat_list.append(dictionary['category'])
        total_categories += 1


for k, v in best_in_category.items():
    print(f'{k}:{v}')       
print(total_categories)
print(total_cheapest_sum)


        

