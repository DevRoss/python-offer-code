#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 2019/8/23
import re


class Solution:
    def myAtoi(self, str: str) -> int:
        num = str.strip()
        if num == '':
            return 0
        syn = 1
        if num[0] == '-':
            syn = -1
            num = num[1:]
        elif num[0] == '+':
            num = num[1:]

        num = re.search(r"^\d+", num)
        if num:
            num = int(num.group())
            if syn == -1:
                num = -num
            if num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif num < -(2 ** 31):
                return -(2 ** 31)
            else:
                return num
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi(" -42ffff"))
    print(s.myAtoi(" -"))
    print(s.myAtoi(" "))
    print(s.myAtoi(""))

