#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-26


def solve(array: list):
    if not array:
        return None

    min_value = array[0]
    max_dif = 0
    for i in array:
        if i < min_value:
            min_value = i
        else:
            max_dif = max(max_dif, i - min_value)
    return max_dif


if __name__ == '__main__':
    print(solve([]))
    print(solve([1, 6]))
    print(solve([9, 11, 8, 5, 7, 12, 16, 14]))
