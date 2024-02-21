# Организовать и вывести последовательность А из n чисел (n - четное). Из
# последовательности А получить две последовательности В и С: в последовательности В –
# первая половина элементов А, в С – вторая половина элементов А. Найти произведение
# соответствующих элементов последовательностей В и С. Найти среднее арифметической
# полученной последовательности.
import random
from functools import reduce

A = set()
while len(A) < 10:
    A.add(random.randint(0, 30))
A = list(A)
print('A:', A)


B = [element for element in A if A.index(element) in range(0, (len(A) // 2))]
C = [element for element in A if A.index(element) in range(len(A) // 2, (len(A)) + 1)]
print('B:', B)
print('C:', C)

D = [x * y for x, y in zip(B, C)]
print('Произведение элементов B и C: ', D)
print('Среднее арифметическое полученной последовательности равно: ', reduce(lambda x, y: x + y, D) / len(D))
