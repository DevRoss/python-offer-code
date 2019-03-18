#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-10


def solve(n):
    count = 0
    flag = 1
    while flag & 0xffffffff:
        if n & flag:
            count += 1
        flag <<= 1
    return count


if __name__ == '__main__':
    print(solve(1))
    print(solve(2))
    print(solve(3))
    print(solve(4))
    print(solve(5))
    print(solve(6))
    print(solve(7))
    print(solve(-1))
