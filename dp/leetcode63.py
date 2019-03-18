#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-18

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

"""


def solve(obstacleGrid: list) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        if obstacleGrid[i][0]:
            break
        dp[i][0] = 1

    for i in range(n):
        if obstacleGrid[0][i]:
            break
        dp[0][i] = 1

    for i in range(1, min(m, n)):
        for j in range(i, n):
            if obstacleGrid[i][j]:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for j in range(i, m):
            if obstacleGrid[j][i]:
                dp[j][i] = 0
            else:
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    test_case = [[0, 0, 0],
                 [0, 1, 0],
                 [0, 0, 0]]
    print(solve(test_case))
