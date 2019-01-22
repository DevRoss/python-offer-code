#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-15


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def count_node(p: ListNode):
    p_slow = p
    p_fast = p
    c = 0
    while True:
        p_slow = p_slow.next
        p_fast = p_fast.next.next
        c += 1
        if p_slow == p_fast:
            break
    return c


def solve(head: ListNode):
    if not head:
        return None

    p_fast = head
    p_slow = head
    # 判断有没有环
    while p_fast and p_slow:
        p_slow = p_slow.next
        p_fast = p_fast.next
        if p_fast is None or p_fast.next is None:
            return None
        else:
            p_fast = p_fast.next
        if p_slow == p_fast:
            break
    # 有环
    num_node = count_node(p_slow)
    p_slow = head
    p_fast = head
    # 前面的指针向前走num_node步
    for i in range(num_node):
        p_fast = p_fast.next
    while p_slow != p_fast:
        p_slow = p_slow.next
        p_fast = p_fast.next
    return p_slow


if __name__ == '__main__':
    head = ListNode(1)
    p = head
    for i in range(2, 8):
        p.next = ListNode(i)
    p_entry = p
    for i in range(8, 12):
        p.next = ListNode(i)

    assert solve(head) is None
    p.next = p_entry
    assert solve(head) is p_entry

    assert solve(ListNode(1)) is None
    assert solve(None) is None
