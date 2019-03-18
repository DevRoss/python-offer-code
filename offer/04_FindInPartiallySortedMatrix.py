#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-7
import numpy as np


def solve(matrix: list, rows: int, columns: int, number: int):
    if matrix is not None and rows > 0 and columns > 0:
        row = 0
        column = columns - 1
        while row < rows and column >= 0:
            if matrix[row, column] == number:
                return True
            elif matrix[row, column] > number:
                column -= 1
            else:
                row += 1
    return False


if __name__ == '__main__':
    m = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 11, 15],
         [6, 8, 11, 15]]
    m = np.matrix(m)
    print(solve(m, 4, 4, 7))
    print(solve(m, 4, 4, 23))
    print(solve(m, 4, 4, 5))
    print(solve(m, 4, 4, 6))
    print(solve(m, 4, 4, 12))
