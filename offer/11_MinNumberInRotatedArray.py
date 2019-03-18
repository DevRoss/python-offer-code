#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-9


def solve(array: list) -> int or bool:
    start = 0
    end = len(array) - 1
    mid = 0
    if not len(array):
        return False
    if len(array) == 1:
        return array[0]

    while array[start] >= array[end]:
        if end - 1 == start:
            break
        mid = (start + end) // 2
        if array[start] >= array[mid] >= array[end]:
            return array[end]
        if array[mid] >= array[start]:  # 表示中间的数在左边的数组中
            start = mid
        else:  # 表示中间的数在右边的数组中
            end = mid
    if end - start > 1:
        return array[start]
    return array[end]


if __name__ == '__main__':
    print(solve([1, 2, 3, 4, 5]))
    print(solve([3, 4, 5, 1, 2]))
    print(solve([5, 4, 3, 2, 1]))
    print(solve([]))
    print(solve([0]))
