# normalize_names(names), которая:
# Принимает список строк names.
# Приводит каждое имя к нижнему регистру.
# Убирает лишние пробелы по краям.
# Возвращает новый список без пустых строк.
# Пример: [" Alice ", "bob", " ", "CHARLIE"] → ["alice", "bob", "charlie"].

def normalize_names(names: list[str]):
    new_list = []
    for name in names:
        name = name.lower().strip()
        if name:
            new_list.append(name)
    return new_list

print(normalize_names([" Alice ", "bob", " ", "CHARLIE"]))

def normalize_names(names):
    return [n.strip().lower() for n in names if n.strip()]

# print(normalize_names([" Alice ", "bob", " ", "CHARLIE"]))