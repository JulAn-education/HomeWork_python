# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

n = int(input("Введите количество элементов списка: "))

list = [randint(1, 10) for i in range(n)]
print(list)

x = int(input("Введите число: "))

print(f"Число {x} встречается в списке {list.count(x)} раза")
