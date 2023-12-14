# Дан список размера N. Обнулить элементы списка, расположенные между его
# минимальным и максимальным элементами (не включая минимальный и
# максимальный элементы).

import random

spisok = []
i = 0
while i < 10:
    spisok.append(random.randint(0, 30))
    i += 1

print(spisok)

if (spisok.index(min(spisok)) + 1) < spisok.index(max(spisok)):
    for element in range(spisok.index(min(spisok)) + 1, spisok.index(max(spisok))):
        spisok[element] = 0
else:
    for element in range(spisok.index(max(spisok)) + 1, spisok.index(min(spisok))):
        spisok[element] = 0

print(spisok)
