#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-18

def solve(s: str):
    maxlen = 0
    start = 0
    # 奇数
    for i in range(len(s)):
        j = k = i
        while j >= 0 and k < len(s) and s[j] == s[k]:
            length = k - j + 1
            if length > maxlen:
                maxlen = length
                start = j
            k += 1
            j -= 1
    # 偶数
    for i in range(len(s) - 1):
        j = i
        k = i + 1
        while j >= 0 and k < len(s) and s[j] == s[k]:
            length = k - j + 1
            if length > maxlen:
                maxlen = length
                start = j
            k += 1
            j -= 1
    return s[start: start + maxlen]


if __name__ == '__main__':
    # print(solve('babad'))
    # print(solve('ba'))
    print(solve('aa'))
