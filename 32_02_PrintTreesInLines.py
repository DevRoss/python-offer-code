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
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        res_val = []
        res.append(pRoot)

        nextLevel = 0  # 表示下一层节点的数目
        toBePrinted = 1  # 表示当前层还没有打印的节点数
        temp = []
        while len(res) > 0:
            node = res[0]
            temp.append(node.val)
            if node.left:
                res.append(node.left)
                nextLevel += 1

            if node.right:
                res.append(node.right)
                nextLevel += 1

            del res[0]
            toBePrinted -= 1
            if toBePrinted == 0:
                res_val.append(temp)
                toBePrinted = nextLevel
                nextLevel = 0
                temp = []
        return res_val


if __name__ == '__main__':
    pass
