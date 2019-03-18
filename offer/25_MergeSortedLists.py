#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        pMergedHead = None
        if (pHead1.val < pHead2.val):
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1, pHead2.next)

        return pMergedHead


if __name__ == '__main__':
    pass
