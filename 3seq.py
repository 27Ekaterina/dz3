# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
# Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
# Введите элементы 2-го списка: 2,5
# Результат: 1,3,4

number_elements = input("Введите количество элементов 1го списка: ")
user_list = set()
while len(user_list) < int(number_elements):
    user_list.add(int(input("Введите элемент 1го списка: ")))
print(user_list)

number_elements2 = input("Введите количество элементов 2го списка: ")
user_list2 = set()
while len(user_list2) < int(number_elements2):
    user_list2.add(int(input("Введите элемент 2го списка: ")))
print(user_list2)

print("Первый список без элементов второго: ", user_list-user_list2)