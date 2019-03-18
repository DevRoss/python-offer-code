#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-22
from functools import cmp_to_key


def cmp(int1, int2):
    s1 = str(int1)
    s2 = str(int2)
    if s1 + s2 < s2 + s1:
        return -1
    elif s1 + s2 > s2 + s1:
        return 1
    else:
        return 0


def solve(array: list):
    ret = sorted(array, key=cmp_to_key(cmp))
    for i in ret:
        print(i,end='')
    print()


if __name__ == '__main__':
    solve([3, 32, 321])
    solve([3])
    solve([])
