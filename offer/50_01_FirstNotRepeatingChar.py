#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-23


def solve(string: str):
    if not string:
        return None
    table = dict()

    for i in string:
        table[i] = table.get(i, 0) + 1
    for i in string:
        if table[i] == 1:
            return i
    return None


if __name__ == '__main__':
    print(solve('ajlk;jcv'))
    print(solve('ajlk;jcvabadsch'))
    print(solve(''))
    print(solve(None))
