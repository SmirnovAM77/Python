#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности

#Пример:
#4 -> 1 2 3 4
#9

n = int(input("Введите количество кустов (минимум 3 куста на ферме): "))
from random import randint 
list1 = [randint(1, n) for i in range(n)]
print(*list1)
k = 0
maxModul = 0
for i in range(1, len(list1) - 1):
    k = list1[i] + list1[i - 1] + list1[i + 1]
    if k > maxModul:
        maxModul = k
print(maxModul)
