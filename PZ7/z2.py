# Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
# расставлены правильно (то есть каждой открывающей соответствует одна
# закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
# в которой расположена первая ошибочная закрывающая скобка, или, если
# закрывающих скобок не хватает, число —1.

s = input("Введите строку со скобками: ")
stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        if len(stack) == 0:
            print(i)
            break
        else:
            stack.pop()
if len(stack) == 0:
    print(0)
else:
    print(-1)
