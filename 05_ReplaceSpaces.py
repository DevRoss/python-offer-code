#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-8


def solve(s: str) -> str:
    s = list(s)
    num_space = 0
    for i in s:
        if i == ' ':
            num_space += 1
    p1 = len(s) - 1
    s += ' ' * (2 * num_space)  # 增加字符串长度
    p2 = len(s) - 1
    while 0 <= p1 and p1 < p2:
        if s[p1] == ' ':
            s[p2 - 2:p2 + 1] = '%20'
            p2 -= 3
            p1 -= 1
        else:
            s[p2] = s[p1]
            p1 -= 1
            p2 -= 1
    return ''.join(s)

if __name__ == '__main__':
    print(solve('hello world'))
    print(solve('hello  123 123 '))
    print(solve(''))
    print(solve(' '))
