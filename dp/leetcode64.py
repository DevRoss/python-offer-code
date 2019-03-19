#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-19
"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


def solve(grid: list) -> int:
    m, n = len(grid), len(grid[0])
    for i in range(1, n):
        grid[0][i] = grid[0][i - 1] + grid[0][i]

    for i in range(1, m):
        grid[i][0] = grid[i - 1][0] + grid[i][0]

    for i in range(1, min(m, n)):
        for j in range(i, n):
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        for j in range(i + 1, m):
            grid[j][i] = min(grid[j - 1][i], grid[j][i - 1]) + grid[j][i]

    # for i in grid:
    #     print(i)
    return grid[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    print(solve(grid))
