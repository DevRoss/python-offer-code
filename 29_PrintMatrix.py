#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
            return
        start = 0
        rows = len(matrix)
        columns = len(matrix[0])
        res = []
        while (columns > start * 2 and rows > start * 2):
            self.printMatrixInCircle(matrix, columns, rows, start, res)
            start += 1

        return res

    def printMatrixInCircle(self, matrix, columns, rows, start, res):
        endX = columns - 1 - start
        endY = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, endX + 1):
            res.append(matrix[start][i])

        # 从上到下打印一列
        if start < endY:
            for i in range(start + 1, endY + 1):
                res.append(matrix[i][endX])

        # 从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX - 1, start - 1, -1):
                res.append(matrix[endY][i])

        # 从下到上打印一列
        if start < endX and start < endY - 1:
            for i in range(endY - 1, start, -1):
                res.append(matrix[i][start])


if __name__ == '__main__':
    pass
