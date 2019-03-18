#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-25


def solve(array: list, target):
    if not array:
        return None
    table = set()
    for i in array:
        if i in table:
            return target - i, i
        else:
            table.add(target - i)
    return None


if __name__ == '__main__':
    print(solve([1, 5, 67, 8, 9, 4, 66, 62, 7, 82, 2, 86], 13))
    print(solve([1, 5, 67, 8, 9, 4, 66, 62, 7, 82, 2, 86], 168))
    print(solve([1, 5, 67, 8, 9, 4, 66, 62, 7, 82, 2, 86], 98))
