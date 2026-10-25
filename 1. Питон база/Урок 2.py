# Вложенные циклы
# Напишите функцию print_multiplication_table(n), 
# которая с помощью вложенных циклов выводит таблицу умножения размером n×n

# def print_multiplication_table(n):
#     for t in range(1,n+1):
#         for i in range(1, n+1):
#             print(t*i, end='\t')
#         print()

# print_multiplication_table(6)

# Работа со списками
# Создайте функцию find_duplicates(lst), 
# которая принимает список и возвращает новый список с дублирующимися элементами 
# (каждый дубликат должен быть только один раз).

# Пример: find_duplicates([1, 2, 2, 3, 4, 4, 5]) → [2, 4]

def find_duplicates(lst):
    set_lst = set()
    set_dupl = set()
    for i in lst:
        if i not in set_lst:
            set_lst.add(i)
        else:
            set_dupl.add(i)
    return list(set_dupl)
        
lst = [1, 2, 2, 3, 4, 4, 5]
print(find_duplicates(lst))



