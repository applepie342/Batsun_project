class Note:
    def __init__(self, text, iscompleted):
        self.text = text
        self.count = 0
        self.iscompleted = iscompleted

    def upcount(self, value):
        self.count += value

    def reset_count(self):
        self.count = 0


note1 = Note("Задача 1", "true")
note1.upcount(5)
print(note1.__dict__)

note1.reset_count()
print(note1.__dict__)

