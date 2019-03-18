#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18


class Node:
    def __init__(self, x):
        self.val = x
        self.lchild = None
        self.rchild = None


class ListNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


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


def travel(node: ListNode):
    if not node:
        return
    # 向右遍历
    while node:
        print(node.value, end=' ')
        node = node.right


def solve(tree):
    if not tree:
        return None

    tail = ListNode(0)
    list_node = tail

    # 中序遍历，向前添加结点
    def construct_list(node: Node):
        nonlocal list_node
        if not node:
            return
        construct_list(node.lchild)
        list_node.left = ListNode(node.val)
        list_node = list_node.left
        construct_list(node.rchild)

    construct_list(tree)
    p = tail
    while p.left:
        p.left.right = p
        p = p.left
    tail.left.right = None
    return p


if __name__ == '__main__':
    tree = create_binary_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6], 8)
    head = solve(tree)
    travel(head)
    print()
    travel(solve(Node(9999)))
    print()
    travel(solve(None))
