#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-18
"""
最长公共子序列
参考：   https://www.kancloud.cn/digest/pieces-algorithm/163624
        https://blog.csdn.net/hrn1216/article/details/51534607
"""


def solve(str1: str, str2: str):
    def dp(str1: str, str2: str):
        # 二维数组
        mat = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
        for i in range(1, len(str2) + 1):
            for j in range(1, len(str1) + 1):
                if str2[i - 1] == str1[j - 1]:
                    mat[i][j] = mat[i - 1][j - 1] + 1
                else:
                    mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

        return mat

    def trace(mat, i, j):
        if i < 1 or j < 1 or mat[i][j] == 0:
            return

        if str1[j - 1] == str2[i - 1]:
            trace(mat, i - 1, j - 1)
            print(str1[j - 1], end=' ')
        # 向上走
        elif str1[j - 1] == str2[i - 2]:
            trace(mat, i - 1, j)
        # 向左走
        else:
            trace(mat, i, j - 1)

    mat = dp(str1, str2)
    trace(mat, len(str2), len(str1))


#     print(i)


if __name__ == '__main__':
    solve('BDCABA', 'ABCBDAB')
