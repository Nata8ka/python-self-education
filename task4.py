print('Задача 1.1')
number = int(input("Введите число: "))
if (1 <= number <= 100) or (200 <= number <= 300):
    print("Число попадает в заданный диапазон.")
else:
    print("Число не попадает в заданный диапазон.")

print('Задача 1.2')
x = float(input("Введите начальную температуру воды: "))
t = (100 - x) * 2
print("Вода закипит через", t, "минут")

print('Задача 1.3')
X = int(input("Введите число: "))
for i in range(1, X+1):
    print(i, '000')

print('Задача 1.4')
height = int(input("Введите высоту треугольника: "))
for i in range(height):
    print("*" * (i + 1))

print('Задача 2.1')
A = int(input(""))
B = int(input(""))
C = int(input(""))
M = int(input(""))
K = int(input(""))
if A <= M and B <= K and C <= M and C <= K:
    print('Коробка войдет в дверь')
else:
    print('Коробка не войдет в дверь')

print('Задача 2.2')
height = int(input("Введите высоту треугольника: "))
for i in range(height):
    for j in range(height-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()

print('Задача 2.3')
N = int(input("Введите число N: "))
i = 1
while i**2 < N:
    print(i**2)
    i += 1

print('Задача 3.1')
k = int(input("Введите количество шариков мороженого, которые нужно купить: "))
can_buy = False
max_threes = k // 3
max_fives = k // 5
for i in range(max_threes, -1, -1):
    for j in range(max_fives, -1, -1):
        if 3*i + 5*j == k:
            can_buy = True
            break
    if can_buy:
        break

if can_buy:
    print("Да")
else:
    print("Нет")

print('Задача 3.2')
P = float(input("Введите сумму вклада, тыс. грн: "))
r = float(input("Введите годовую процентную ставку, %: "))
Z = float(input("Введите желаемую сумму вклада, тыс. грн: "))
S = P
t = 0
while S < Z:
    S = S * (1 + r/100)
    t += 1
print(f'через {t} лет')

print('Задача 3.3')
n = int(input("Введите число: "))
s = sum(int(d) for d in str(n))
print("Сумма цифр равна", s)
