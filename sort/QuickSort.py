#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-7


def solve(array):
    def partition(l, r, array):
        """
        使得参考数左边的数都小于参考数，使得参考数右边的数都大于参考数
        """
        x = array[l]
        while l < r:
            while l < r and x <= array[r]:
                r -= 1
            if l < r:
                array[l], array[r] = array[r], array[l]
                l += 1
            while l < r and array[l] < x:
                l += 1
            if l < r:
                array[l], array[r] = array[r], array[l]
        array[l] = x
        return l

    def quick_sort(l, r, array):
        if l < r:
            p = partition(l, r, array)
            quick_sort(l, p - 1, array)
            quick_sort(p + 1, r, array)

    quick_sort(0, len(array) - 1, array)
    return array


if __name__ == '__main__':
    print(solve([1, 552, 66, 73, 7, 32, 6, 772, 7, 11]))
    print(solve([1]))
    print(solve([1, 2]))
    print(solve([2, 1]))
