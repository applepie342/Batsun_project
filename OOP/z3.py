class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1

    @staticmethod
    def total_people(first, second):
        return f"{first} {second}"


pers1 = Person("person 1")

