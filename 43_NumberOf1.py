#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-21


def solve(n: int):
    strN = str(n)

    def core(n: str):
        if not n[0].isdigit():
            return 0
        first = int(n[0])
        if len(n) == 1:
            if first == 0:
                return 0
            else:
                return 1
        first_1 = 0
        # 现在计算第一位出现的次数
        if first > 1:
            first_1 = 10 ** (len(n) - 1)
        elif first == 1:
            first_1 = int(n[1:]) + 1
        # 除了第一位之外的1
        other_1 = first * (len(n) - 1) * 10 ** (len(n) - 2)
        rest_num_1 = core(n[1:])
        return first_1 + other_1 + rest_num_1

    return core(strN)


if __name__ == '__main__':
    print(solve(12))
    print(solve(12134))
    print(solve(1))
    print(solve(0))
    print(solve(-1))
