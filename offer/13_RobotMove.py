#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-9


def compute_digit(row, col):
    ret = 0
    while row > 0:
        ret += row % 10
        row //= 10

    while col > 0:
        ret += col % 10
        col //= 10
    return ret


def check(threshold, row, col, rows, cols, visited):
    if 0 <= row < rows and 0 <= col < cols and (not visited[row * cols + col]) \
            and compute_digit(row, col) <= threshold:
        return True
    return False


def move(threshold, row, col, rows, cols, visited):
    count = 0

    if check(threshold, row, col, rows, cols, visited):
        visited[row * cols + col] = True
        count = 1 + move(threshold, row - 1, col, rows, cols, visited) \
                + move(threshold, row + 1, col, rows, cols, visited) \
                + move(threshold, row, col - 1, rows, cols, visited) \
                + move(threshold, row, col + 1, rows, cols, visited)
    return count


def solve(threshold, rows, cols):
    visited = [False] * (rows * cols)
    ret = move(threshold, 0, 0, rows, cols, visited)
    return ret


if __name__ == '__main__':
    print(solve(6, 5, 5))
    print(solve(-1, 5, 5))
    print(solve(6, 5, 4))
    print(solve(6, 0, 0))
