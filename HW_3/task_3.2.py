# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

from random import randint

n = int(input("Введите количество элементов списка: "))

list = [randint(1, 10) for i in range(n)]
print(list)

num = int(input("Введите число: "))

result = min(list, key=lambda x: abs(x-num))
print(result)

