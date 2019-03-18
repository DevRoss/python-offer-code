#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solve(ln: ListNode):
    if not ln:
        return
    p = ln
    while p:
        print(p.val, end=' ')
        p = p.next
    print()


def test1():
    print('test1')
    ln = None
    solve(ln)


def test2():
    print('test2')
    ln = ListNode(1)
    solve(ln)


def test3():
    print('test3')
    ln = ListNode(-1)
    p = ln
    for i in range(5):
        p.next = ListNode(i)
        p = p.next
    solve(ln.next)


if __name__ == '__main__':
    test1()
    test2()
    test3()
