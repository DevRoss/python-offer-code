#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-23


def solve(string: str):
    max_len = 0
    current_len = 0
    table = dict()
    for i in range(len(string)):
        if string[i] not in table or i - table[string[i]] > current_len:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = i - table[string[i]]
        table[string[i]] = i
    max_len = max(max_len, current_len)
    return max_len


if __name__ == '__main__':
    print(solve('cabc2rwb'))
    print(solve('abb'))
    print(solve(''))
