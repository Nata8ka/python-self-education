a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = input('Операція:')
if c == '+':
    d = a + b
elif c == '-':
    d = a-b
elif c == '/':
    d = a/b
elif c == '*':
    d = a*b
elif c == 'mod':
    d = a % b
elif c == 'pow':
    d = a**b
elif c == 'div':
    d = a//b
else:
    print("zzzz")
print('Число: ', d)
a = int(input('Введите число: '))
b = int(input('Введите число: '))
if a % b == 0:
    print(a, 'ділиться на', b)
else:
    print(a, 'не ділиться на', b)
if b % a == 0:
    print(b, 'ділиться на', a)
else:
    print(b, 'не ділиться на', a)
a = int(input('Введите число: '))
b = a // 100
c = a // 10 % 10
d = a % 10
if a == b or a == c or b == c:
    print('Є однакові цифр')
else:
    print('не має однаковий цифр')
