#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-26


def solve(numbers: list):
    if not numbers or len(numbers) != 5:
        return False
    sorted_num = sorted(numbers)
    num_0 = sorted_num.count(0)
    index = num_0
    while index < len(numbers) - 1:
        dif = sorted_num[index + 1] - sorted_num[index]
        # 有对
        if dif == 0:
            return False
        elif dif == 1:
            pass
        elif dif - 1 > num_0:
            return False
        else:
            num_0 -= dif - 1
        index += 1
    return True


if __name__ == '__main__':
    # print(solve([]))
    print(solve([0, 5, 7, 9, 6]))
    print(solve([0, 5, 7, 9, 10]))
    print(solve([0, 5, 7, 9, 0]))
    print(solve([0, 5, 7]))
