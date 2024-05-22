# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником.

class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def sr_ball(self):
        sred = sum(self.grades) / len(self.grades)
        print("Средний балл студента равен ", round(sred, 2))
        return sred

    def sucess(self):
        if self.sr_ball() == 5:
            print("Студент отличник")
        else:
            print("Студент не отличник")


student1 = Student("Иван", "Иванов", [5, 5, 5, 5, 5, 5, 5])
print(student1.__dict__)
# student1.sr_ball()
student1.sucess()
