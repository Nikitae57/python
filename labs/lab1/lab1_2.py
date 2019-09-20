import textwrap as tw
import re


def print_menu():
    menu = """
        1) Вывести список на экран
        2) Добавить элемент в список
        3) Удалить элемент из списка
        4) Составить кортеж из четных элементов списка
        5) Найти сумму всех целочисленных элементов
        6) Сформировать строку и посчитать слова
        7) Задать 2 множества и вывести их объединение
        8) Сделать словарь и вывести на экран пары с ключом > 5
        0) Выйти
    """
    print(tw.dedent(menu))


def add_item(target_list):
    if type(target_list) != list:
        raise ValueError

    index = None
    while index is None:
        try:
            index = int(input('Введите индекс: '))
        except ValueError:
            index = None

    value = input('Введите значение: ')

    if '.' in value:
        # float
        try:
            typed_value = float(value)
        except ValueError:
            typed_value = value
    elif 'j' in value:
        # complex
        try:
            typed_value = complex(value)
        except ValueError:
            typed_value = value
    else:
        # int or string
        try:
            typed_value = int(value)
        except ValueError:
            typed_value = value

    target_list.insert(index, typed_value)


def remove_item(target_list):
    if type(target_list) != list:
        raise ValueError

    index = None
    while index is None:
        try:
            index = int(input('Введите индекс: '))
        except ValueError:
            index = None

    target_list.pop(index)


def make_tuple_of_even(src_list):
    if type(src_list) != list:
        raise ValueError

    list_of_even = src_list[::2]

    return tuple(list_of_even)


def sum_of_ints(src_list):
    if type(src_list) != list:
        raise ValueError

    ints_sum = 0
    for item in src_list:
        if type(item) == int:
            ints_sum += item

    return ints_sum


def word_count(src_list):
    if type(src_list) != list:
        raise ValueError

    result_str = ""
    for item in src_list:
        result_str += str(item)

    words = re.findall('[a-zA-Zа-яА-Я]+', result_str)

    return len(words)


def make_set_union():
    set_str1 = input('Введите первое множество через запятую: ')
    set_str2 = input('Введите второе множество через запятую: ')

    set1 = set(set_str1.replace(' ', '').split(','))
    set2 = set(set_str2.replace(' ', '').split(','))
    union = sorted(set1.union(set2))

    print(union)


def make_dict(src_list):
    if type(src_list) != list:
        raise ValueError

    result_dict = {}
    for index, item in enumerate(src_list):
        if index <= 5:
            continue
        result_dict[index] = item

    print(result_dict)


def run():
    should_run = True
    item_list = [1, None, 2.3, "sda"]

    while should_run:
        print_menu()
        try:
            user_choice = int(input())
        except ValueError:
            user_choice = None

        if user_choice is None:
            print("Некоректный ввод")
            continue

        if user_choice == 0:
            exit(0)
        elif user_choice == 1:
            print(item_list)
        elif user_choice == 2:
            add_item(item_list)
        elif user_choice == 3:
            remove_item(item_list)
        elif user_choice == 4:
            print(make_tuple_of_even(item_list))
        elif user_choice == 5:
            print(sum_of_ints(item_list))
        elif user_choice == 6:
            print(word_count(item_list))
        elif user_choice == 7:
            make_set_union()
        elif user_choice == 8:
            make_dict(item_list)


if __name__ == '__main__':
    run()
