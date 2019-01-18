#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-8


def solve(n: int):
    if n <= 0:
        return -1
    table = [0, 1]
    if n < 2:
        return table[n]
    fib1 = table[0]
    fib2 = table[1]
    fib_n = 0
    for i in range(2, n + 1):
        fib_n = fib1 + fib2
        fib1 = fib2
        fib2 = fib_n
    return fib_n


if __name__ == '__main__':
    for i in range(2, 10):
        print(solve(i), end=' ')
