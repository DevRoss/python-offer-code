#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class Solution:
    # s字符串
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s or len(s) <= 0:
            return False
        alist = [i.lower() for i in s]
        if 'e' in alist:
            index = alist.index('e')
            front = alist[:index]
            behind = alist[index + 1:]
            if '.' in behind or len(behind) == 0:
                return False
            isfront = self.isDigit(front)
            isbehind = self.isDigit(behind)
            return isfront and isbehind
        else:
            return self.isDigit(alist)

    def isDigit(self, alist):
        dotNum = 0
        allow_num = ['0', '1', '2', '3', '4', '5',
                     '6', '7', '8', '9', '+', '-', '.']
        for i in range(len(alist)):
            if alist[i] not in allow_num:
                return False
            if alist[i] == '.':
                dotNum += 1
            if alist[i] in '+-' and i != 0:
                return False
        if dotNum > 1:
            return False
        return True


if __name__ == '__main__':
    pass
