# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Произведение элементов меньших 0 в первой половине:
import random

spisok = []
i = 0
while i < 10:
    spisok.append(random.randint(-30, 30))
    i += 1

file = open("z1-1.txt", 'w')
for element in spisok:
    file.write(str(element))
    file.write(' ')
file.close()

file2 = open("z1-2.txt", 'w')
file2.write('Исходные данные: ')
for element in spisok:
    file2.write(str(element))
    file2.write(' ')
file.close()

file = open('z1-1.txt')
nums = file.read()
nums = nums.split()
for index in range(len(nums)):
    nums[index] = int(nums[index])
file.close()


t = 1
for index in range(len(nums) // 2):
    if nums[index] < 0:
        t *= nums[index]

file2 = open("z1-2.txt", 'a')
file2.write('\n')
print('Количество элементов: ', str(len(nums)), '\n', 'Максимальный элемент: ', str(max(nums)), file=file2)
print('Произведение элементов меньших 0 в первой половине: ', str(t), file=file2)
file2.close()
