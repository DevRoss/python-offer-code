#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-29
"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        i = 0
        j = len(height) - 1
        max_ = 0
        while i < j:
            tmp = min(height[i], height[j]) * (j - i)
            max_ = max(max_, tmp)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_


if __name__ == '__main__':
    pass
