import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Форма заявки приема на работу в зоопарке")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

contact_info = ttk.Labelframe(mainframe, text="Контактная информация")
contact_info.grid(column=0, row=0, sticky=(tk.W, tk.E))
ttk.Label(contact_info, text="Имя*").grid(column=1, row=1, sticky=tk.W)
name_entry = ttk.Entry(contact_info)
name_entry.grid(column=3, row=1)
ttk.Label(contact_info, text="Телефон").grid(column=1, row=2, sticky=tk.W)
phone_entry = ttk.Entry(contact_info)
phone_entry.grid(column=3, row=2)
ttk.Label(contact_info, text="Email*").grid(column=1, row=3, sticky=tk.W)
email_entry = ttk.Entry(contact_info)
email_entry.grid(column=3, row=3)

personal_info = ttk.Labelframe(mainframe, text="Персональная информация")
personal_info.grid(column=0, row=1, sticky=(tk.W, tk.E))
ttk.Label(personal_info, text="Возраст*").grid(column=1, row=1, sticky=tk.W)
age_entry = ttk.Entry(personal_info)
age_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
ttk.Label(personal_info, text="Пол").grid(column=1, row=2, sticky=tk.W)
gender_combobox = ttk.Combobox(personal_info, values=["Женщина", "Мужчина"])
gender_combobox.grid(column=2, row=2, sticky=(tk.W, tk.E))
ttk.Label(personal_info, text="Перечислите личные качества", wraplength=140).grid(column=1, row=3, sticky=tk.W)
qualities_text = tk.Text(personal_info, width=20, height=5)
qualities_text.grid(column=2, row=3, sticky=(tk.W, tk.E))

fav_animals = ttk.Labelframe(mainframe, text="Выберите ваших любимых животных")
fav_animals.grid(column=0, row=2, sticky=(tk.W, tk.E))
zebra_checkbox = ttk.Checkbutton(fav_animals, text="Зебра")
zebra_checkbox.grid(column=1, row=1, sticky=tk.W)
cat_checkbox = ttk.Checkbutton(fav_animals, text="Кошка")
cat_checkbox.grid(column=2, row=1, sticky=tk.W)
cat_checkbox = ttk.Checkbutton(fav_animals, text="Анаконда")
cat_checkbox.grid(column=3, row=1, sticky=tk.W)
cat_checkbox = ttk.Checkbutton(fav_animals, text="Человек")
cat_checkbox.grid(column=4, row=1, sticky=tk.W)
cat_checkbox = ttk.Checkbutton(fav_animals, text="Слон")
cat_checkbox.grid(column=1, row=2, sticky=tk.W)
cat_checkbox = ttk.Checkbutton(fav_animals, text="Антилопа")
cat_checkbox.grid(column=2, row=2, sticky=tk.W)
cat_checkbox = ttk.Checkbutton(fav_animals, text="Голубь")
cat_checkbox.grid(column=3, row=2, sticky=tk.W)
cat_checkbox = ttk.Checkbutton(fav_animals, text="Краб")
cat_checkbox.grid(column=4, row=2, sticky=tk.W)

submit_button = ttk.Button(mainframe, text="Отправить информацию")
submit_button.grid(column=0, row=3)

style = ttk.Style()
style.configure('.', font=('Arial', 14))

name_entry.focus()

root.mainloop()
