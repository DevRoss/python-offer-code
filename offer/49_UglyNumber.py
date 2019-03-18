#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-23


def solve(n: int):
    if n <= 0:
        return None
    ugly_numbers = [0] * n
    ugly_numbers[0] = 1
    p2 = 0
    p3 = 0
    p5 = 0
    for i in range(1, n):
        min_ugly = min(ugly_numbers[p2] * 2, ugly_numbers[p3] * 3, ugly_numbers[p5] * 5)
        ugly_numbers[i] = min_ugly
        while ugly_numbers[p2] * 2 <= ugly_numbers[i]:
            p2 += 1
        while ugly_numbers[p3] * 3 <= ugly_numbers[i]:
            p3 += 1
        while ugly_numbers[p5] * 5 <= ugly_numbers[i]:
            p5 += 1
    return ugly_numbers[-1]


if __name__ == '__main__':
    print(solve(1))
    print(solve(10))
    print(solve(1000))
