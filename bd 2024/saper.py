import sqlite3 as sq
from data_users import info_users


with sq.connect('saper.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")


# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.execute("INSERT INTO users VALUES (1, 'Алексей', 2, 22, 1000)")


# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)


# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     # cur.execute("SELECT * FROM users WHERE old > 20 AND score <= 1000")
#     # cur.execute("SELECT * FROM users WHERE score < 1000")
#     # cur.execute("SELECT * FROM users WHERE old IN(19, 32) AND score > 300 OR sex = 1")
#     # cur.execute("SELECT * FROM users WHERE score <= 1000 ORDER BY old DESC")
#     result = cur.fetchall()
#     print(result)


# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users")
#     result1 = cur.fetchone()
#     result2 = cur.fetchmany(2)
#     print(result1)
#     print(result2)


# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE users SET old = old+1 WHERE old < 20")


# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM users WHERE user_id = 2")


with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)
