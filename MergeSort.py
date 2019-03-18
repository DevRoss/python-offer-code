#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-7


def solve(array):
    def merge_sort(array: list):
        def merge(array, left, mid, right, tmp):
            i = left
            j = mid + 1
            k = left
            while i <= mid and j <= right:
                if array[i] <= array[j]:
                    tmp[k] = array[i]
                    i += 1
                    k += 1
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

            array[left:right + 1] = tmp[left:right + 1]

        def core(l, r, array: list, tmp: list):
            if l < r:
                mid = (l + r) >> 1
                core(l, mid, array, tmp)
                core(mid + 1, r, array, tmp)
                merge(array, l, mid, r, tmp)

        tmp = array.copy()
        core(0, len(array) - 1, array, tmp)

    merge_sort(array)


if __name__ == '__main__':
    a = [1, 57, 83, 112, 5, 1, 23, 56, 73]
    solve(a)
    print(a)
