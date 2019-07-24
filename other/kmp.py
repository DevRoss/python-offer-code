#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-7-16


def get_table(main_str: str):
    table = [0] * len(main_str)
    table[0] = -1
    table[1] = 0
    pos = 2  # pos为扫描main_str的时候的当前指针
    cond = 0  # cond为在前缀的指针
    length = len(main_str)
    while pos < length:
        if main_str[pos] == main_str[cond]:
            cond += 1
            table[pos] = cond
            pos += 1
        elif cond > 0:
            cond = table[cond]
        else:
            pos += 1
    return table


def kmp(main_str: str, pattern: str):
    """
    kmp算法
    :param main_str:
    :param pattern:
    :return: begin position if match, else -1
    """
    i = j = 0
    next_table = get_table(main_str)
    while i < len(main_str) and j < len(pattern):
        if j == -1 or main_str[i] == pattern[j]:
            j += 1
            i += 1
        else:
            j = next_table[j]
    if j == len(pattern):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    main_str = 'ABABAC'
    pattern = 'ABABAC'
    print(kmp(main_str, pattern))
    main_str = 'ABABAC'
    pattern = 'C'
    print(kmp(main_str, pattern))
    main_str = 'ABABAC'
    pattern = 'BA'
    print(kmp(main_str, pattern))
    main_str = 'ABABAC'
    pattern = 'ANC'
    print(kmp(main_str, pattern))
