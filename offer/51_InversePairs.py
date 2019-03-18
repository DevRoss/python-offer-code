#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-24


def solve(array: list):
    def core(data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        left = core(copy, data, start, start + length)
        right = core(copy, data, start + length + 1, end)
        i = start + length
        j = end
        index_copy = end
        count = 0
        while start <= i and start + length + 1 <= j:
            # 计数
            if data[i] > data[j]:
                copy[index_copy] = data[i]
                index_copy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[index_copy] = data[j]
                index_copy -= 1
                j -= 1
        while start <= i:
            copy[index_copy] = data[i]
            index_copy -= 1
            i -= 1
        while start + length + 1 <= j:
            copy[index_copy] = data[j]
            index_copy -= 1
            j -= 1

        return left + right + count

    if not array:
        return 0
    cp = array.copy()
    return core(array, cp, 0, len(array) - 1)


if __name__ == '__main__':
    print(solve([7, 5, 6, 4]))
    print(solve([7, 6, 4]))
    print(solve([7, 6, 56, 5524, 62, 2, 8]))
