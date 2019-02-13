#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-24


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solve(l1: ListNode, l2: ListNode):
    p1 = l1
    p2 = l2
    len1 = 0
    len2 = 0
    while p1:
        len1 += 1
        p1 = p1.next
    while p2:
        len2 += 1
        p2 = p2.next
    p1 = l1
    p2 = l2

    # 长的先向前走
    if len1 > len2:
        for i in range(len1 - len2):
            p1 = p1.next
    if len1 < len2:
        for i in range(len2 - len1):
            p2 = p2.next

    while p1 and p2 and p1.val != p2.val:
        p1 = p1.next
        p2 = p2.next
    if p1 is None or p2 is None:
        return None
    return p1


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(10)
    p1 = l1
    p2 = l2
    for i in range(2, 6):
        p1.next = ListNode(i)
        p1 = p1.next
    for i in range(11, 18):
        p2.next = ListNode(i)
        p2 = p2.next

    ret = solve(l1, l2)
    if ret:
        print(ret.val)

    for i in range(30, 35):
        node = ListNode(i)
        p1.next = node
        p2.next = node
        p1 = p1.next
        p2 = p2.next

    ret = solve(l1, l2)
    if ret:
        print(ret.val)

    ret = solve(ListNode(1), ListNode(1))
    if ret:
        print(ret.val)
