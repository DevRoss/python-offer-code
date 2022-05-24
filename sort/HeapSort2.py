#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   HeapSort2.py
@Time    :   2022/05/24 20:15:33
@Author  :   Ross
@Desc    :   heap sort implementation
'''


class HeapSort:

    @staticmethod
    def adj_heap(array, start, end):
        left = start * 2 + 1
        right = start * 2 + 2
        candidate = start
        if left <= end and array[left] < array[candidate]:
            candidate = left
        if right <= end and array[right] < array[candidate]:
            candidate = right
        if candidate != start:
            array[candidate], array[start] = array[start], array[candidate]
            HeapSort.adj_heap(array, candidate, end)

    @staticmethod
    def heap_sort(array):
        length = len(array)
        for i in range(length // 2 - 1, -1, -1):
            HeapSort.adj_heap(array, i, length - 1)
        for i in range(length - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            HeapSort.adj_heap(array, 0, i - 1)


if __name__ == '__main__':
    a = [5, 1, 78, 3, 54, 2, 16, 88, 89, 6, 54, 44]
    HeapSort.heap_sort(a)
    print(a)
