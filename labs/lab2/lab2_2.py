import textwrap as tw
import math as m


def print_menu():
    menu = """
        R) Площадь прямоугольника
        T) Площадь прямоугольного треугольника
        M) Площадь правильного многоугольника
        E) Выйти
    """
    print(tw.dedent(menu))


def rectangle_area():
    a, b = None, None

    while a is None or b is None:
        try:
            user_input = input('Введите две стороны через пробел: ')
            splitted_input = user_input.lstrip().rstrip().split(' ')
            a, b = splitted_input[0], splitted_input[1]

            a = float(a)
            b = float(b)
        except ValueError:
            a = None
            b = None

    area = lambda a, b: a * b
    print(area(a, b))


def right_triangle_area():
    a, b = None, None

    while a is None or b is None:
        try:
            user_input = input('Введите две стороны через пробел: ')
            splitted_input = user_input.lstrip().rstrip().split(' ')
            a, b = splitted_input[0], splitted_input[1]

            a = float(a)
            b = float(b)
        except ValueError:
            a = None
            b = None

    area = lambda a, b: a * b / 2
    print(area(a, b))


def right_polygon_area():
    n, a = None, None

    while n is None or a is None:
        try:
            user_input = input('Введите количество сторон и их длину через пробел: ')
            splitted_input = user_input.lstrip().rstrip().split(' ')
            n, a = splitted_input[0], splitted_input[1]

            n = float(n)
            a = float(a)
        except ValueError:
            n = None
            a = None

    area = lambda n, a: n / 4 * a**2 * (1 / m.tan(m.pi / n))
    print(area(n, a))


def run():
    should_run = True
    while should_run:
        print_menu()

        user_choice = input().lower()
        if user_choice == 'r':
            rectangle_area()

        elif user_choice == 't':
            right_triangle_area()

        elif user_choice == 'm':
            right_polygon_area()

        elif user_choice == 'e':
            should_run = False
        else:
            print("Некоректный ввод")
            continue


if __name__ == '__main__':
    run()

