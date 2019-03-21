#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-3-21

"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
"""

MININT = 0x80000000
MAXINT = 0x7FFFFFFF


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 表示有且只有一个负数
        negative = dividend ^ divisor < 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                result += (1 << i)
                dividend -= (divisor << i)
        if negative:
            return -result
        return min(result, MAXINT)  # 溢出


if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(7, 3))
    print(solution.divide(7, -3))
    print(solution.divide(-3, -3))
    print(solution.divide(-2147483648, -1))
