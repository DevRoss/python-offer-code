#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-25


def solve(array: list):
    if not array:
        return None
    bit_sum = [0] * 32
    for num in array:
        mask = 1
        for i in range(32):
            if num & mask != 0:
                bit_sum[i] += 1
            mask <<= 1
    result = 0
    for i in range(31, -1, -1):
        result <<= 1
        result += bit_sum[i] % 3
    return result


if __name__ == '__main__':
    print(solve([1, 4, 5, 5, 6, 6, 6, 5, 4, 4]))
    print(solve([4]))
    print(solve([4, 4, 4, 7]))
