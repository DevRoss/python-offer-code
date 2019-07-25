#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 2019/7/24

# 背包最大容量
max_w = 10
# 物品的重量以及相应的价值
w_vs = [(2, 6),
        (2, 3),
        (6, 5),
        (5, 4),
        (4, 6)]


def solve(max_w, w_vs):
    dp = [[0] * (max_w + 1) for _ in range(len(w_vs))]
    for i in range(0, len(w_vs)):
        for j in range(1, max_w + 1):
            if j < w_vs[i][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - w_vs[i][0]] + w_vs[i][1], dp[i - 1][j])

    for i in dp:
        print(i)


if __name__ == '__main__':
    solve(max_w, w_vs)
