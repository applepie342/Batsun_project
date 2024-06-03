# Дано целое число A. Проверить истинность высказывания: «Число A является
# нечетным»
import tkinter as tk
from tkinter import ttk


def check_number():
    input_value = entry.get()
    try:
        number = int(input_value)
        if number % 2 == 0:
            result_label["text"] = "Число {} четное".format(number)
        else:
            result_label["text"] = "Число {} нечетное".format(number)
    except ValueError:
        result_label["text"] = "Неправильный формат числа"


root = tk.Tk()
root.title("Проверка на четность")
root.geometry('300x150')

input_label = ttk.Label(root, text="Введите целое число:")
input_label.pack()

entry = ttk.Entry(root)
entry.pack()

check_button = ttk.Button(root, text="Проверить", command=check_number)
check_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

style = ttk.Style()
style.configure('.', font=('Arial', 12))

root.mainloop()
