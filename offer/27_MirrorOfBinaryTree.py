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
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        if not root.left and not root.right:
            return
        pTemp = root.left
        root.left = root.right
        root.right = pTemp

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)


if __name__ == '__main__':
    pass
