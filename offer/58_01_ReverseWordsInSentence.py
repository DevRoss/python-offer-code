#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-25


def solve(string: str):
    if string is None:
        return
    return ' '.join(reversed(string.split(' ')))


if __name__ == '__main__':
    print(solve('I am a student.'))
    print(solve(''))
    print(solve('I'))
    print(solve('I am'))
