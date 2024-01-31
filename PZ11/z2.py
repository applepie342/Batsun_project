# Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме выведя строки в обратном порядке.

t = 0
for i in open('text18-2.txt', encoding='UTF-16'):
    print(i, end='')
    for j in i:
        if j in '.,!-…:':
            t += 1
print("Количество знаков препинания равно ", t)

f1 = open('text18-2.txt', encoding='UTF-16')
content = reversed(f1.readlines())
f2 = open('reversed_file.txt', 'w')
for line in content:
    f2.write(line)
f2.close()

