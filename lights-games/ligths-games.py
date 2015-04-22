#!/usr/bin/env python3

"""
Idea is change the state of ligths on NxN matrix from zeros, on up,down,left,rigth postitions
and center point too.
"""

def show_solution(matrix):

    for row in matrix:
        print(row)

    print("\n")


def ligth_games(matrix, i, j, ancho, alto):

    if i >= 0 and i <=ancho:
        if j>=0 and j <= alto:
            if i-1 < 0:

            if i+j > ancho:
                pass
            if j-1 < 0:
                passpass
            if j+1 > ancho:
                pass


def main():

    matrix = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
    ]

    ancho = len(matrix)
    alto = len(matrix[0])

    ligth_games(matrix, ancho, alto)



if __name__ == '__main__':
    main()
