#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-10


def solve(base, exponent):
    if base == 0:
        if exponent < 0:
            raise ValueError('0的负数次方未定义。')
        else:
            return 0
    ret = 1
    if exponent == 0:
        return 1
    elif exponent > 0:
        for i in range(exponent):
            ret *= base
    else:
        exponent = abs(exponent)
        for i in range(exponent):
            ret /= base
    return ret


if __name__ == '__main__':
    print(solve(2, 2))
    print(solve(2, 0))
    print(solve(-2, -3))
    print(solve(0, 0))
    print(solve(0, 2))
    print(solve(0, -2))
