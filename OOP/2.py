class Note:
    def __init__(self, text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 1


note1 = Note("Задача 1")
note2 = Note("Задача 2")
# print(note1.text)
# print(note2.text)
# print(note1.__dict__)
# print(note2.__dict__)
# print(dir(note1))

# note1.upcount()
# print(note1.count)
# note1.upcount()
# print(note1.count)

print(note1.upcount)
print(Note.upcount)
