#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-8

class Queue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, e):
        self.stack1.append(e)

    def pop(self):
        if len(self.stack2) <= 0:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) <= 0:
            raise Exception("queue is empty")
        return self.stack2.pop()


if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        q.push(i)
    for i in range(6):
        print(q.pop())
