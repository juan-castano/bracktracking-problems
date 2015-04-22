#!/usr/bin/env python3

def show_numbers(array):

    if len(array) >= 0:
        print(array)
        array = [1:]
        show_numbers(array)

    else:
        return


def main():
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    show_numbers(array)

if __name__ == '__main__':
    main()
