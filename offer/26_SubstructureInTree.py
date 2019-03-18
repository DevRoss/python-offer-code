#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.SubtreeCore(pRoot1, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        return res

    def SubtreeCore(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.SubtreeCore(pRoot1.left, pRoot2.left) and self.SubtreeCore(pRoot1.right, pRoot2.right)


if __name__ == '__main__':
    pass
