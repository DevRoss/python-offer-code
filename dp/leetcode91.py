#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-19

"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        s = '0' + s
        length = len(s)
        dp = [1] * (length)

        for i in range(1, length):
            c = 0
            single = s[i]  # 一位数
            if single != '0':
                c += dp[i - 1]
            double = s[i - 1:i + 1]  # 两位数
            if (not double.startswith('0')) and 0 < int(double) < 27:
                c += dp[i - 2]
            dp[i] = c
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings('12'))
    print(solution.numDecodings('226'))
