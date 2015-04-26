#!/usr/bin/env python3


def show_pairs_dices(quantity):
    for val in range(quantity):
        print(quantity)
        quantity -= 1
        show_pairs_dices(quantity)


def main():
    quantity_dices = 10
    show_pairs_dices(quantity_dices)


if __name__ == '__main__':
    main()
