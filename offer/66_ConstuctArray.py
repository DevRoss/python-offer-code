#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-27


def solve(array: list):
    if not array:
        return None
    length = len(array)
    ret = [1] * length
    for i in range(1, length):
        ret[i] = ret[i - 1] * array[i - 1]
    temp = 1
    for i in range(length - 2, -1, -1):
        temp *= array[i + 1]
        ret[i] *= temp
    return ret


if __name__ == '__main__':
    print(solve(list(range(1, 6))))
    print(solve(list(range(1, 2))))
