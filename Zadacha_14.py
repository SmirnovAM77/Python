#Задача 14
#Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
#Пример:
#10 -> 1 2 4 8

N = int(input("Введите число N: "))
print(f"{N} -> 1", end=" ")
for i in range(2, N, 2):
    print(i, end=" ")
