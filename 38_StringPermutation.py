#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-19


def solve(string: str):
    if not string:
        return
    str_list = list(string)

    def core(s: list, index):
        if index >= len(s):
            print(''.join(s))

        else:
            for i in range(index, len(s)):
                s[index], s[i] = s[i], s[index]  # 第一个与后面的交换
                core(s, index + 1)
                s[index], s[i] = s[i], s[index]  # 还原

    core(str_list, 0)


if __name__ == '__main__':
    solve('')
