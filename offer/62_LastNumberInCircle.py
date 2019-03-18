#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-26


def solve(n, m):
    if n < 1 or m < 1:
        return None
    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i
    return last


if __name__ == '__main__':
    print(solve(10, 1))
    print(solve(10, 2))
    print(solve(10, 30))
