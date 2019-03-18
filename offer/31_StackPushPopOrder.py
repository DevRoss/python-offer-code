#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            # 相当于元素进栈后立即出栈
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            # 如果当前辅助栈中的栈顶元素刚好是要弹出的元素，那么直接弹出
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            # 不断往辅助栈中压入元素
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True


if __name__ == '__main__':
    pass
