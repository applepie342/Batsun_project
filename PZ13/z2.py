# В матрице найти сумму отрицательных элементов в первой трети матрицы.

# table = [[x * y for x in range(-5, 3)] for y in range(-3, 6)]
# print(table)
#
# data = [stroka for stroka in table if table.index(stroka) in range(0, len(table) // 3)]
# print(data)
#
#
# minus = [x for x in data]
# print(minus)
import random

rows = 3
cols = 4

matrix = [[random.randint(-15, 15) for _ in range(cols)] for _ in range(rows)]
print(matrix)

summa = 0
for row in matrix:
    if matrix.index(row) in range(0, len(matrix) // 3):
        minus = [num for num in row if num < 0]
        for element in minus:
            summa += element
print("Сумма отрицательных элементов в первой трети матрицы равна ", summa)
