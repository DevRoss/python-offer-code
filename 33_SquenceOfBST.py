#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) <= 0:
            return False
        root = sequence[-1]
        i = 0

        # 找出左小右大的分界点i,此时i属于右子树
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1

        # 如果在右子树中有比根节点小的值，直接返回False
        for node in sequence[i:-1]:
            if node < root:
                return False
        # 判断左子树是否为二叉搜索树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        # 判断右子树是否为二叉搜索树
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right


if __name__ == '__main__':
    pass
