#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-7

# 我选择用空间来换时间

def solve(l: list) -> int:
    table = dict()
    for i in l:
        if table.get(i):
            return i
        else:
            table[i] = True
    return -1


if __name__ == '__main__':
    print(solve([]))
    print(solve([0, 1, 2, 3, 4, 5, 6]))
    print(solve([0, 3, 1, 5, 2, 4]))
    print(solve([3, 0, 1, 4, 2, 4]))
    print(solve([0]))
