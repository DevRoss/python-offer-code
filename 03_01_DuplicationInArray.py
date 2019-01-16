#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-7


def solve(l: list) -> bool:
    l_len = len(l)
    i = 0
    while i < l_len:
        if l[i] == i:
            i += 1
        elif l[i] > i and l[l[i]] != l[i]:
            l[l[i]], l[i] = l[i], l[l[i]]  # 交换
        else:
            return True
    return False


if __name__ == '__main__':
    print(solve([]))
    print(solve([0, 1, 2, 3, 4, 5, 6]))
    print(solve([0, 3, 1, 5, 2, 4]))
    print(solve([3, 0, 1, 4, 2, 4]))
    print(solve([0]))
