#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        pAhead = head
        pBehind = None
        for i in range(k - 1):
            if pAhead.next:
                pAhead = pAhead.next
            else:
                return None
        pBehind = head
        while pAhead.next:
            pAhead = pAhead.next
            pBehind = pBehind.next
        return pBehind


if __name__ == '__main__':
    pass
