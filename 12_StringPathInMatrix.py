#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-9


def find_path(matrix: list, visited: list, target, rows, cols, row, col, index) -> bool:
    if index >= len(target):
        return True
    has_path = False
    if 0 <= row < rows and 0 <= col < cols and (not visited[row * cols + col]) \
            and matrix[row * cols + col] == target[index]:
        index += 1
        print(row, col)
        visited[row * cols + col] = True
        has_path = find_path(matrix, visited, target, rows, cols, row + 1, col, index) or \
                   find_path(matrix, visited, target, rows, cols, row - 1, col, index) or \
                   find_path(matrix, visited, target, rows, cols, row, col + 1, index) or \
                   find_path(matrix, visited, target, rows, cols, row, col - 1, index)
        if not has_path:
            index -= 1
            visited[row * cols + col] = False

    return has_path


def solve(matrix: list, rows, cols, target) -> bool:
    if not len(matrix):
        return False
    visited = [False] * len(matrix)

    for row in range(rows):
        for col in range(cols):
            if find_path(matrix, visited, target, rows, cols, row, col, 0):
                return True
            print('-'*30)
    return False


if __name__ == '__main__':
    # matrix = list('abtgcfcsjdeh')
    # print(solve(matrix, 3, 4, 'bfce'))
    print(solve(['1'], 1, 1, '1'))
    # print(solve(matrix, 3, 4, 'bfce'))
