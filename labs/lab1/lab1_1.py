import math as m


x = None
while x is None:
    try:
        x = float(input('Введите x: '))
    except ValueError:
        x = None

y = None
while y is None:
    try:
        y = float(input('Введите y: '))
    except ValueError:
        y = None

n = None
while n is None:
    try:
        n = float(input('Введите n: '))
    except ValueError:
        n = None

m = None
while m is None or m == 0:
    try:
        m = float(input('Введите m: '))
    except ValueError:
        m = None

result = m.pow(y, 1 / n) * (m.sin(m.pow(y, 2)) + m.pow(m.cos(y), 2)) + m.pow(x, m.pow(n, m)) / m
print('Результат вычислений:', result)
