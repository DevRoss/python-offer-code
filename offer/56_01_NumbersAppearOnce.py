#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-25


def fist_1(n: int):
    position = 0
    while n > 0:
        if n & 1:
            return position
        n >>= 1
        position += 1
    return -1


def is_bit(n: int, index: int):
    n >>= index
    return n & 1


def solve(array: list):
    if not array:
        return None
    total_dif = 0
    for i in array:
        total_dif ^= i
    pos_1 = fist_1(total_dif)
    num1 = 0
    num2 = 0
    for i in array:
        if is_bit(i, pos_1):
            num1 ^= i
        else:
            num2 ^= i
    return num1, num2


if __name__ == '__main__':
    print(solve([2, 4, 3, 6, 3, 2, 5, 5]))
    print(solve([4, 3, 6, 3, 5, 5]))
    print(solve([4, 3, 6, 3, 5, 5]))
    print(solve([3, 6]))
    print(solve([]))
