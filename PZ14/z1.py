# Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
# произведения ими написанные. Посчитать общее количество произведений в данном
# файле.
import re

text = open("writer.txt", encoding='UTF-8')
z = re.compile(r"^[А-Я]\w+-*\w*", re.M)
r = re.compile(r"[0-9]+-[0-9]+")
k = re.compile(r"«.*?»")

p = re.compile(r'\n+')
with open('writer.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    stroka = re.split(p, text)
    a = k.findall(text)

s1 = map(lambda x: z.findall(x), stroka)
s2 = map(lambda y: r.findall(y), stroka)
s3 = map(lambda y: k.findall(y), stroka)

s = [element for element in zip(s1, s2, s3)]

for i in s[1:-1]:
    print(i, '\n')

print('Общее количество произведений равно', len(a))
