#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-21


def solve(array: list):
    if not array:
        return None
    max_sum = array[0]
    tmp = 0
    for i in array:
        if tmp <= 0:
            tmp = i
        else:
            tmp += i
        max_sum = max(max_sum, tmp)

    return max_sum


def solve2(array: list):
    if not array:
        return None

    def core(array: list, i):
        if i == 0:
            return array[i]

        pre = core(array, i - 1)
        if pre <= 0:
            return max(array[i], pre)
        else:
            return pre + array[i]

    return core(array, len(array) - 1)


if __name__ == '__main__':
    print(solve([-10, -1, -3]))
    print(solve([-10, -1, 2, 4]))
    print(solve([-10, -1, 2, 4, -2, -1, 4]))
    print(solve([-10]))
    print(solve([-10, 0]))
