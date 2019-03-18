#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18


class ComplexListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.sbiling = None


def solve(src: ComplexListNode):
    if not src:
        return

    dest = ComplexListNode(src.val)
    p_src = src
    p_dest = dest
    table = dict()  # 用于查找节点
    while p_src:
        table[p_src] = p_dest
        if p_src.next:
            p_dest.next = ComplexListNode(p_src.next.val)
        p_dest = p_dest.next
        p_src = p_src.next

    p_src = src
    p_dest = dest
    while p_src:
        if p_src.sbiling is not None:
            p_dest.sbiling = table[p_src.sbiling]
        p_dest = p_dest.next
        p_src = p_src.next
    return dest


if __name__ == '__main__':
    head = ComplexListNode(0)
    p = head
    l = [head]
    for i in range(1, 6):
        p.next = ComplexListNode(i)
        p = p.next
        l.append(p)
    l[4].sbiling = l[1]
    l[2].sbiling = l[5]
    copied = solve(head)
    p_dest = copied
    while p_dest:
        print(p_dest.val, end=' ')
        if p_dest.sbiling:
            print(p_dest.sbiling.val, end=' ')
        print()
        p_dest = p_dest.next
