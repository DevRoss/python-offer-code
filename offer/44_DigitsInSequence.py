#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-22

def num_int(digits):
    if digits == 1:
        return 10
    return 10 ** (digits - 1) * 9


def begin_number(digits):
    if digits == 1:
        return 0
    else:
        return 10 ** (digits - 1)


def num_of_index(n, digits):
    number = begin_number(digits) + n // digits
    index = n % digits
    return int(str(number)[index])


def solve(n: int):
    if n <= 0:
        return None
    digits = 1  # 表示正在操作digits位的数
    while True:
        numbers = num_int(digits)
        if n < numbers:
            return num_of_index(n, digits)
        n -= numbers * digits
        digits += 1


if __name__ == '__main__':
    for i in range(20):
        print(solve(i))
