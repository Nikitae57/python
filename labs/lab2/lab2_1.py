import math as m


func = lambda x, y, n: 3 * m.pow(m.cos(x - m.pi / 6), n) / (1 / 2 + m.sin(y))

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

print('Результат вычислений:', func(x, y, n))
