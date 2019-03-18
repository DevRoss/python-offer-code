#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-24


def find_first_k(array: list, start, end, key):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == key:
            if mid == 0 or array[mid - 1] < key:
                return mid
            else:
                end = mid - 1
        elif array[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def find_last_k(array: list, start, end, key):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == key:
            if mid == len(array) - 1 or array[mid + 1] > key:
                return mid
            else:
                start = mid + 1
        elif array[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def solve(array: list, key: int):
    if not array:
        return None
    first = find_first_k(array, 0, len(array) - 1, key)
    if first == -1:
        return None
    last = find_last_k(array, first, len(array) - 1, key)

    return last - first + 1


if __name__ == '__main__':
    print(solve([0, 1, 1], key=0))
    print(solve([0, 1, 1], key=1))
    print(solve([0, 1, 1], key=2))
    print(solve([0, 1, 1, 2, 5, 6, 6, 7, 9], key=1))
    print(solve([0, 1, 1, 2, 5, 6, 6, 7, 9], key=9))
    print(solve([0, 1, 1, 2, 5, 6, 6, 7, 9], key=55))
    print(solve([9], key=9))
    print(solve([], key=9))
