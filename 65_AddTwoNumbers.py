#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-26


def solve(a, b):
    while True:
        _sum = a ^ b
        c = (a & b) << 1
        a = _sum
        b = c
        if b == 0:
            break
    return a


if __name__ == '__main__':
    print(solve(1, 2))
    print(solve(1, 0))
    print(solve(0, 0))
    print(solve(-10, 2))
    print(solve(-10, -2))
