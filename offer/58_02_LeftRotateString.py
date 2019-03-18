#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-25


def solve(string: str, pos: int):
    if string is None:
        return None
    length = len(string)
    if pos > length or pos < 0:
        return None
    elif pos == length or pos == 0:
        return string
    else:
        return string[pos:] +string[:pos]


if __name__ == '__main__':
    print(solve('abcdefg', 2))
    print(solve('abcdefg', 1))
    print(solve('abcdefg', 0))
    print(solve('abcdefg', 7))
    print(solve('abcdefg', 8))
    print(solve('adaf', 7))
    print(solve('', 0))
