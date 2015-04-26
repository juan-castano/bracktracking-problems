#!/usr/bin/env python3


def __show_numbers(array, number, value):

    if len(array) > 0:
        if number != array[0]:
            if (number + array[0]) == value:
                print("%s + %s = %s" % (number, array[0], value))

        __show_numbers(array[1:], number, value)


def show_numbers(array, value):

    for number in array:
        __show_numbers(array, number, value)


def main():
    array = list(range(1, 15))
    number = int(input("Ingrese el numero a buscar: "))
    show_numbers(array, number)


if __name__ == '__main__':
    main()
