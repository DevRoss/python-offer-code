#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next
        res = list(filter(lambda c: res.count(c) == 1, res))

        newList = ListNode(0)
        pre = newList
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return newList.next


if __name__ == '__main__':
    pass
