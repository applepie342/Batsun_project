# Дан список размера N. Найти номера тех элементов списка, которые больше своего
# левого соседа, и количество таких элементов. Найденные номера выводить в
# порядке их убывания

import random

spisok = []
i = 0
while i < 10:
    spisok.append(random.randint(0, 30))
    i += 1
print(spisok)

numbers = []
for index in range(1, len(spisok)):
    if spisok[index] > spisok[index - 1]:
        numbers.append(index)

print("Номера элементов списка, которые больше своего левого соседа: ", sorted(numbers, reverse=True))
print("Количество таких элементов равно ", len(numbers))
