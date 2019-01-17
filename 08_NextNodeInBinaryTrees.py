#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-8


class Node:
    def __init__(self, x, p):
        self.val = x
        self.lchild = None
        self.rchild = None
        self.parent = p


def construct(start_pre, end_pre, start_in, end_in,
              pre_order: list, in_order: list, parent):
    root_value = pre_order[start_pre]
    root_in_index = in_order.index(root_value, start_in, end_in + 1)
    root = Node(root_value, parent)
    left_len = root_in_index - start_in  # 左子树长度
    right_len = end_in - root_in_index  # 右子树长度
    if start_in < root_in_index:
        root.lchild = construct(start_pre + 1, start_pre + left_len,
                                start_in, root_in_index - 1, pre_order, in_order, root)
    if root_in_index < end_in:
        root.rchild = construct(end_pre - right_len + 1, end_pre,
                                root_in_index + 1, end_in,
                                pre_order, in_order, root)
    return root


def create_binary_tree(pre_order: list, in_order: list, length: int) -> Node:
    if not pre_order or not in_order or length <= 0:
        return None
    return construct(0, length - 1, 0, length - 1, pre_order, in_order, None)


def solve(node: Node) -> Node or None:
    p = node
    # 有右子数
    if p.rchild:
        p = p.rchild
        while p.lchild:
            p = p.lchild
        return p
    # 有父结点
    elif p.parent:
        while p.parent and p.parent.rchild is p:  # 如果是右结点，就向上走，是左结点就输出
            p = p.parent
        return p.parent
    # 根结点
    else:
        return None


def in_order_search(node: Node, key):
    global ret
    if node.lchild:
        in_order_search(node.lchild, key)
    if key == node.val:
        ret = node
        return
    if node.rchild:
        in_order_search(node.rchild, key)


if __name__ == '__main__':
    tree = create_binary_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6], 8)
    for i in [4, 7, 2, 1, 5, 3, 8, 6]:
        ret = None
        in_order_search(tree, i)
        print(ret.val, end=' ')
        ret = solve(ret)
        if ret is None:
            print(None)
        else:
            print(ret.val)
        print('---')
