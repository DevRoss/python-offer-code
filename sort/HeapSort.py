#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 2019/9/3


def heap_sort(array):
    end = len(array) - 1
    # 从下往上构造最大堆
    for i in range(end // 2 - 1, -1, -1):
        adj_heap(array, i, end)

    while end >= 0:
        array[0], array[end] = array[end], array[0]
        end -= 1
        adj_heap(array, 0, end)


def top_k(array, k):
    end = len(array) - 1
    for i in range(end // 2 - 1, -1, -1):
        adj_heap(array, i, end)
    for i in range(k):
        array[0], array[end] = array[end], array[0]
        end -= 1
        adj_heap(array, 0, end)


def adj_heap(array, i, end):
    while i < end // 2:
        left = i * 2 + 1
        right = left + 1
        j = left  # 指针指向左节点
        if right <= end and array[right] > array[left]:  # 存在右节点，且右节点大于左节点
            j = right
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            break
        i = j


if __name__ == '__main__':
    case1 = [20, 50, 20, 40, 70, 10, 80, 30, 60]
    heap_sort(case1)
    print(case1)

    case2 = [200, 50, 2, 40, 70, 10, 80, 30, 6]
    top_k(case2, 5)
    print(case2)

    case3 = [20, 50, 20, 40, 70, 10, 80, 30, 60, 2, 12, 5155, 66, 24, 89]
    heap_sort(case3)
    print(case3)
