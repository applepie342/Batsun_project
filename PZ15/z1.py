# Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
# которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
# содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
# Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
# выбранная Специальность.
import sqlite3 as sq
from students import info_students


with sq.connect('abiturient.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS anketa")
    cur.execute("""CREATE TABLE IF NOT EXISTS anketa (
    reg_num INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    otchestvo TEXT,
    birthday TEXT,
    achievments TEXT,
    adress TEXT,
    speciality TEXT
    )""")


with sq.connect('abiturient.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info_students)

# with sq.connect('abiturient.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM anketa")
#     print(cur.fetchall())


# Поиск
with sq.connect('abiturient.db') as con:
    cur = con.cursor()

    # cur.execute("""SELECT * from anketa WHERE name LIKE 'Алексей' """)
    # print(cur.fetchall())

    # cur.execute("""SELECT * from anketa WHERE birthday LIKE '%2005' """)
    # print(cur.fetchall())
    #
    # cur.execute("""SELECT * from anketa WHERE achievments LIKE 'Да' """)
    # print(cur.fetchall())


# Редактирование
with sq.connect('abiturient.db') as con:
    cur = con.cursor()

    # cur.execute("""SELECT * from anketa WHERE reg_num = 2 """)
    # print(cur.fetchall())
    # cur.execute("""UPDATE anketa SET birthday = '20.01.2005' WHERE birthday LIKE '%2004' """)
    # cur.execute("""SELECT * from anketa WHERE reg_num = 2 """)
    # print(cur.fetchall())

    # cur.execute("""SELECT * from anketa WHERE speciality LIKE 'СА' """)
    # print(cur.fetchall())
    # cur.execute("""UPDATE anketa SET speciality = 'КМ' WHERE speciality LIKE 'СА' """)
    # cur.execute("""SELECT * from anketa WHERE speciality LIKE 'КМ' """)
    # print(cur.fetchall())
    #
    # cur.execute("""SELECT * from anketa WHERE name LIKE 'Ксения' """)
    # print(cur.fetchall())
    # cur.execute("""UPDATE anketa SET adress = 'Братский, 21' WHERE name LIKE 'Ксения' """)
    # cur.execute("""SELECT * from anketa WHERE name LIKE 'Ксения' """)
    # print(cur.fetchall())

# Удаление
with sq.connect('abiturient.db') as con:
    cur = con.cursor()

    cur.execute("""SELECT * from anketa WHERE name LIKE 'Мария' and speciality LIKE 'ИКС' """)
    print(cur.fetchall())
    cur.execute("""DELETE from anketa WHERE name LIKE 'Мария' AND speciality LIKE 'ИКС' """)
    cur.execute("""SELECT * from anketa WHERE name LIKE 'Мария' and speciality LIKE 'ИКС' """)
    print(cur.fetchall())

    # cur.execute("""SELECT * from anketa WHERE reg_num = 5 """)
    # print(cur.fetchall())
    # cur.execute("""DELETE from anketa WHERE reg_num = 5 """)
    # cur.execute("""SELECT * from anketa WHERE reg_num = 5 """)
    # print(cur.fetchall())
    #
    # cur.execute("""SELECT * from anketa WHERE surname LIKE 'Краснова' """)
    # print(cur.fetchall())
    # cur.execute("""DELETE from anketa WHERE surname LIKE 'Краснова' """)
    # cur.execute("""SELECT * from anketa WHERE surname LIKE 'Краснова' """)
    # print(cur.fetchall())
