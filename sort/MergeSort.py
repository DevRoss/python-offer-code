#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-7


def solve(array):
    def merge_sort(array: list):
        tmp = array.copy()

        def merge(array, left, right):
            mid = (left + right) >> 1
            i = left
            j = mid + 1
            k = left
            while i <= mid and j <= right:
                if array[i] <= array[j]:
                    tmp[k] = array[i]
                    i += 1
                else:
                    tmp[k] = array[j]
                    j += 1
                k += 1

            while i <= mid:
                tmp[k] = array[i]
                i += 1
                k += 1

            while j <= right:
                tmp[k] = array[j]
                j += 1
                k += 1
            # copy tmp to array
            array[left: right + 1] = tmp[left: right + 1]

        def core(l, r, array: list):
            if l < r:
                mid = (l + r) >> 1
                core(l, mid, array)
                core(mid + 1, r, array)
                merge(array, l, r)

        core(0, len(array) - 1, array)

    merge_sort(array)
    return array


if __name__ == '__main__':
    a = [1, 57, 83, 112, 5, 1, 23, 56, 73]
    solve(a)
    print(a)
