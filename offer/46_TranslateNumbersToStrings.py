#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-22


def solve(n: int):
    str_n = str(n)
    if not n or len(str_n) == 0 or n < 0:
        return None
    if len(str_n) == 1:
        return 1

    count = [0] * len(str_n)
    count[-1] = 1
    if int(str_n[-2:]) <= 25:
        count[-2] = 2
    else:
        count[-2] = 1
    i = len(str_n) - 3
    while i >= 0:
        c = count[i + 1]
        if int(str_n[i:i + 2]) <= 25:
            c += count[i + 2]
        count[i] = c
        i -= 1
    return count[0]


if __name__ == '__main__':
    print(solve(12258))
    print(solve(18))
    print(solve(1))
    print(solve(None))
