#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())

    def pop(self):
        # write code here
        if self.stack == [] or self.minstack == []:
            return None
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minstack[-1]


if __name__ == '__main__':
    pass
