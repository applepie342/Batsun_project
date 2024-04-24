# В матрице найти сумму отрицательных элементов в первой трети матрицы.
import random

rows = 3
cols = 4

matrix = [[random.randint(-15, 15) for x in range(cols)] for y in range(rows)]
print(matrix)

summa = 0
for row in matrix:
    if matrix.index(row) in range(0, len(matrix) // 3):
        minus = [num for num in row if num < 0]
        for element in minus:
            summa += element
print("Сумма отрицательных элементов в первой трети матрицы равна ", summa)
