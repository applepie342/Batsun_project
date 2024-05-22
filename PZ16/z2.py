# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_gender(self):
        print("Пол: ", self.gender)

class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age,"Мужской")

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age,"Женский")


pers1 = Human("Иван", "18", "Мужской")
pers2 = Man("Алексей", "19")
pers3 = Woman("Евгения", "20")

pers1.show_gender()
pers2.show_gender()
pers3.show_gender()