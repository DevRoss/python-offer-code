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
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []

        def FindPathCore(root, path, currentNum):
            currentNum += root.val
            path.append(root)
            # 判断是否达到叶子节点
            flag = (root.left == None and root.right == None)

            # 如果到达叶子节点且当前值等于期望值
            if currentNum == expectNumber and flag:
                onepath = []
                for node in path:
                    onepath.append(node.val)
                result.append(onepath)

            if currentNum < expectNumber:
                if root.left:
                    FindPathCore(root.left, path, currentNum)
                if root.right:
                    FindPathCore(root.right, path, currentNum)
            path.pop()

        FindPathCore(root, [], 0)
        return result


if __name__ == '__main__':
    pass
