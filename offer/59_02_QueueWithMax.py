#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-25
from collections import deque


class Q:
    def __init__(self):
        self.data = deque()
        self.max_q = deque()

    def max(self):
        if not len(self.data):
            raise IndexError('Can not call max when the queue is empty.')
        return self.max_q[0]

    def push(self, e):
        if len(self.max_q) == 0:
            self.max_q.append(e)
        elif e == self.max_q[0]:
            self.max_q.appendleft(e)
        elif e == self.max_q[-1]:
            self.max_q.append(e)
        else:
            while len(self.max_q) and e > self.max_q[-1]:
                self.max_q.pop()
            self.max_q.append(e)
        self.data.append(e)

    def pop(self):
        if len(self.data) == 0:
            raise IndexError('Can not pop on a empty queue.')
        ret = self.data.popleft()
        if ret == self.max_q[0]:
            self.max_q.popleft()
        return ret


if __name__ == '__main__':
    q = Q()
    for i in [1, 3, 5, 2, 7, 10, 2, 20]:
        q.push(i)
        print(q.data)
        print(q.max_q)
        print('=' * 20)
