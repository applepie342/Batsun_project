# Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
# информацию из строки в словарь, найти среднее арифметическое оценок,
# результаты вывести на экран.

info = {}
stroka = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'
stroka = stroka.split()
info['Фамилия'] = stroka[0]
info['Имя'] = stroka[1]
info['Группа'] = stroka[2]
info['Оценки'] = []
for element in stroka[3:]:
    info['Оценки'].append(int(element))
print(info)

print('Среднее арифметическое оценок равно', sum(info['Оценки'])/len(info['Оценки']))