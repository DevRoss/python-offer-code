#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-26

max_value = 6


def solve(number: int):
    if number < 1:
        return None

    # 新建两个数组，并进行初始化
    probabilities = [[0] * (number * max_value + 1), [0] * (number * max_value + 1)]
    flag = 0
    for i in range(1, max_value + 1):
        probabilities[flag][i] = 1

    for k in range(2, number + 1):
        for i in range(0, k):
            probabilities[1 - flag][i] = 0

        # 更新前面数字
        for i in range(k, max_value * k + 1):
            probabilities[1 - flag][i] = 0
            for j in range(1, min(i, max_value) + 1):
                probabilities[1 - flag][i] += probabilities[flag][i - j]
        flag = 1 - flag

    total = max_value ** number
    for i in range(number, max_value * number + 1):
        ratio = probabilities[flag][i] / total
        print('{}: {}'.format(i, ratio))


if __name__ == '__main__':
    solve(1)
