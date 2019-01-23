#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-16

class Node:
    def __init__(self, x):
        self.val = x
        self.lchild = None
        self.rchild = None


# 使用07_ConstructBinaryTree的代码
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


# 使用07_ConstructBinaryTree的代码
def create_binary_tree(pre_order: list, in_order: list, length: int) -> Node:
    if not pre_order or not in_order or length <= 0:
        return None
    return construct(0, length - 1, 0, length - 1, pre_order, in_order)


def in_order(node: Node, trace: list):
    if not node:
        return
    in_order(node.lchild, trace)
    trace.append(node.val)
    in_order(node.rchild, trace)


def is_symmetrical(trace: list) -> bool:
    i = 0
    j = len(trace) - 1
    while i < j:
        if trace[i] != trace[j]:
            return False
        i += 1
        j -= 1
    return True


def solve(tree: Node):
    if not tree:
        return False
    trace = list()
    in_order(tree, trace)
    return is_symmetrical(trace)


if __name__ == '__main__':
    print(solve(create_binary_tree([1, 2, 2], [2, 1, 2], 3)))
    print(solve(create_binary_tree([1], [1], 1)))
    print(solve(create_binary_tree([], [], 0)))
    print(solve(create_binary_tree([1, 2, 4, 2, 4], [2, 4, 1, 2, 4], 5)))
    print(solve(create_binary_tree([1, 2, 4, 2, 4], [2, 4, 1, 4, 2], 5)))

