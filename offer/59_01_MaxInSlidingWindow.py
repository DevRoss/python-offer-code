#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-25


def solve(array: list, win_size):
    if not array or win_size > len(array) or win_size <= 0:
        return None
    length = len(array)
    cur_sum = max_sum = sum(array[:win_size])
    win_start = 0
    left = 1
    right = win_size
    while right < length:
        cur_sum -= array[left - 1]
        cur_sum += array[right]
        if cur_sum > max_sum:
            max_sum = cur_sum
            win_start = left
        left += 1
        right += 1
    return array[win_start:win_start + win_size]


if __name__ == '__main__':
    print(solve([2, 3, 4, 2, 6, 2, 5, 1], 3))
    print(solve([2, 6], 3))
    print(solve([2, 6, 3], 3))
    print(solve([2, 6, 3], 1))
    print(solve([2], 1))
