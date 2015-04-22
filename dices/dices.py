#!/usr/bin/env python3

def search_pair(quantity):

    if quantity != 0:
        if quantity > 6:
            quantity -= 1
            search_pair(quantity)

        print(quantity)
        quantity += 1
        search_pair(quantity)

    else:
        return



def main():
    quantity = int(input("Ingrese la cantidad de dados: "))
    search_pair(quantity)

if __name__ == '__main__':
    main()
