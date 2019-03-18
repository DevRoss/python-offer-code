#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-22
import numpy as np


def solve(matrix: np.ndarray):
    max_mat = np.zeros(matrix.shape, dtype=np.int)
    rows, cols = matrix.shape
    for start in range(0, min(rows, cols)):
        for j in range(start, cols):
            # 第一行的情况
            if start == 0:
                if j == 0:
                    max_mat[start, j] = matrix[start, j]
                else:
                    max_mat[start, j] = max_mat[start, j - 1] + matrix[start, j]
            # 不是第一行的情况
            else:
                max_mat[start, j] = matrix[start, j] + max(max_mat[start - 1, j], max_mat[start, j - 1])
        for i in range(start + 1, rows):
            # 第一列的情况
            if start == 0:
                if i == 0:
                    max_mat[i, start] = matrix[i, start]
                else:
                    max_mat[i, start] = max_mat[i - 1, start] + matrix[i, start]
            # 不是第一列的情况
            else:
                max_mat[i, start] = matrix[i, start] + max(max_mat[i - 1, start], max_mat[i, start - 1])
    return max_mat[rows - 1, cols - 1]


if __name__ == '__main__':
    matrix = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(solve(np.array(matrix, dtype=np.int)))
