# Составить список, в который будут включены только согласные буквы и
# привести их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль',
# 'Дели', 'Каир']
spisok = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']


def sogl(spisok):
    yield from [bukva for slovo in spisok for bukva in slovo if bukva in 'ЙйЦцКкНнГгШшЩщЗзХхФфВвПпРрЛлДдЖжЧчСсМмТтБб']


all_sogl = set(sogl(spisok))
verh_reg = set([i.upper() for i in all_sogl])
print(list(verh_reg))
