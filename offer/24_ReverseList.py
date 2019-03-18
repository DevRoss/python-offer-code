#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pReversedHead = None
        pNode = pHead
        pPrev = None
        while pNode:
            pNext = pNode.next
            if not pNext:
                pReversedHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead


if __name__ == '__main__':
    pass
