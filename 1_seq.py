amount_elem = int(input("Введите количество элементов списка: "))
list_num = []
for i in range(1, amount_elem + 1):
    list_num.append(input(f"Введите {i} элемент списка: "))
list_num.sort()
print(list_num)