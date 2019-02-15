#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-24


class Node:
    def __init__(self, x):
        self.val = x
        self.lchild = None
        self.rchild = None


def serialize(node: Node, string: str):
    if not node:
        return string + '$'
    string += node.val
    string = serialize(node.lchild, string)
    string = serialize(node.rchild, string)
    return string


def deserialize(string: str):
    index = -1
    str_len = len(string)

    def core(string: str):
        nonlocal index, str_len
        if index > str_len:
            return None
        index += 1
        root = None
        if string[index] != '$':
            root = Node(string[index])
            root.lchild = core(string)
            root.rchild = core(string)
        return root

    return core(string)


def solve(root: Node):
    def post_order(root: Node):
        if not root:
            return False

        left_depth = post_order(root.lchild)
        right_depth = post_order(root.rchild)
        if left_depth < 0 or right_depth < 0 or abs(left_depth - right_depth) > 1:
            return -1

        depth = max(left_depth, right_depth)
        return depth + 1

    ret = post_order(root)
    if ret < 0:
        return False
    return True


if __name__ == '__main__':
    tree = deserialize('123$$$356$$$689$$$$')
    print(solve(tree))
    tree = deserialize('12$$3$$')
    print(solve(tree))
    tree = Node(1)
    print(solve(tree))
