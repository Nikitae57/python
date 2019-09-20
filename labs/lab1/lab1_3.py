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

    while a is None:
        try:
            a = float(input('Введите первую сторону: '))
        except ValueError:
            a = None

    while b is None:
        try:
            b = float(input('Введите вторую сторону: '))
        except ValueError:
            b = None

    area = a * b
    print(area)


def right_triangle_area():
    a, b = None, None

    while a is None:
        try:
            a = float(input('Введите первую сторону: '))
        except ValueError:
            a = None

    while b is None:
        try:
            b = float(input('Введите вторую сторону: '))
        except ValueError:
            b = None

    area = a * b / 2
    print(area)


def right_polygon_area():
    n, a = None, None

    while n is None:
        try:
            n = float(input('Введите количество сторон: '))
        except ValueError:
            n = None

    while a is None:
        try:
            a = float(input('Введите длину стороны: '))
        except ValueError:
            a = None

    area = n / 4 * a**2 * (1 / m.tan(m.pi / n))
    print(area)


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

