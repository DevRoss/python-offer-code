#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-19


def check(array: list, middle):
    c = 0
    for i in range(middle, len(array)):
        if array[i] != array[middle]:
            break
        c += 1
    for i in range(middle, -1, -1):
        if array[i] != array[middle]:
            break
        c += 1
    return c > (len(array) >> 1)


def solve(array: list):
    if not array:
        return None

    middle = (len(array) - 1) >> 1

    def partition(array, left, right):
        first = left

        key = array[left]
        while left != right:
            while key <= array[right] and left < right:
                right -= 1
            while array[left] <= key and left < right:
                left += 1
            if left < right:
                array[left], array[right] = array[right], array[left]
        # 归位
        array[first] = array[left]
        array[left] = key
        return left

    left = 0
    right = len(array) - 1
    index = partition(array, left, right)

    while index != middle:
        if index > middle:
            right = index - 1
            index = partition(array, left, right)

        else:
            left = index + 1
            index = partition(array, left, right)
    if check(array, middle):
        return array[middle]
    return None


if __name__ == '__main__':
    print(solve([1, 2, 7, 2, 8, 2, 2, 5, 2]))
    print(solve([1, 2, 7, 2, 8, 7, 2, 5, 2]))
    print(solve([3]))
