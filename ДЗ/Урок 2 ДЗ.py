# ДЗ
# Работа с множествами
# Напишите функцию common_elements(set1, set2), которая возвращает множество общих элементов двух множеств.

# Пример: common_elements({1, 2, 3}, {2, 3, 4}) → {2, 3}

# def common_elements(set1, set2):
#     common_set = set()
#     for x in set1:
#         if x in set2:
#             common_set.add(x)
#     return common_set

# print(common_elements({1, 2, 3, 5, 8, 7}, {2, 8, 3, 4, 5}))



# ДЗ
# Словари и списки
# Создайте функцию group_by_length(words), которая принимает список слов и возвращает словарь, где:

# ключ — длина слова;

# значение — список слов этой длины.

# Пример:

# python
# group_by_length(['cat', 'dog', 'elephant', 'ant'])
# Результат: {3: ['cat', 'dog', 'ant'], 8: ['elephant']}

# def  group_by_length(words: list[str]):
#     dict = {}
#     for word in words:
#         length = len(word)
#         if length not in dict:
#             dict[length] = []
#         dict[length].append(word)
#     return dict 
        

# print(group_by_length(['cat', 'dog', 'elephant', 'ant', 'lion']))
        


# ДЗ
#  Вложенные циклы и словари
# Напишите функцию count_letters(text), которая:

# принимает строку;

# с помощью вложенного цикла (или простого цикла) подсчитывает частоту каждой буквы (игнорируйте пробелы и регистр);

# возвращает словарь с буквами и их частотами.

# Пример: count_letters("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# def count_letters(text):
#     text = text.lower().replace(' ', '')
#     result = {}
#     count = 0
#     for l in text:
#         if l not in result:
#             result[l] = 1
#         else:
#             result[l] += 1

#     return result

# print(count_letters("  HE  Llo  56565656  lovely W o R L d"))


# ДЗ
# Кортежи и списки
# Создайте функцию swap_pairs(lst), которая принимает список чисел и возвращает новый список, 
# где соседние элементы поменяны местами. Если количество элементов нечётное, последний элемент остаётся на месте.

# Пример: swap_pairs([1, 2, 3, 4, 5]) → [2, 1, 4, 3, 5]

# def swap_pairs(lst: list[int]):
#     swap_lst = []
#     for i in range (0, len(lst), 2):
#         if i + 1 < len(lst):
#             swap_lst.append((lst[i], lst[i+1]))
#         else:
#             swap_lst.append((lst[i],))

#     result = []
#     for x in swap_lst:
#         if len(x) > 1:  
#             t_swapped = x[1], x[0]
#             t1, t2 = t_swapped
#             result.append(t1)
#             result.append(t2)
#         else:
#             t3, = x
#             result.append(t3)
    
#     return result

    
# print(swap_pairs([1, 2, 3, 4, 5]))


# def swap_pairs(lst: list[int]):
#     swap_lst = []
#     for i in range (0, len(lst), 2):
#         if i + 1 < len(lst):
#             swap_lst.append([lst[i], lst[i+1]])
#         else:
#             swap_lst.append([lst[i]])

#     result = []
#     for x in swap_lst:
#         if len(x) > 1:  
#             t_swapped = x[1], x[0]
#             t1, t2 = t_swapped
#             result.append(t1)
#             result.append(t2)
#         else:
#             t3, = x
#             result.append(t3)
    
#     return result

    
# print(swap_pairs([1, 2, 3, 4, 5]))


# ДЗ
# Множества и словари
# Напишите функцию unique_values_by_key(dict_list), которая принимает список словарей и возвращает словарь, где:

# ключ — ключ из исходных словарей;

# значение — множество уникальных значений для этого ключа.

# Пример:

# python
# data = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 30},
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Anny', 'age': 45}
# ]
# Результат: {'name': {'Alice', 'Bob'}, 'age': {25, 30}}

def unique_values_by_key(dict_list):
    result = {}
    for i in dict_list:
        for key, value in i.items():
            if key not in result:
                    result[key] = set()
            else:
                result[key].add(value)                           
    return result

# print(unique_values_by_key(data))


