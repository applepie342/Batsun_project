# Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
# которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
# содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
# Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
# выбранная Специальность.
import sqlite3 as sq

with sq.connect('abiturient.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS anketa")
    cur.execute("""CREATE TABLE IF NOT EXISTS anketa (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    otchestvo TEXT NOT NULL,
    birthday TEXT NOT NULL,
    achievments TEXT,
    adress TEXT NOT NULL,
    speciality TEXT NOT NULL
    )""")

# with sq.connect('abiturient.db') as con:
#     cur = con.cursor()
#     cur.execute("INSERT INTO anketa VALUES ('1', 'Алексей','Иванов', 'Иванович', 'GRS', 'Да', 'Тургеневская', 'ИС')")

with sq.connect('abiturient.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM anketa")
    result = cur.fetchall()
    print(result)
