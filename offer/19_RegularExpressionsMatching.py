#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        # 当模式中的第二个字符是"*"时
        if len(pattern) > 1 and pattern[1] == "*":
            # 如果字符串第一个模式跟模式第一个字符匹配(相等或匹配到".")，可以有3种匹配方式：
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                # 1、模式后移2字符，相当于X*被忽略
                # 2、字符串后移1字符，模式后移两字符；
                # 3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)

            else:
                return self.match(s, pattern[2:])

        # 当模式中的第二个字符不是"*"时:
        # 1、如果字符串第一个字符和模式中的第一个字符匹配(相等或匹配到".")，那么字符串和模式都后移一个字符，然后匹配剩余的
        if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        # 2、如果字符串第一个字符和模拟中的第一个字符相不匹配，直接返回false
        return False


if __name__ == '__main__':
    pass
