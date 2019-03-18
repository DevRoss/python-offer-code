#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class Solution:
    def reOrderArray(self, array):
        # write code here
        if array == None or len(array) == 0:
            return
        pBegin = 0
        pEnd = len(array) - 1
        while (pBegin < pEnd):
            while pBegin < pEnd and not self.isEven(array[pBegin]):
                pBegin += 1
            while pBegin < pEnd and self.isEven(array[pEnd]):
                pEnd -= 1
            if pBegin < pEnd:
                temp = array[pBegin]
                array[pBegin] = array[pEnd]
                array[pEnd] = temp
        return array

    def isEven(self, number):
        return number & 1 == 0


if __name__ == '__main__':
    pass
