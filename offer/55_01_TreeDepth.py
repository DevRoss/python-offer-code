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
    if not root:
        return 0
    depth = 0
    max_depth = 0

    def pre_order(root: Node):
        nonlocal depth, max_depth
        if not root:
            return

        depth += 1
        max_depth = max(depth, max_depth)
        pre_order(root.lchild)
        pre_order(root.rchild)
        depth -= 1

    pre_order(root)
    return max_depth


if __name__ == '__main__':
    tree = deserialize('123$$$35$$68$$$')
    print(solve(tree))
    print(solve(Node(1)))
    print(solve(None))
