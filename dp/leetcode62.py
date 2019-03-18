#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-18

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

"""


def solve(m: int, n: int) -> int:
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, min(m, n)):
        for j in range(i, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for j in range(i, m):
            dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    print(solve(7, 3))
