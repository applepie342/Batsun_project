# Дано целое число A. Проверить истинность высказывания: «Число A является
# нечетным»

a = input("Введите целое число: ")
while type(a) != int:  # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите целое число: ")
if a % 2 == 0:
    print("Число A четное")
else:
    print("Число А нечетное")
