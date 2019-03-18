#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-24


def solve(array: list, length):
    if not array:
        return None
    start = 0
    end = len(array) - 1
    while start < end - 1:
        mid = (start + end) // 2
        if mid == array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if start == end:
        if end == array[end]:
            return array[end] + 1
        else:
            return array[end] - 1
    else:
        return array[end] + 1


if __name__ == '__main__':
    array = list(range(20))
    array.remove(0)
    print(solve(array, 20))
    array = list(range(20))
    array.remove(19)
    print(solve(array,20))
    array = list(range(20))
    array.remove(10)
    print(solve(array, 20))



