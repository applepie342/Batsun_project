# Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок
# стоит B рублей. Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также
# во сколько раз шоколадные конфеты дороже ирисок.


choco_kg = input("Введите количество килограмм шоколадных конфет: ")
while type(choco_kg) != int:  # обработка исключений
    try:
        choco_kg = int(choco_kg)
    except ValueError:
        print("Неправильно ввели!")
        choco_kg = input("Введите количество килограмм шоколадных конфет: ")
choco_cost = input("Введите их стоимость: ")
while type(choco_cost) != int:  # обработка исключений
    try:
        choco_cost = int(choco_cost)
    except ValueError:
        print("Неправильно ввели!")
        choco_cost = input("Введите стоимость шоколадных конфет: ")
toffee_kg = input("Введите количество килограмм ирисок: ")
while type(toffee_kg) != int:  # обработка исключений
    try:
        toffee_kg = int(toffee_kg)
    except ValueError:
        print("Неправильно ввели!")
        toffee_kg = input("Введите количество килограмм ирисок: ")
toffee_cost = input("Введите их стоимость: ")
while type(toffee_cost) != int:  # обработка исключений
    try:
        toffee_cost = int(toffee_cost)
    except ValueError:
        print("Неправильно ввели!")
        toffee_cost = input("Введите стоимость ирисок: ")
one_choco_cost = round(choco_cost / choco_kg, 2)
one_toffee_cost = round(toffee_cost / toffee_kg, 2)
print("Один килограмм шоколадных конфет стоит ",  one_choco_cost, "рублей")
print("Один килограмм ирисок стоит ", one_toffee_cost, "рублей")
print("Шоколадные конфеты дороже ирисок в ", round(one_choco_cost / one_toffee_cost, 2), "раз")
