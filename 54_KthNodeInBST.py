#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-24


class Node:
    def __init__(self, x):
        self.val = x
        self.lchild = None
        self.rchild = None


def construct(start_pre, end_pre, start_in, end_in,
              pre_order: list, in_order: list):
    # 先找根节点
    root_value = pre_order[start_pre]
    root_in_index = in_order.index(root_value, start_in, end_in + 1)
    root = Node(root_value)
    left_len = root_in_index - start_in  # 左子树长度
    right_len = end_in - root_in_index  # 右子树长度

    # 构建左子树
    if start_in < root_in_index:
        root.lchild = construct(start_pre + 1, start_pre + left_len,
                                start_in, root_in_index - 1, pre_order, in_order)
    # 构建右子树
    if root_in_index < end_in:
        root.rchild = construct(end_pre - right_len + 1, end_pre,
                                root_in_index + 1, end_in,
                                pre_order, in_order)
    return root


def create_binary_tree(pre_order: list, in_order: list, length: int) -> Node:
    if not pre_order or not in_order or length <= 0:
        return None
    return construct(0, length - 1, 0, length - 1, pre_order, in_order)


def solve(root: Node, k):
    if not root:
        return False

    def in_order(root: Node):
        nonlocal k
        if not root or k == 0:
            return None
        target = in_order(root.lchild)
        if not target:
            if k == 1:
                target = root
            k -= 1
        if not target:
            target = in_order(root.rchild)
        return target

    return in_order(root)


if __name__ == '__main__':
    tree = create_binary_tree([5, 3, 2, 4, 7, 6, 8], [2, 3, 4, 5, 6, 7, 8], 7)
    ret = solve(tree, 1)
    print(ret.val)
    ret = solve(tree, 2)
    print(ret.val)
    ret = solve(tree, 3)
    print(ret.val)
    ret = solve(tree, 4)
    print(ret.val)
    ret = solve(tree, 5)
    print(ret.val)
    ret = solve(tree, 8)
    print(ret)
    ret = solve(tree, 9)
    print(ret)
