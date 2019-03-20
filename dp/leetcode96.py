#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-20
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


    //假设a[i-1]表示有1...(i-1)个节点组成的二叉搜索树的种类数，那么我们如何求a[i]呢？
    //https://blog.csdn.net/Jaster_wisdom/article/details/81148452
    //第一种情况，根节点为1，那么左子树必定为空，右子树为2...i个节点，那么种类数为1*a[i-1]，
    //也可以表示为a[0]*a[i-1]，即左边0个节点的情况，右边有i-1个节点的情况，它们之间是乘的关系。
    //a[i] = a[0]*a[i-1] + a[1]*a[i-2] + a[2]*a[i-3] + ... + a[i-1]*a[0]
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))
    print(solution.numTrees(4))
    print(solution.numTrees(10))
