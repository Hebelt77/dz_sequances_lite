num = input("Введите элементы списка через запятую: ")
print(num)

if ',' in num:
    num_revise = num.replace(',', '')
elif ';' in num:
    num_revise = num.replace(';', '')
elif '/' in num:
    num_revise = num.replace('/', '')
num_revise = set(num_revise)

print(f"Результат: {', '.join(num_revise)}")
