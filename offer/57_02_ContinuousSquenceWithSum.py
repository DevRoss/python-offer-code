#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-25


def _print(begin, end):
    for i in range(begin, end + 1):
        print(i, end=' ')
    print()


def solve(target):
    if target < 3:
        return
    mid = (1 + target) >> 1
    small = 1
    big = 2
    cur_sum = small + big
    while small < mid:
        if cur_sum == target:
            _print(small, big)
            big += 1
            cur_sum += big
        elif cur_sum < target:
            big += 1
            cur_sum += big

        else:
            cur_sum -= small
            small += 1


if __name__ == '__main__':
    solve(15)
    print('='*20)
    solve(10)
    print('=' * 20)
    solve(100)
    print('=' * 20)
    solve(1)
    print('=' * 20)
