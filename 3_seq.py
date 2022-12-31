
elem_1 = input("Введите элементы 1-го списка через запятую: ")
elem_1 = elem_1.split(',')

elem_2 = input("Введите элементы 2-го списка через запятую: ")
elem_2 = elem_2.split(',')
# Первый способ
result = []
for elem in elem_1:
    if elem not in elem_2:
        result.append(elem)
print(f"Результат с циклом for: {', '.join(result)}")

# Второй способ имеет недостаток удаляющий повторяющиеся элементы из списка.
set_elem_1 = set(elem_1)
set_elem_2 = set(elem_2)

set_elem_1.difference_update(set_elem_2)
print(f"Результат со множествами: {', '.join(set_elem_1)}")