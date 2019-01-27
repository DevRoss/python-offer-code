#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-20


def solve(array: list, k):
    def partition(array: list, left, right):
        first = left
        key = array[first]
        while left != right:
            while key <= array[right] and left < right:
                right -= 1
            while array[left] <= key and left < right:
                left += 1
            if left < right:
                array[left], array[right] = array[right], array[left]
        array[first] = array[left]
        array[left] = key
        print(array)
        return left

    left = 0
    right = len(array) - 1
    index = partition(array, left, right)
    while index != k - 1:
        if index < k - 1:
            left = index + 1
            index = partition(array, left, right)
        else:
            right = index - 1
            index = partition(array, left, right)
    return array[:k]


if __name__ == '__main__':
    print(solve([1, 4, 62346, 889, 3, 8, 77, 2], 3))
    # 可以使用 heapq
