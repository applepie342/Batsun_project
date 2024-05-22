# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате
import pickle

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

def save_def(*args):
    with open("students.pickle", "wb") as file:
        pickle.dump(args, file)

def load_def():
    with open("students.pickle", "rb") as file:
        data = pickle.load(file)
        return data


student1 = Student("Иван", "Иванов", [5, 5, 5, 5, 5, 5, 5])
student2 = Student("Сергей", "Сергеев", [5, 4, 4, 5, 5, 5, 3])
student3 = Student("Александр", "Александров", [3, 5, 4, 4, 3, 5, 4])

save_def(student1, student2, student3)

students = load_def()
for student in students:
    print("Имя: ", student.name, ", Фамилия: ", student.surname, ", Оценки: ", student.grades)