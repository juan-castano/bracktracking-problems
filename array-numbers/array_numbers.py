#!/usr/bin/env python3


def __show_numbers(array, number, value):

    if len(array) > 0:
        if number != array[0]:
            if (number+array[0]) == value:
                print("%s + %s = %s" % (number, array[0], value))

        __show_numbers(array[1:], number, value)


def show_numbers(array, value):

    for number in array:
        __show_numbers(array, number, value)




def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    number = int(input("Ingrese el numero a buscar: "))
    show_numbers(array, number)


if __name__ == '__main__':
    main()
