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
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        res_val = []
        res.append(root)
        while len(res) > 0:
            node = res.pop(0)
            res_val.append(node.val)
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
        return res_val


if __name__ == '__main__':
    pass
