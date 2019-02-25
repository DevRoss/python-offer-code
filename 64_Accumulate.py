#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-26

functions = None


class Function:
    @classmethod
    def end(cls, e):
        return 0

    @classmethod
    def add(cls, e):
        global functions
        return functions[not not e](e - 1) + e

    @classmethod
    def sum(cls, n):
        return cls.add(n)


if __name__ == '__main__':
    functions = [Function.end, Function.add]
    print(Function.sum(4))
