#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-24


def solve(array: list):
    if not array:
        return None
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) >> 1
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return None


if __name__ == '__main__':
    print(solve([-6, -3, -1, 3, 5, 6, 7]))
    print(solve([-6, -3, -1, 88, 5, 6, 7]))
    print(solve([0, 2, 5, 7, 83]))
    print(solve([-1, 0, 2]))
