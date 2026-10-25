'''
# ДЗ
# Реализуй функцию stats_by_category(items), которая принимает список словарей вида:

'''
# РЕШЕНИЕ

categories = [
  {"name": "apple", "category": "fruit", "price": 10},
  {"name": "carrot", "category": "vegetable", "price": 5},
  {"name": "banana", "category": "fruit", "price": 8},
]

# '''
# Функция должна вернуть словарь, где ключ — категория, а значение — словарь с:
# "count": количество товаров в категории,
# "total_price": суммарная цена,
# "avg_price": средняя цена (округлить до 2 знаков).

# Если в категории нет товаров — не добавлять её.
# '''

def stats_by_category(items):
  #создадим словарь, который нужно вернуть функции
  result = {}
  for item in items:
    food = item['category']
    if food not in result:
        result[food] = {'count':0, 'total_price':0, 'avg_price':0}
    result[food]['count'] += 1
    result[food]['total_price'] += item['price']
    result[food]['avg_price'] = round(result[food]['total_price']/result[food]['count'], 2)   
       
  return result
            
print(stats_by_category(categories))

# Ошибки:
# - Всегда вводить переменные в разных циклах, не использовать старые переменные
# - В словаре нужно обращаться по ключу или значению, не всегда необходимо распаковывать словарь


'''
Задание:
Есть два списка: 

students = ["Анна", "Борис", "Виктор"] 
scores = [85, 92, 78]

Напиши функцию top_students(students, scores, k=2), которая:

Сопоставляет студентов и баллы через zip.

Сортирует по убыванию баллов.

Возвращает список из k лучших студентов (только имена)
'''

students = ["Анна", "Борис", "Виктор"] 
scores = [85, 92, 78]

def top_students(students, scores, k=2):
  top_list = list(zip(students, scores))
  sorted_list = sorted(top_list, key= lambda x: x[1], reverse=True)
  student, score = (zip(*sorted_list))
  # result = []
  # for x in range(len(student)):
  #   x = student[x]  
  #   result.append(x)
  result = [student[x] for x in range(len(student))]

  return result[:k]

print(top_students(students, scores))



'''
Написать функцию, которая принимает на вход натуральное число N
и возвращает список простых чисел от 1 до N.
'''