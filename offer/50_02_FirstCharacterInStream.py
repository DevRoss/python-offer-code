#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-23


def solve(string: str):
    if not string or len(string) == 0:
        return None
    table = dict()
    i = 0
    while i < len(string):
        # 第一次出现
        if string[i] not in table:
            table[string[i]] = i
        else:
            table[string[i]] = -1
            # 更新first
        i += 1
    first = None
    for k, v in table.items():
        if v >= 0:
            if first is None:
                first = (k, v)
            else:
                if v < first[1]:
                    first = (k, v)
    if first is None:
        return None
    return first[0]

if __name__ == '__main__':
    print(solve('a'))
    print(solve('ab'))
    print(solve('abb'))
    print(solve('abba'))
    print(solve('abbca'))
    print(solve('abbcac'))
    print(solve(''))
