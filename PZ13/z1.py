# В матрице найти минимальный и максимальные элементы.
import random

rows = 3
cols = 4

matrix = [[random.randint(-15, 15) for _ in range(cols)] for _ in range(rows)]
print(matrix)
print('Максимальный элемент матрицы равен:', max(max(matrix)))
print('Минимальный элемент матрицы равен:', min(min(matrix)))
