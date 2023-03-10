#Задача 36
#Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
#Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
#Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
#Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
#Пример:
#Ввод:
#print_operation_table(lambda x, y: x * y)

column = int(input("Введите количество колонок: "))
line = int(input("Введите количество строк: "))
matrix = []
for i in range(1, line):
    temp = []
    for j in range(1, column):
        temp.append(i * j)
    matrix.append(temp)   
for i in matrix:
    print(''.join(f'{n:<3}' for n in i))