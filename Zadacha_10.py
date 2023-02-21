#Задача 10
#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть.
#Пример:
#5 -> 1 0 1 1 0
#2

n = int(input("Введите количество монеток: "))
numOfReshko = 0
for i in range(0, n):
    import random
    storona = random.randint(0, 1)
    numOfReshko += storona #считаем сколько монет лежат решком вверх
    print(storona, end=" ")
numOfOrel = n - numOfReshko
#if numOfReshko >= numOfOrel:
    #print(numOfOrel)
print()
print(min(numOfOrel, numOfReshko))


