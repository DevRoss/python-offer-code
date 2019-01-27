#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-21
import heapq


class MinHeap:
    def __init__(self):
        self.data = list()

    def heapify(self):
        heapq.heapify(self.data)

    def push(self, e):
        heapq.heappush(self.data, e)

    def pop(self):
        return heapq.heappop(self.data)

    def get_top(self):
        if not self.data:
            return
        return self.data[0]

    def __len__(self):
        return len(self.data)


class MaxHeap:
    def __init__(self):
        self.data = list()

    def heapify(self):
        heapq.heapify(self.data)

    def push(self, e):
        heapq.heappush(self.data, -e)

    def pop(self):
        return -heapq.heappop(self.data)

    def get_top(self):
        if not self.data:
            return
        return -self.data[0]

    def __len__(self):
        return len(self.data)


def solve(array: list):
    if not array:
        return None
    min_heap = MinHeap()
    max_heap = MaxHeap()

    for i in array:
        if len(max_heap) == 0:
            max_heap.push(i)

        if i < max_heap.get_top():
            max_heap.push(i)
            if len(max_heap) > len(min_heap):
                min_heap.push(max_heap.pop())
        else:
            min_heap.push(i)
            if len(min_heap) > len(max_heap):
                max_heap.push(min_heap.pop())
    # 当数组个数为单数，取长度大的堆的顶元素
    if len(array) & 1 != 0:
        if len(max_heap) > len(min_heap):
            return max_heap.get_top()
        else:
            return min_heap.get_top()
    # 双数的时候
    else:
        return (max_heap.get_top() + min_heap.get_top()) / 2


if __name__ == '__main__':
    print(solve([1, 2, 3, 4, 5]))
    print(solve([634, 1, 4, 5, 56, 3]))
    print(solve([]))
    print(solve([1]))
    print(solve([1, 5]))
