#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-10


def solve_dp(length):
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    products = [0] * (length + 1)
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    for i in range(4, length + 1):  # 0 - length 长度中，每一个长度的最大积
        max = 0
        for j in range(length // 2, length):
            product = products[j] * products[i - j]
            if max < product:
                max = product
        products[i] = max
    return products[length]


def solve_greedy(length):
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    product = 1
    while length > 3:
        if length >= 5:
            product *= 3
            length -= 3
        elif length == 4:
            product *= 2
            length -= 2
    product *= length
    return product


if __name__ == '__main__':
    print(solve_greedy(0))
    print(solve_greedy(1))
    print(solve_greedy(2))
    print(solve_greedy(3))
    print(solve_greedy(4))
    print(solve_greedy(5))
    print(solve_greedy(6))
    print(solve_greedy(7))
